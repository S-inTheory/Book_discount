import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_book_info_labirint(html):
    print('Лабиринт')
    soup = BeautifulSoup(html, 'html.parser')
    author_find = soup.find('span', itemprop='author')
    title_find = soup.findAll('span', itemprop='name')
    price_find = soup.find('span', itemprop='price')
    for title in title_find[1]:
        print(f'Название: {title}')
    for name in author_find:
        print(f'Автор: {name}')
        break
    for price in price_find:
        price = price.replace('руб', 'р.')
        price = price.replace('Цена: ', '')
        print(f'Цена: {price}')


def get_book_info_ozon(html):
    print('OZON')
    soup = BeautifulSoup(html, 'html.parser')
    title_find = soup.h1.span
    author_find = soup.find('div', class_='b2t3')
    price_find = soup.find('span', class_='b3a9')
    for name in title_find:
        if '|' in name:
            name = name.split('|')
            print(f'Название: {name[0]}')
        else:
            print(name)
    for author in author_find:
        for author_name in author:
            print(f'Автор: {author_name}')
        break
    for price in price_find:
        price = price.strip()
        price = price.replace('₽', 'р.')
        print(f'Цена: {price}')
        break


def get_book_info_book24(html):
    print('Book24')
    soup = BeautifulSoup(html, 'html.parser')
    title_find = soup.find('h1', class_='item-detail__title')
    author_find = soup.find('a', class_='item-tab__chars-link')
    price_find = soup.find('div', class_='item-actions__price')
    for title in title_find:
        print(f'Название: {title}')
    for name in author_find:
        print(f'Автор: {name}')
    for price in price_find:
        price = list(price)
        print(f'Цена: {price[0]} р.')
        break


if __name__ == '__main__':
    html_labirint = get_html('https://www.labirint.ru/books/734321/')
    get_book_info_labirint(html_labirint)

    html_ozon = get_html('https://www.ozon.ru/context/detail/id/165003295/')
    get_book_info_ozon(html_ozon)

    html_book24 = get_html('https://book24.ru/product/tomminokery-5481232/')
    get_book_info_book24(html_book24)
