from selenium import webdriver
from selenium.webdriver.common.by import By



# driver = webdriver.Chrome()
# driver.get('https://profipult.ru/product-category/pulty/page/2')
# elem = driver.find_element(By.CSS_SELECTOR, '.next')

# print(elem)

# elem.click()
# elem = driver.find_element(By.CSS_SELECTOR, '.next')
# print(elem)


import csv


# with open(f'result.csv', newline='', encoding='utf-8') as csvfile_r:
#     reader = csv.DictReader(csvfile_r)
#     for i, row in enumerate(reader):
#         if i == 1:
#             data = row
#             break

# for i in range(1, 247):
#
#     with open(f'{i}.csv', newline='', encoding='utf-8') as csvfile_r:
#         csvfile_r.readline()
#
#
# for key,val in data.items():
#     print(f'{key}: {val}')


#Редактируем файлы
# for i in range(1, 247):
#     with open(f'{i}.csv', 'rt', encoding='utf-8') as csvfile_r:
#         x = csvfile_r.read()
#
#     with open(f'{i}.csv', 'wt', encoding='utf-8') as csvfile_r:
#         x = x.replace('Значение атрибутов', 'Значения атрибутов')
#         csvfile_r.write(x)


# for i in range(1, 247):
#     with open(f'{i}.csv', 'rt', encoding='utf-8') as csvfile_r:
#         x = csvfile_r.read()
#         if 'Пульт Came TTS44FKS' in x:
#             print(i)
#             break




# for i in range(1, 247):
#     with open(f'{i}.csv', newline='', encoding='utf-8') as csvfile_r:
#         reader = csv.DictReader(csvfile_r)
#         for row in reader:
#             print(row['Краткое описание'])
#             print(row.get('Мета: _bulkdiscount_quantity_1'))




# for i in range(1, 247):
#     with open(f'{i}.csv', newline='', encoding='utf-8') as csvfile_r:
#         reader = csv.DictReader(csvfile_r)
#         for row in reader:
#             data = row
#             if row.get('Мета: _bulkdiscount_quantity_1') is None:
#                 data['Краткое описание'] = ''
#             else:
#                 data['Краткое описание'] = row['Краткое описание']
#
#     with open(f'{i}.csv', 'w', newline='', encoding='utf-8') as csvfile_w:
#         fieldnames = data.keys()
#         writer = csv.DictWriter(csvfile_w, fieldnames=fieldnames)
#
#         writer.writeheader()
#         writer.writerow(data)


