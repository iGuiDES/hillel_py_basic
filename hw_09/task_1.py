# pylint: disable=missing-module-docstring

import random

int_elements = [random.randint(1, 500) for _ in range(25)]

print("Список int_elements:", int_elements)

squares = [x**2 for x in int_elements]
print("Список квадратів:", squares)

remainders_11 = [x % 11 for x in int_elements]
print("Список залишку ділення на 11:", remainders_11)

even_elements = [x for x in int_elements if x % 2 == 0]
print("Список парних елементів:", even_elements)

odd_digits_elements = [x for x in int_elements if len(str(x)) % 2 != 0]
print("Список елементів із непарною кількістю цифр:", odd_digits_elements)

not_multiple_of_3 = [x for i, x in enumerate(int_elements) if (i+1) % 3 != 0]
print("Список елементів на позиціях, які не кратні 3:", not_multiple_of_3)
