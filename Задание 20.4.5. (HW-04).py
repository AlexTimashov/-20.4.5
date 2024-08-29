import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

# Какой номер самого дорого заказа за июль?
max_price = 0
max_order = None
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}. Стоимость заказа: {max_price}')

# Какой номер заказа с самым большим количеством товаров?
max_quantity = 0
max_order = None
for order_num, order_data in orders.items():
    if order_data['quantity'] > max_quantity:
        max_quantity = order_data['quantity']
        max_order = order_num
print(f'Номер заказа с самым большим количеством товаров: {max_order}. Количество товаров в заказе: {max_quantity}')

# В какой день в июле было сделано больше всего заказов?
busiest_day = None
max_orders = 0
orders_count = {}

for order_info in orders.values():
    date_parts = order_info['date'].split('-')
    day = date_parts[1]

    if day in orders_count:
        orders_count[day] += 1
    else:
        orders_count[day] = 1

    if orders_count[day] > max_orders:
        max_orders = orders_count[day]
        busiest_day = day

print(f'Больше всего заказов было сделано {busiest_day} июля. Количество заказов составило: {max_orders}')

# Какой пользователь сделал самое большое количество заказов за июль?
user_orders_count = {}

for order_info in orders.values():
    user_id = order_info['user_id']

    if user_id in user_orders_count:
        user_orders_count[user_id] += 1
    else:
        user_orders_count[user_id] = 1

max_quantity = 0
top_user = None
for user_id, count in user_orders_count.items():
    if count > max_quantity:
        max_quantity = count
        top_user = user_id

print(f'Пользователь с ID: {top_user}, сделал больше всего заказов. Количество заказов составило: {max_orders}')

# У какого пользователя самая большая суммарная стоимость заказов за июль?
user_order_values = {}

for order_info in orders.values():
    user_id = order_info['user_id']
    order_value = float(order_info['price'])

    if user_id in user_order_values:
        user_order_values[user_id] += order_value
    else:
        user_order_values[user_id] = order_value

max_value = 0
top_user = None
for user_id, total_value in user_order_values.items():
    if total_value > max_value:
        max_value = total_value
        top_user = user_id

print(f'У пользователя с ID: {top_user}, самая большая суммарная стоимость заказов. Стоимость заказов составляет: {max_value}')

# Какая средняя стоимость заказа была в июле?
total_value = 0
order_count = 0

for order_info in orders.values():
    order_value = float(order_info['price'])
    total_value += order_value
    order_count += 1

if order_count > 0:
    average_value = total_value / order_count
else:
    average_value = 0

print(f'Cредняя стоимость заказа составляет: {average_value}')

# Какая средняя стоимость товаров в июле?
total_value = 0
total_quantity = 0

for order_info in orders.values():
    total_value += float(order_info['price'])
    total_quantity += int(order_info['quantity'])

if total_quantity > 0:
    average_price = round(total_value / total_quantity,2)
else:
    average_price = 0

print(f'Cредняя стоимость товаров оставляет: {average_price}')
