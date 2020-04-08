from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, BooleanField, SubmitField, Form
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User, Book


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit_sign_in = SubmitField('Sign In', render_kw={'class': 'btn btn-primary'})
    remember_me = BooleanField('Remember me', default=True, render_kw={'class': 'form-check-input'})


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')],
                              render_kw={"class": "form-control"})
    submit = SubmitField('Sign Up', render_kw={"class": "btn btn-primary"})

    def validate_username(self, username):
        user_count = User.query.filter_by(username=username.data).count()
        if user_count > 0:
            raise ValidationError('Пользователь с таким именем уже существует')

    def validate_email(self, email):
        email_count = User.query.filter_by(email=email.data).count()
        if email_count > 0:
            raise ValidationError('Пользователь с такой почтой уже существует')


class SearchForm(Form):
    title = StringField('title', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Search', render_kw={"class": "btn btn-primary"})

    def validate_title(self, title):
        book_count = Book.query.filter_by(title=title.data)
        if book_count > 0:
            raise ValidationError('Такая книга есть в нашей базе данных, сейчас мы вам её покажем')
