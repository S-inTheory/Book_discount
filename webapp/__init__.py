from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_required
from flask_migrate import Migrate

from webapp.user.models import db, User, Book
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

    @app.route('/search_process', methods=['POST'])
    def search_process():
        form = SearchForm()
        new_book = form.book.data
        return books_find.get_search_books(new_book)




    @app.route('/main')
    @login_required
    def content_page():
        return render_template('main.html')

    return app
