# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

N = int(input("Введіть число N: "))

for i in range(1, N + 1):
    square = i ** 2

    if square <= N:
        print(square)
