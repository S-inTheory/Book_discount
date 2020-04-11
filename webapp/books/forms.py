from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from webapp.user.models import Book

class SearchForm(Form):
    title = StringField('title', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Search', render_kw={"class": "btn btn-primary"})

    def validate_title(self, title):
        book_count = Book.query.filter_by(title=title.data)
        if book_count > 0:
            raise ValidationError('Такая книга есть в нашей базе данных, сейчас мы вам её покажем')