import random


def sort_matrix(M):
    mx = [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]

    print("\nПочаткова матриця:\n")
    print_matrix(mx)

    col_sum = [sum(column) for column in zip(*mx)]

    for i in range(M - 1):
        for j in range(M - 1 - i):
            if col_sum[j] > col_sum[j + 1]:
                col_sum[j], col_sum[j + 1] = col_sum[j + 1], col_sum[j]
                for row in mx:
                    row[j], row[j + 1] = row[j + 1], row[j]

    for j in range(M):
        for i in range(M - 1):
            for k in range(M - 1 - i):
                if ((j + 1) % 2 == 1 and mx[k][j] < mx[k + 1][j]) or (
                        (j + 1) % 2 == 0 and mx[k][j] > mx[k + 1][j]):
                    mx[k][j], mx[k + 1][j] = mx[k + 1][j], mx[k][j]

    return mx, col_sum


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:4}", end="")
        print()
    print("\nSUM")
    col_sum = [sum(column) for column in zip(*matrix)]
    for sum_value in col_sum:
        print(f"{sum_value:4}", end="")
    print("\n")


if __name__ == '__main__':
    M = int(
        input("Введіть розмір матриці M (ціле, позитивним число більше 5): "))
    while M <= 5:
        M = int(
            input("Розмір матриці має бути більшим за 5, спробуйте знову: "))

    sorted_matrix, column_sums = sort_matrix(M)

    print("\nВідсортована матриця:\n")

    print_matrix(sorted_matrix)
