from webapp import create_app
from webapp.books.parsers.labirint_and_book24_find import get_search_books

app = create_app()
with app.app_context():
    get_search_books('томминокеры')