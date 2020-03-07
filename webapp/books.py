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

def get_book_info(shop, html):
    shop = str(shop)
    shop = shop.lower()
    if shop == 'labirint':
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

    elif shop == 'book24':
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
    else:
        return 'Этот магазин пока не поддерживается'


if __name__ == '__main__':
    html = get_html('https://www.ozon.ru/context/detail/id/167179971/')
    get_book_info('ozon', html)
