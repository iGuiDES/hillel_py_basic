N = int(input("Введіть число N: "))

square = 0

while square <= N:
    square = square + 1
    square_value = square * square

    if square_value > N:
        print(square_value, end=' ')
