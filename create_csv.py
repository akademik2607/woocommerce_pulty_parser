import csv

#Заменить на 1
new_filename = 258

def create_attr_name(count):
    return f'Название атрибута {count}'


def create_attr_value(count):
    return f'Значения атрибутов {count}'


def create_attr_visible(count):
    return f'Видимость атрибута {count}'


def create_attr_is_global(count):
    return f'Глобальный атрибут {count}'

def create_bulkdiscount_quantity(count):
    return f'Мета: _bulkdiscount_quantity_{count}'

def create_bulkdiscount_discount_fixed(count):
    return f'Мета: _bulkdiscount_discount_fixed_{count}'


def create_csv(data):
    csv_string_dict = {
        'ID': '',
        'Тип': 'simple',
        'Артикул': '',
        'Имя': data['title'],
        'Опубликован': '1',
        'Рекомендуемый?': '0',
        'Видимость в каталоге': 'visible',
        'Краткое описание': data['excerpt_description'],
        'Описание': data['description'],
        'Дата начала действия скидки': '',
        'Дата окончания действия скидки': '',
        'Статус налога': '',
        'Налоговый класс': 'taxable',
        'В наличии?': '1',
        'Запасы': '',
        'Величина малых запасов': '',
        'Возможен ли предзаказ?': '0',
        'Продано индивидуально?': '0',
        'Вес (kg)': '',
        'Длина (cm)': '',
        'Ширина (cm)': '',
        'Высота (cm)': '',
        'Разрешить отзывы от клиентов?': '0',
        'Примечание к покупке': '',
        'Акционная цена': '',
        'Базовая цена': data['price'],
        'Категории': data['category'],
        'Метки': '',
        'Класс доставки': '',
        'Изображения': data['images'],
        'Лимит загрузок': '',
        'Дней срока загрузки': '',
        'Родительский': '',
        'Сгруппированные товары': '',
        'Апсэлы': '',
        'Кросселы': '',
        'Внешний URL': '',
        'Текст кнопки': '',
        'Позиция': '0',
        'Название атрибута 1': 'Производитель',
        'Значения атрибутов 1': data['attributes'].get('Бренд', data['attributes'].get('Производитель')),
        'Видимость атрибута 1': '1',
        'Глобальный атрибут 1': '1',
    }
    if 'Артикул' in data['attributes']:
        del data['attributes']['Артикул']
    if data['attributes'].get('Бренд', None):
        del data['attributes']['Бренд']
    elif data['attributes'].get('Производитель', None):
        del data['attributes']['Производитель']
    del data['excerpt_description']
    count = 2
    for key,val in data['attributes'].items():
        csv_string_dict[create_attr_name(count)] = key
        csv_string_dict[create_attr_value(count)] = val
        csv_string_dict[create_attr_visible(count)] = '1'
        csv_string_dict[create_attr_is_global(count)] = '0'

        count += 1

    print(csv_string_dict)
    csv_string_dict['Мета: _bulkdiscount_text_info'] = ''
    csv_string_dict['Мета: _bulkdiscount_enabled'] = 'yes'
    if data['opts']:
        count = 1
        for opt in data['opts']:
            csv_string_dict[create_bulkdiscount_quantity(count)] = opt[0]
            csv_string_dict[create_bulkdiscount_discount_fixed(count)] = opt[1]

            count += 1

    global new_filename
    with open(f'{new_filename}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = csv_string_dict.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(csv_string_dict)

    new_filename += 1


    # for opt in data['opts']:
    #     print(opt)




# with open('0.csv', newline='', encoding='utf-8') as csvfile:
# with open('wc-product-export-22-2-2023-1677050349145.csv', newline='', encoding='utf-8') as csvfile:
#      reader = csv.DictReader(csvfile)
#      for row in reader:
#          # print(row.keys())
#          # print(row['Описание'])
#          # print(row['Мета: _bulkdiscount_quantity_1'])
#          # print(row['Мета: _bulkdiscount_discount_fixed_1'])
#          for key,val in row.items():
#              print(f'{key}: {val}')
#          break

