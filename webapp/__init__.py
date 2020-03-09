from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_required, current_user, login_user, logout_user

from webapp.model import db, User
from webapp.forms import LoginForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        page_title = 'Главная страница'
        return render_template('index.html', title=page_title)



    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        login_form = LoginForm()
        return render_template('login.html', title='Sign In', form=login_form)

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))

    @app.route('/process_login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('index'))
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/main')
    @login_required
    def content_page():
        return render_template('main.html')

    return app
    return app.add_url_rule('/img/<path:filename>')





