import requests
from webapp.user.models import db, Book, Impressum


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


def save_impressum(author='', publisher=''):
    new_author = Impressum(author=author)
    new_publisher = Impressum(publisher=publisher)
    db.session(new_author)
    db.session(new_publisher)
    db.session.commit()


def save_books(title=None, price_labirint=None, url_labirint=None, price_book24=None, url_book24=None):
    new_book = Book(title=title, price_labirint=price_labirint, url_labirint=url_labirint)
    book24 = Book(price_book24=price_book24, url_book24=url_book24)
    db.session.add(new_book)
    db.session.add(book24)
    db.session.commit()



