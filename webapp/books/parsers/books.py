from urllib import request, error
from bs4 import BeautifulSoup
import os


def get_html(url):
    try:
        html_1 = request.urlopen(url)
        return html_1
    except (error.URLError, ValueError):
        print('Сетевая ошибка')
        return False


def get_book_info(shop, html_1):
    shop = str(shop).lower()
    if shop == 'labirint':
        print('Лабиринт')
        soup = BeautifulSoup(html_1, 'html.parser')
        author_find = soup.find('span', itemprop='author')
        publisher_find = soup.find('div', class_='publisher').find('a')
        title_find = soup.findAll('span', itemprop='name')
        price_find = soup.find('span', itemprop='price')
        for publisher in publisher_find:
            print(publisher)
        image_find = soup.find('div', id='product-image').find('img', class_='book-img-cover')
        for title in title_find[1]:
            print(f'Название: {title}')
        for name in author_find:
            print(f'Автор: {name}')
            break
        for price in price_find:
            price = price.replace('руб', 'р.')
            price = price.replace('Цена: ', '')
            print(f'Цена: {price}')
        if image_find:
            image_url = image_find['data-src']
            image_data = request.urlopen(image_url).read()
            filename = image_find['title']
            output = open(os.path.join('/home/livsi/projects/book_discount/webapp/static/book_covers', filename), 'wb')
            output.write(image_data)
            output.close()
    elif shop == 'book24':
        print('Book24')
        soup = BeautifulSoup(html_1, 'html.parser')
        title_find = soup.find('h1', class_='item-detail__title')
        author_find = soup.find('a', class_='item-tab__chars-link')
        publisher_find = soup.findAll('a', class_='item-tab__chars-link')
        price_find = soup.find('div', class_='item-actions__price')
        image_find = soup.find('img', class_='item-cover__image')
        for title in title_find:
            print(f'Название: {title}')
        for name in author_find:
            print(f'Автор: {name}')
        for publisher in publisher_find:
            publisher_list = list(publisher_find[3])
            publisher = publisher_list[0].strip().split()
        print(publisher[1])
        for price in price_find:
            price = list(price)
            print(f'Цена: {price[0]} р.')
            break
        if image_find:
            image_url = image_find['src']
            image_data = request.urlopen(image_url).read()
            filename = image_find['title']
            output = open(os.path.join('/home/livsi/projects/book_discount/webapp/static/book_covers', filename), 'wb')
            output.write(image_data)
            output.close()

    else:
        return 'Этот магазин пока не поддерживается'


if __name__ == '__main__':
    html_1 = get_html('https://book24.ru/product/tomminokery-5481232/')
    get_book_info('book24', html_1)
