def calculator(num_1, num_2, separator="+"):

    """
        Ця функція виконує роль калькулятора
        Вона приймає 3 параметри:
        - перший параметр - ціле число
        - другий параметр - ціле число
        - третій параметр - знак калькуляції (за замовчуванням має знак "+"

        Завдання функції розрахувати результат відповідно прийнятих
        параметрів
    """

    if separator == '+':
        return num_1 + num_2

    elif separator == '-':
        return num_1 - num_2

    elif separator == "*":
        return num_1 * num_2

    elif separator == "/":
        return num_1 / num_2

    elif separator == '%':
        return num_1 % num_2

    else:
        return 0


print(calculator(10, 2))
print(calculator(100, 10, '/'))
print(calculator(100, 10, '*'))
print(calculator(100, 10, '-'))
print(calculator(100, 10, '+'))
print(calculator(100, 9, '%'))
