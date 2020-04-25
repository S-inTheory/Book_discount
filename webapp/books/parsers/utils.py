import requests
from webapp.books.models import Impressum, Book, db


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 '
                      'Safari/537.36 '
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def save_books(title=None, price_labirint=None, url_labirint=None, price_book24=None, url_book24=None):
    new_book = Book(title=title, price_labirint=price_labirint, url_labirint=url_labirint, url_book24=url_book24,
                    price_book24=price_book24, )
    db.session.add(new_book)
    db.session.commit()



