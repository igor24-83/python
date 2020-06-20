#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп
lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
lamps_quantity = store[goods['Лампа']][0]['quantity']

table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] + store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
table_quantity = store[goods['Стол']][0]['quantity']+store[goods['Стол']][1]['quantity']

sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] + store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
sofa_quantity = store[goods['Диван']][0]['quantity']+store[goods['Диван']][1]['quantity']

stul_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] + store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price'] + store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
stul_quantity = store[goods['Стул']][0]['quantity']+store[goods['Стул']][1]['quantity']+store[goods['Стул']][2]['quantity']
# или проще (/сложнее ?)
#lamp_code = goods['Лампа']
#lamps_item = store[lamp_code][0]
#lamps_price = lamps_item['price']
#lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, общая стоимость -', lamps_cost, 'руб')
print('Стол -', table_quantity, 'шт, общая стоимость -', table_cost, 'руб')
print('Диван -', sofa_quantity, 'шт, общая стоимость -', sofa_cost, 'руб')
print('Стул -', stul_quantity, 'шт, общая стоимость -', stul_cost, 'руб')
# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб







