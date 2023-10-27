# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

total = 0
count = 0
max_number = None
min_number = None
even_count = 0
odd_count = 0

while True:
    user_numbers = int(input("Введіть ціле число (або 0 для завершення): "))

    if user_numbers == 0:
        break

    total += user_numbers
    count += 1
    max_number = user_numbers if max_number is None else max(max_number, user_numbers)
    min_number = user_numbers if min_number is None else min(min_number, user_numbers)

    if user_numbers % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if count > 0:
    average = total / count
    print("Сума чисел:", total)
    print("Середнє арифметичне:", average)
    print("Максимальне значення:", max_number)
    print("Мінімальне значення:", min_number)
    print("Кількість парних чисел:", even_count)
    print("Кількість не парних чисел:", odd_count)
else:
    print("Не було введено жодного числа.")
