def my_func(num_1, symbol, num_2):
    if symbol == '+':
        return num_1 + num_2
    elif symbol == '-':
        return num_1 - num_2
    elif symbol == '/':
        return num_1 / num_2
    elif symbol == '//':
        return num_1 // num_2
    elif symbol == '%':
        return num_1 % num_2

result = my_func(10, "+", 2)
print(result)