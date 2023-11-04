import random


def sort_matrix(num):
    """
        Створює та сортує квадратну матрицю розмірності M x M з випадковими
        числами від 1 до 50.

        Сортування матриці виконується за сумами її стовпців у порядку
        зростання. Якщо індекс стовпця
        непарний (починаючи з 1), то елементи в стовпці сортуються за
        зростанням, якщо парний - за спаданням.

        Args:
            num (int): Розмірність квадратної матриці, має бути більше 5.

        Returns:
            tuple: Повертає кортеж, який містить:
                - відсортовану матрицю (list of lists of int)
                - список сум стовпців оригінальної матриці (list of int)
        """

    mx = [
        [random.randint(1, 50) for _ in range(num)] for _ in range(num)
    ]

    print("\nПочаткова матриця:\n")
    print_matrix(mx)

    col_sum = [sum(column) for column in zip(*mx)]

    for i in range(num - 1):
        for j in range(num - 1 - i):
            if col_sum[j] > col_sum[j + 1]:
                col_sum[j], col_sum[j + 1] = col_sum[j + 1], col_sum[j]
                for row in mx:
                    row[j], row[j + 1] = row[j + 1], row[j]

    for j in range(num):
        for i in range(num - 1):
            for k in range(num - 1 - i):
                if ((j + 1) % 2 == 1 and mx[k][j] < mx[k + 1][j]) or (
                        (j + 1) % 2 == 0 and mx[k][j] > mx[k + 1][j]):
                    mx[k][j], mx[k + 1][j] = mx[k + 1][j], mx[k][j]

    return mx, col_sum


def print_matrix(matrix):
    """
        Друкує матрицю і суми її стовпців.

        Args:
            matrix (list of lists of int): Матриця, що має бути виведена.

        Функція нічого не повертає, вона тільки друкує матрицю і суми стовпців.
        """
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
