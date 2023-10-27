# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

N = int(input("Введіть число N: "))

numbers = []

for i in range(1, N + 1):
    square = i ** 2

    if str(square)[-len(str(i)):] == str(i):
        numbers.append(i)

if numbers:
    print("Антропоморфні числа, які не перевищують", N, ":", numbers)
