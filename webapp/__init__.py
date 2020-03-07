from flask import Flask, render_template, flash, redirect

from webapp.model import db
from webapp.forms import LoginForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        page_title = 'Главная страница'
        return render_template('index.html', title=page_title)

    @app.route('/register')
    def register():
        form = LoginForm()
        if form.validate_on_submit():
            flash('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect('/')
        return render_template('register.html', title='Sign Up', form=form)

    @app.route('/login')
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            flash('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect('/')
        return render_template('login.html', title='Sign In', form=form)
    return app
    return app.add_url_rule('/img/<path:filename>')





