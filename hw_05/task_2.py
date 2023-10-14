N = int(input("Введіть число N: "))

numbers = []

for i in range(1, N + 1):
    squared = i ** 2
    last_number = i % 10
    last_squared = squared % 10
    if last_number == last_squared:
        numbers.append(i)

if numbers:
    print("Антропоморфні числа, які не перевищують", N, ":")
    print(numbers)
else:
    print("Немає антропоморфних чисел, які не перевищують", N)
