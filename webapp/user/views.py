from flask import Blueprint, render_template, redirect, url_for, flash, request
from webapp.user.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from webapp.user.models import User, Book
from webapp import db
from webapp.user.forms import SearchForm
from webapp.books.parsers import labirint_and_book24_find

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    return render_template('user/login.html', title='Sign In', form=login_form)


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('index'))


@blueprint.route('/process_login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
        flash('Вы вошли на сайт')
        return redirect(url_for('index'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    return render_template('user/registration.html', title='Sign Up', form=form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(form, field).label.text, error
                                                        ))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('user.register'))


@blueprint.route('/', methods=['GET'])
def search_form():
    form = SearchForm(request.form)
    if form.validate_on_submit():
        book = Book(title=form.title.data)
        labirint_and_book24_find.get_search_books(book)
    return render_template('menu.html', title='Search', form=form)





