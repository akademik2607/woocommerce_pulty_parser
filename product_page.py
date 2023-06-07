from selenium import webdriver
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup as bs
import re


def get_images(product_url):
    driver = webdriver.Chrome()
    driver.get(product_url)
    elem = driver.find_elements(By.CSS_SELECTOR, '.woocommerce-product-gallery__image img')
    images = list(map(lambda i: i.get_attribute('src'), elem))
    # images = f'"{images}"'
    images = ', '.join(list(map(lambda i: re.search(r'(.*?php\?src=)(.*?)(&nocache=)', i).group(2), images))[1:])

    driver.close()
    return images

def get_description(html):
    description_list = list(html.find(attrs={'class': 'wprt-container'}).children)
    description_list = list(map(lambda i: str(i), description_list))
    description = ' '.join(description_list)
    return description


def get_attributes(html):
    attr_names = list(map(lambda i: i.text, html.findAll(attrs={'class': 'woocommerce-product-attributes-item__label'})))
    attr_vals = list(map(lambda i: i.text, html.findAll(attrs={'class': 'woocommerce-product-attributes-item__value'})))
    attrs = dict(zip(attr_names, attr_vals))
    return attrs


def get_title(html):
    title = html.findAll(name='h1')
    return title[0].text


def get_price(html):
    html = html.find(attrs={'class': 'summary-inner'})
    price = html.find(attrs={'class': 'price'})
    price = price.text.strip()
    price = price.strip(' руб.').replace(' ', '')
    return price


def get_category(html):
    def get_category_title(url):
        html = requests.get(url)
        html = bs(html.text, 'lxml')
        title = html.find(name='h1').text
        return title

    category_links = html.find(attrs={'class': 'posted_in'})
    links = category_links.findAll(name='a')

    categories_href = list(map(lambda i: i.attrs['href'].split(r'/'), links))
    base_category_path = categories_href[0][0:4]
    category_names = []
    for cat_href in categories_href:
        dynamic_path_list = cat_href[4:-1]
        dynamic_path_url = '/'.join(base_category_path)
        category_titles = ''
        for i, item in enumerate(dynamic_path_list):
            dynamic_path_url += '/' + item
            if i != 0:
                category_titles += ' > '
            category_titles += get_category_title(dynamic_path_url)
        category_names.append(category_titles)
    category_names = ', '.join(category_names)
    return category_names


def get_opt(html, price):
    summary_inner = html.find(attrs={'class': 'summary-inner'})
    opt = summary_inner.find(attrs={'class': 'opt'})
    if opt:
        results = re.findall(r'(От )(\d*)', opt.text)
        counts = []
        for result in results:
            counts.append(result[1])
        results = re.findall(r'(- )(\d*)', opt.text)
        prices = []
        for result in results:
            prices.append(result[1])
        # print(price)
        # print(prices)
        price_int = int(price)
        prices = list(map(lambda i: str(price_int - int(i.replace(' ', ''))), prices))
        # print(prices)
        return list(dict(zip(counts, prices)).items())
    return None


def min_description(html):
    summary_inner = html.find(attrs={'class': 'summary-inner'})
    opt = summary_inner.find(attrs={'class': 'opt'})
    # print(dir(opt))
    if opt:
        opt = opt.text.replace('От', '<h4><strong>От')
        opt = opt.replace('- ', '- <span style="color: #3699d1;">')
        opt = opt.replace('руб.', '₽</span></strong></h4>')
        return opt
    return ''


def product_page(product_url):
    images = get_images(product_url)

    response = requests.get(product_url)
    html = bs(response.text, 'lxml')
    min_description(html)
    categories = get_category(html)
    price = get_price(html)
    description = get_description(html)
    attributes = get_attributes(html)
    title = get_title(html)
    opts = get_opt(html, price)
    excerpt_description = min_description(html)
    return {
        'images': images,
        'description': description,
        'attributes': attributes,
        'title': title,
        'price': price,
        'category': categories,
        'opts': opts,
        'excerpt_description': excerpt_description,
    }


# product_page('https://profipult.ru/product/nice-flo-2/')
# product_page('https://profipult.ru/product/came-gard-2500-combo-classico-komplekt-shlagbauma/')
