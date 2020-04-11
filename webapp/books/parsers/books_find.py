import bs4
import os
from urllib import request

from webapp.books.parsers.utils import get_html, save_books, save_impressum


def get_search_books(book):
    html = get_html('https://www.labirint.ru/search/'+book+'/?stype=0&available=1')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    labirint_find = soup.findAll('div', class_='products-row')
    for books in labirint_find:
        title = list(books.find('span', class_='product-title'))[0]
        price_labirint = list(books.find('span', class_='price-gray'))[0]
        author = list(books.find('div', class_='product-author').find('span'))[0]
        publisher = list(books.find('div', class_='product-pubhouse').find('span'))[0]
        image = books.find('a', class_='cover').find('img', class_='book-img-cover')
        url_labirint = 'https://www.labirint.ru'+books.find('a', class_='product-title-link')['href']
        save_impressum(author, publisher)
        save_books(title, price_labirint, url_labirint)
        if image:
            image_url = image['data-src']
            image_data = request.urlopen(image_url).read()
            filename = image['title']
            output = open(os.path.join('/home/livsi/projects/book_discount/webapp/static/book_covers', filename), 'wb')
            output.write(image_data)
            output.close()

    html_1 = get_html('https://book24.ru/search/?q='+book+'&available=1')
    soup_1 = bs4.BeautifulSoup(html_1, 'html.parser')
    book24_find = soup_1.findAll('div', class_='catalog-products__content')
    for books in book24_find:
        price_book24 = list(books.find('div', class_='book__price-inner'))[0].split()[0]
        url_book24 = 'https://book24.ru/product'+books.find('a', class_='book__title-link')['href']
        save_books(price_book24, url_book24)


