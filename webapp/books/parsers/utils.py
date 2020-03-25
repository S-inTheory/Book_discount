import requests
from webapp.user.models import db, Book, Impressum
from bs4 import BeautifulSoup


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
    new_author_publisher = Impressum(author=author, publisher=publisher)
    db.session(new_author_publisher)
    db.session.commit()


def save_books(title='', price_labirint='', url_labirint='', price_book24=0, url_book24=''):
    new_book = Book(title=title, price_labirint=price_labirint, url_labirint=url_labirint, price_book24=price_book24,
                    url_book24=url_book24)
    db.session.add(new_book)
    db.session.commit()



