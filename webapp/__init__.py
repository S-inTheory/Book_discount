from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required
from flask_migrate import Migrate

from webapp.user.models import db, User
from webapp.books.models import db, Book
from webapp.books.forms import SearchForm
from webapp.books.parsers import books_find
from webapp.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/', methods=['GET'])
    def index():
        page_title = 'Главная страница'
        search_form = SearchForm()
        return render_template('/base.html', title=page_title, form=search_form)

    @app.route('/', methods=['POST'])
    def search_result():
        page_title = 'Результаты поиска'
        form = SearchForm()
        if form.validate_on_submit():
            try:
                new_book = Book.title
                books_list = new_book.query.filter(Book.title.like('%' + form.book.data + '%'))
                return render_template('books/search_result.html', title=page_title, books_list=books_list, form=form)
            except TypeError:
                print('Такой книги не нашлось, поискать ещё?')
        return render_template('books/search_result.html', title=page_title, form=form)

    @app.route('/search_process', methods=['POST'])
    def search_process():
        form = SearchForm()
        new_book = form.book.data
        books_find.get_search_books(new_book)
        return render_template('books/search_result.html', form=form)

    @app.route('/main')
    @login_required
    def content_page():
        return render_template('main.html')

    return app
