data = [
    {"name": "Alisa", "country": "UA", "item": "socks", "price": 15},
    {"name": "Alisa", "country": "UA", "item": "socks", "price": 25},
    {"name": "Ben", "country": "US", "item": "pencil", "price": 95},
    {"name": "Alisa", "country": "UA", "item": "pencil", "price": 45},
    {"name": "Oleg", "country": "GB", "item": "socks", "price": 100},
    {"name": "Ben", "country": "US", "item": "pencil", "price": 10}
]

workers_set = {item['name'] for item in data}
print(workers_set)

profits_dict = {}

for profit in data:
    worker = profit['name']
    profits = profit['price']

    if worker in profits_dict:
        profits_dict[worker] += profits
    else:
        profits_dict[worker] = profits

print(profits_dict)
