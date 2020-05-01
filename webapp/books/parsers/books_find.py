import bs4
import os
from urllib import request

from sqlalchemy.exc import SQLAlchemyError

from webapp.books.models import Impressum, Book, db

from webapp.books.parsers.utils import get_html


def get_search_books(new_book):
	html = get_html('https://www.labirint.ru/search/' + new_book + '/?stype=0&available=1')
	soup = bs4.BeautifulSoup(html, 'html.parser')
	labirint_find = soup.find('div', class_='products-row')
	html_1 = get_html('https://book24.ru/search/?q=' + new_book + '&available=1')
	soup_1 = bs4.BeautifulSoup(html_1, 'html.parser')
	book24_find = soup_1.find('div', class_='catalog-products__content')
	try:
		title = list(labirint_find.find('span', class_='product-title'))[0]
		price_labirint = list(labirint_find.find('span', class_='price-gray'))[0] + ' р.'
		url_labirint = 'https://www.labirint.ru' + labirint_find.find('a', class_='product-title-link')['href']
		author = list(labirint_find.find('div', class_='product-author').find('span'))[0]
		publisher = list(labirint_find.find('div', class_='product-pubhouse').find('span'))[0]

	except AttributeError:
		print('Данная книга не найдена')
		title = 'not found'
		author = 'not found'
		publisher = 'not found'
		price_labirint = 'not found'
		url_labirint = 'not found'

	new_impressum = Impressum(author=author, publisher=publisher)
	try:
		db.session.add(new_impressum)
		db.session.commit()
	except SQLAlchemyError:
		db.session.close()

	impressum = Impressum.query.filter(Impressum.author == author, Impressum.publisher == publisher).first()

	try:
		image = labirint_find.find('a', class_='cover').find('img', class_='book-img-cover')
	except AttributeError:
		image = None

	try:
		url_book24 = 'https://book24.ru' + book24_find.find('a', class_='book__title-link')['href']
	except AttributeError:
		print('Данная книга не найдена')
		url_book24 = 'not found'
	try:
		price_book24 = list(book24_find.find('div', class_='book__price-inner'))[0].split()[0] + ' р.'
	except AttributeError:
		print('Данная книга не найдена')
		price_book24 = 'not found'

	add_book = Book(title=title, price_labirint=price_labirint, url_labirint=url_labirint, url_book24=url_book24,
					price_book24=price_book24, impressum_id=impressum.id, impressum_author=impressum.author,
					impressum_publisher=impressum.publisher)

	book_exists = Book.query.filter(Book.title == title and Book.author == author).count()
	print(book_exists)

	if not book_exists:
		try:
			db.session.add(add_book)
			db.session.commit()
		except SQLAlchemyError:
			db.session.close()

	if image:
		image_url = image['data-src']
		image_data = request.urlopen(image_url).read()
		filename = title
		output = open(os.path.join('../book_discount/webapp/static/book_covers', filename), 'wb')
		output.write(image_data)
		output.close()

	pass
