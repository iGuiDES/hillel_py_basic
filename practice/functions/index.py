# Звісно! Ось для вас 10 завдань по функціям у Python:

# 1. **Базове використання функцій**:
#    Напишіть функцію, яка приймає два числа як аргументи і повертає їх суму.

def sum_of_number(a, b):
    """
    This function returns the sum of params of a and b
    """
    return a + b


print(sum_of_number(1, 2))

# 2. **Функція з умовами**:
#    Напишіть функцію, яка приймає число і повертає "парне", якщо число парне,
#    або "непарне", якщо число непарне.


def is_even(number):
    if number % 2 == 0:
        return 'Це число парне!'
    else:
        return 'Це число непарне!'


# 3. **Рекурсія**:
#    Напишіть рекурсивну функцію для обчислення факторіалу числа.
def factorial(num):
    if num != 0:
        result = 1
        for number in range(1, num + 1):
            result *= number

        return result


print(factorial(5))


# 4. **За замовчуванням**:
#    Створіть функцію, яка приймає число і ступінь, до якого його
#    слід піднести. Ступінь має мати значення за замовчуванням 2.
def eval_num(num, degree=2):
    """This function returns the number of the degree"""

    if num != 0:
        return num ** degree


print(eval_num(10, 3))


# 5. **Аргументи за ключем**:
#    Напишіть функцію, яка приймає ім'я та прізвище як ключові
#    аргументи і повертає повне ім'я.

def get_full_name(name, surname):
    """
        This function returns the full name of a person
    """

    result = ''
    if name != '' and surname != '':
        result = f"{name} {surname}"

    return result


print(get_full_name('Oleksandr', 'Yatsenko'))

# 6. **Lambda функція**:
#    Створіть lambda-функцію, яка приймає два числа і повертає їх добуток.

# 7. **Функція, яка приймає список**:
#    Напишіть функцію, яка приймає список чисел і повертає їх
#    середнє арифметичне.
#
# 8. **Функція з вкладеними функціями**:
#    Створіть функцію, яка обчислює об'єм циліндра. Використовуйте
#    вкладену функцію для обчислення площі основи циліндра.
#
# 9. **Функція, яка повертає функцію**:
#    Напишіть функцію, яка приймає число і повертає функцію, яка
#    підносить будь-яке число до ступеня, заданого першим числом.
#
# 10. **Декоратори**:
#    Створіть декоратор, який логує час виконання функції.
#    Застосуйте цей декоратор до будь-якої функції, яку ви написали раніше.
#
