import requests
from bs4 import BeautifulSoup as bs

from create_csv import create_csv
from product_page import product_page


def category_page(category_url):
    print(category_url)
    response = requests.get(category_url)
    html = bs(response.text, 'lxml')
    links = html.findAll(name='a', attrs={'class': 'product-image-link'})
    product_links = list(map(lambda i: i.get_attribute_list('href'), links))
    for link in product_links:
        print(link[0])
        page_data = product_page(link[0])
        create_csv(page_data)




    # next = html.find(name='a', attrs={'class': 'next'})
    # if next is None:
    #     return
    # category_page(''.join(next.get_attribute_list('href')))


# category_page('https://profipult.ru/product-category/pulty/')
