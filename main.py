import requests
from bs4 import BeautifulSoup as bs
from category_page import category_page

if __name__ == '__main__':
    response = requests.get('https://profipult.ru/')
    site = bs(response.text, 'lxml')
    category_links = site.find(attrs={'id': 'menu-katalog'})
    category_links = category_links.find_all(name='a')
    category_links = list(map(lambda i: i.get_attribute_list('href'), category_links))

    category_links = category_links[2:3]
    #--------------------------------------------------
    for link in category_links:
        category_page(''.join(link))

    print('Готово!')



