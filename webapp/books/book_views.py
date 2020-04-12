# from flask import Blueprint, request
# from webapp.user.models import Book
# from webapp.books.forms import SearchForm
# from webapp.books.parsers import books_find
#
# blueprint = Blueprint('books', __name__, url_prefix='/books')
#
#
# @blueprint.route('/', methods=['GET'])
# def search_form(form):
#     form = SearchForm(request.form)
#     if form.validate_on_submit():
#         book = Book(title=form.title.data)
#         books_find.get_search_books(book)

