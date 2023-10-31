numbers = [n * n for n in range(1, 11) if n % 2 == 0]

print(numbers)

len_in_centimeter = [12, 10, 54, 124, 64]

len_in_inches = [(round(cm / 2.54, 2)) for cm in len_in_centimeter]
print(len_in_inches)

ratings = [2485, 2580, 2480, 2600, 2482, 2520]

titles = ["CM" if item >= 2500 else "MM" for item in ratings]
print(titles)


list_1 = [2, 4, -5, 6, -2]
list_2 = [2, -6, 8, 3, 5, -2]

# Знайти пари, сума яких дорівнює 0

def find_pairs_one(lst_1, lst_2):
    """
        Знаходить пари елементів із двох списків, такі, що сума пари
        дорівнює нулю.

        Параметри:
        lst_1 (list): Перший список елементів.
        lst_2 (list): Другий список елементів.

        Повертає:
        list: Список кортежів, які містять пари елементів, сума яких
        дорівнює нулю.

        Приклад використання:
        >>> list_1 = [1, 2, 3, -2, -1]
        >>> list_2 = [4, -3, 2, 0, -2]
        >>> result = find_pairs_one(list_1, list_2)
        >>> print(result)
        [(2, -2), (-2, 2)]
    """

    pairs = []

    for x in lst_1:
        for y in lst_2:
            current_sum = x + y
            if current_sum == 0:
                pairs.append((x, y))

    return pairs

result = find_pairs_one(list_1, list_2)
print(f'Print result use standard cycle {result}')


def find_pairs_two(lst_1, lst_2):
    """
        Знаходить пари елементів із двох списків, такі, що сума пари
        дорівнює нулю.

        Параметри:
        lst_1 (list): Перший список елементів.
        lst_2 (list): Другий список елементів.

        Повертає:
        list: Список кортежів, які містять пари елементів, сума яких
        дорівнює нулю.

        Приклад використання:
        >>> list_1 = [1, 2, 3, -2, -1]
        >>> list_2 = [4, -3, 2, 0, -2]
        >>> result = find_pairs_two(list_1, list_2)
        >>> print(result)
        [(2, -2), (-2, 2)]
    """

    pairs = [
        (x, y) for x in lst_1 for y in lst_2
        if x + y == 0
    ]

    return pairs

result_two = find_pairs_two(list_1, list_2)
print(f'Result with use list comprehension {result_two}')

