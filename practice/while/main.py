# Вивести всі непарні числа від 1 до 15.
print(f'{"*" * 20} 1 {"*" * 20}')

counter = 1

while counter <= 15:
    if counter % 2 == 1:
        print(counter)
    counter += 1

# Порахувати суму чисел, доки сума не перевищить 100.
print(f'{"*" * 20} 2 {"*" * 20}')

counter = 0

while True:
    counter += 10
    print(counter)
    if counter == 100:
        break


# Знайти кількість цифр у введеному користувачем числі.
print(f'{"*" * 20} 3 {"*" * 20}')



# Знайти середнє арифметичне чисел введених користувачем, поки користувач не введе 0.
print(f'{"*" * 20} 4 {"*" * 20}')
# Вивести числа від 10 до 1 у зворотному порядку.
print(f'{"*" * 20} 5 {"*" * 20}')
# Знайти суму цифр числа, введеного користувачем.
print(f'{"*" * 20} 6 {"*" * 20}')
# Вивести послідовність чисел Фібоначчі до заданої кількості членів.
print(f'{"*" * 20} 7 {"*" * 20}')
# Обчислити кількість цифр "7" в заданому діапазоні чисел.
print(f'{"*" * 20} 8 {"*" * 20}')

print("*" * 20, "Continue", "*" * 20)

counter = 0

while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    else:
        print(counter)