import random


def bubble_sort_decorator(func):
    def wrapper(m_lst):

        lm = len(m_lst)
        for i in range(lm - 1):
            for j in range(0, lm - i - 1):
                if sum(m_lst[j]) > sum(m_lst[j + 1]):
                    for k in range(lm):
                        m_lst[k][j], m_lst[k][j + 1] = (
                            m_lst[k][j + 1], m_lst[k][j])

        func(m_lst)
    return wrapper


@bubble_sort_decorator
def sort_matrix(m_lst):
    lm = len(m_lst)

    for col in range(lm):
        for i in range(lm - 1):
            for j in range(0, lm - i - 1):
                if (col % 2 == 0 and m_lst[j][col] > m_lst[j + 1][col]) or \
                   (col % 2 != 0 and m_lst[j][col] < m_lst[j + 1][col]):
                    m_lst[j][col], m_lst[j + 1][col] = (
                        m_lst[j + 1][col], m_lst[j][col])


def print_matrix(m_lst):
    lm = len(m_lst)

    for row in m_lst:
        for item in row:
            print(f"{item:3}", end=" ")
        print()

    for col in range(lm):
        print(f"{sum(m_lst[row][col] for row in range(lm)):3}", end=" ")
    print()


M = int(input("Введіть розмір матриці (ціле число більше 5): "))
while M <= 5:
    M = int(input("Помилка. Введіть ціле число більше 5: "))

matrix = [
    [random.randint(1, 50)
        for _ in range(M)
     ] for _ in range(M)
]

print(f"\n\n{'*' * M} Початкова матриця: {'*' * M}\n")
print_matrix(matrix)

sort_matrix(matrix)

print(f"\n\n{'*' * M} Відсортована матриця: {'*' * M}\n")
print_matrix(matrix)
