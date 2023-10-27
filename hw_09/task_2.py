# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

import random

n = int(input('Введіть розмір матриці: '))

matrix = [
    [random.randint(1, 100) for _ in range(n)] for __ in range(n)
]

for row in matrix:
    print(row)

d_sum = sum(
    matrix[i][i] for i in range(n)
)
print(f'Сума чисел по діагоналі: {d_sum}')

last_col_sum = sum(row[-1] for row in matrix)
print(f'Сума чисел останньої колонки: {last_col_sum}')
