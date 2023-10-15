N = int(input("Введіть число N: "))

for i in range(N + 1):
    square = i ** 2

    if square <= N:
        print(square)
