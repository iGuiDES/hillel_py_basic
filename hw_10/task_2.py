import random


def create_2d_list(rows=15, cols=8):
    """
        Ця функція створює двовимірний список (матрицю) розміру rows x cols
        із випадковими числами від 0 до 200.

        Параметри rows та cols мають значення за замовчуванням, відповідно,
        15 та 8.
        Використовуючи спискову інтеграцію, для кожного рядка (rows) ми
        створюємо список довжиною cols з випадковими числами.
    """

    return [
        [
            random.randint(0, 200)
            for _ in range(cols)
        ]
        for _ in range(rows)
    ]


def print_table(matrix):
    """
        Функція приймає на вхід двовимірний список (матрицю) і виводить
        його у вигляді таблиці.

        Спочатку перевіряється, чи матриця не порожня.
        Для форматування виводу визначається максимальна ширина кожного
        стовпця за допомогою спискової інтеграції та функції zip.
        Матриця виводиться у вигляді таблиці з вирівнюванням по правому краю.

    """

    if not matrix:
        return

    col_widths = [
        max(len(str(num))
            for num in col
            )
        for col in zip(*matrix)
    ]

    for row in matrix:
        print(
            "  ".join(
                f"{num:>{width}}"
                for num, width in zip(row, col_widths)
            )
        )


print("Без параметрів:")
matrix1 = create_2d_list()
print_table(matrix1)

print("\n\nЗ одним параметром:")
matrix2 = create_2d_list(8)
print_table(matrix2)

print("\n\nЗ двома параметрами:")
matrix3 = create_2d_list(7, 4)
print_table(matrix3)
