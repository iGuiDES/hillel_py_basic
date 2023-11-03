# Звісно! Ось для вас 10 завдань на тему циклів у Python:
#
# 1. **Сума чисел**:
#    Напишіть програму, яка зчитує числа від користувача, поки він не введе
#    "stop". Після цього виведіть суму всіх введених чисел
print(f"\n\n{'*' * 20} Task 1 {'*' * 20}")

result = 0

while True:
    user_number = input('Уведіть ціле число: ')
    if user_number is int and user_number != 'stop':
        result += user_number
    else:
        break

# 2. **Таблиця множення**:
#    Напишіть програму, що виводить таблицю множення для числа введеного
#    користувачем.
print(f"\n\n{'*' * 20} Task 2 {'*' * 20}")

user_number = int(input('Уведіть своє число: '))

if 'str' != type(user_number) and user_number > 0:
    result = []
    for number in range(1, user_number + 1):
        result.append(number * user_number)
    print(result)

# 3. **Пошук простих чисел**:
#    Напишіть програму, яка знаходить всі прості числа в діапазоні
#    від 2 до n, де n вводить користувач.
print(f"\n\n{'*' * 20} Task 3 {'*' * 20}")

user_number_for_find = int(input('Уведіть ціле число: '))

prime_numbers = []

for num in range(2, user_number_for_find + 1):
    if num <= 3:
        continue
    if num % 2 == 0 or num % 3 == 0:
        continue

    next_number = 5
    is_prime = True

    while next_number * next_number <= num:
        if num % next_number == 0 or num % (next_number + 2) == 0:
            is_prime = False
            break
        next_number += 6

    if is_prime:
        prime_numbers.append(num)

print(prime_numbers)


# 4. **Факторіал числа**:
#    Запитайте у користувача число `n` і обчисліть його факторіал
#    за допомогою циклу.
print(f"\n\n{'*' * 20} Task 4 {'*' * 20}")

n = int(input('Уведіть ціле число:'))
nums_factorial = []

for number in range(1, n + 1):
    nums_factorial.append(number * number)

print(nums_factorial)

# 5. **Зворотній порядок**:
#    Напишіть програму, яка зчитує послідовність чисел від користувача
#    та виводить їх у зворотньому порядку.
print(f"\n\n{'*' * 20} Task 5 {'*' * 20}")

n_reverse = int(input('Уведіть числа через пробіл: '))

user_numbers_list = [n_reverse]

reverse_numbers_list = [i for i in user_numbers_list[::-1]]
print(reverse_numbers_list)

# 6. **Сума парних чисел**:
#    Напишіть програму, яка зчитує `n` чисел і обчислює суму парних чисел
#    серед них.
print(f"\n\n{'*' * 20} Task 6 {'*' * 20}")

# 7. **Виведення зірочок**:
#    Запитайте у користувача число `n` і виведіть на екран рівнобедрений
#    трикутник зі зірочок висотою `n`.
print(f"\n\n{'*' * 20} Task 7 {'*' * 20}")

# 8. **Найбільший спільний дільник**:
#    Напишіть програму, яка знаходить найбільший спільний дільник двох
#    чисел за допомогою циклу.
print(f"\n\n{'*' * 20} Task 8 {'*' * 20}")

# 9. **Числа Фібоначчі**:
#    Напишіть програму, яка виводить перші `n` чисел Фібоначчі, де `n`
#    вводить користувач.
print(f"\n\n{'*' * 20} Task 9 {'*' * 20}")

# 10. **Перевірка на паліндром**:
#     Напишіть програму, яка перевіряє, чи є введене користувачем слово
#     або фраза паліндромом (однаково читається в обох напрямках).
print(f"\n\n{'*' * 20} Task 10 {'*' * 20}")

a = [x + y for x in range(5) for y in range(5)]

a_two = []

for x in range(5):
    for y in range(5):
        a_two.append(x + y)

print(a)
