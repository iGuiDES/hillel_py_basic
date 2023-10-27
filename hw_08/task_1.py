# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

lst = [8, 1, 2, 8, 3, 4, 8, 5, 5, 6, 65, 6, 12, 11, 80]

print('Загальна кількість елементів у списку:', len(lst))

elements_count = {}

for number in lst:
    if number in elements_count:
        elements_count[number] += 1
    else:
        elements_count[number] = 1

print("Кількість різних чисел у списку:", len(elements_count))
