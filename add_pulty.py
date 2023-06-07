import requests
from bs4 import BeautifulSoup as bs

from create_csv import create_csv
from product_page import product_page


urls = ['https://profipult.ru/product/nero-radio-8101-2m/',
        'https://profipult.ru/product/nero-radio-8101-4m/',
        'https://profipult.ru/product/pult-intro-ii-8501-1m/',
        'https://profipult.ru/product/nero-intro-ii-8501-2m/',
        'https://profipult.ru/product/nero-intro-ii-8501-4m/',
        'https://profipult.ru/product/bft-mitto-2-1-rev/',
        'https://profipult.ru/product/bft-mitto-4-ustarevshaya-model/',
        'https://profipult.ru/product/marantec-302-433-mhz/',
        'https://profipult.ru/product/marantec-304-433-mhz/',
        'https://profipult.ru/product/pult-faac-xt4-433-rc/',
        'https://profipult.ru/product/marantec-313-433-mhz/'
    ]
page_data = product_page('https://profipult.ru/product/marantec-313-433-mhz/')
create_csv(page_data)

# for url in urls:
#     page_data = product_page(url)
#     create_csv(page_data)
