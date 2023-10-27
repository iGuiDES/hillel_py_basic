import random


def create_2d_list(rows=15, cols=8):
    return [
        [
            random.randint(0, 200)
            for _ in range(cols)
        ]
        for _ in range(rows)
    ]


def print_table(matrix):
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
