print("*" * 15, "1", "*" * 15)
# Вивести всі парні числа від 1 до 20.

for item in range(1, 20 + 1):
    if item % 2 == 0:
        print(item)

print("*" * 15, "2", "*" * 15)
# Обчислити суму всіх чисел в заданому списку.

numbers_list = [1, 23, 324, 45, 5, 61, 17, -8, 1993, 0]

sum_number = 0

for item in numbers_list:
    if isinstance(item, int):
        sum_number += item

print("Сума елементів у списку:", sum_number)

print("*" * 15, "3", "*" * 15)
# Знайти найбільший елемент в списку.

max_element = numbers_list[0]

for item in numbers_list:
    if item > max_element:
        max_element = item

print("Найбільший елемент у списку:", max_element)

print("*" * 15, "4", "*" * 15)
# Обчислити факторіал числа, яке вводить користувач.

user_number = int(input('Введіть ціле число: '))
factorial = 1

for item in range(1, user_number + 1):
    factorial *= item

print('Факторіал числа', user_number, 'дорівнює,', factorial)

print("*" * 15, "5", "*" * 15)
# Вивести всі букви у рядку і їх позиції.

user_str = input('Введіть будь яку фразу: ')

for item, char in enumerate(user_str):
    print('Символ', char, 'знаходиться на позиції', item)

print("*" * 15, "6", "*" * 15)
# Створити список, який містить квадрати чисел від 1 до 10.

square_numbers = []

for item in range(1, 10 + 1):
    square_numbers.append(item ** 2)

print(square_numbers)

print("*" * 15, "7", "*" * 15)
# Знайти всі прості числа в заданому діапазоні.

start = int(input('Введіть стартове число: '))
end = int(input('Введіть кінцеве число: '))

prime_numbers = []

for item in range(start, end + 1):
    if item > 1:
        is_prime = True
        for i in range(2, int(item ** 0.5) + 1):
            if item % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(item)

print('Прості числа у діапазоні від', start, "до", end, ':', prime_numbers)
