# user_count_hobby = int(input('Яка у Вас кількісь хобі? '))
#
# i = 1
# hobbies = []
#
# while i <= user_count_hobby:
#     hobbies.append(input(f"Назва {i} хобі? "))
#     i += 1
#
# print(hobbies)


my_list = [1, 2, 3, 4, 'Python', True]

print(my_list[4])

lst_empty = list('hello, python!')
print(lst_empty)

regions = [
    'АР Крим', 'Вінницька', 'Волинська', 'Дніпропетровська', 'Донецька',
    'Житомирська', 'Закарпатська', 'Запорізька', 'Іванно-Франківська',
    'Київська', 'Кіровоградська', 'Луганська', 'Львівська', 'Миколаївська',
    'Одеська', 'Полтавська', 'Рівненська', 'Сумська', 'Тернопільська',
    'Харківська', 'Херсонська', 'Хмельницька', 'Черкаська', 'Чернівецька',
    'Чернігівська'
]

for region in regions:
    print(region)

