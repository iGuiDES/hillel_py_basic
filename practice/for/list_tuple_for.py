persons = [
	('John', 20),
	('Bob', 32),
	('Dave', 40)
]

players = dict(
	Carlsen=2843,
	Caruana=2822,
	John=2190
)

list_1 = [2, 4, -5, 6, 8, -2]
list_2 = [2, -6, 8, 3, 5, -2]


def create_user(tuple):
    """
    Виводить інформацію про користувачів на основі 
    переданого кортежу.

    Параметри:
    - tuple (tuple[tuple[str, int]]): Кортеж кортежів, де перший 
    елемент - ім'я користувача, а другий - його вік.

    Не повертає значень. Виводить результат на екран.

    Приклад:
    >>> create_user((("John", 25), ("Alice", 30)))
    My name is John. I am 25 years old!
    My name is Alice. I am 30 years old!
    """

    for (name, age) in tuple:
        print(f"My name is {name}. I am {age} years old!")

        
        
def players_rating(dict):
    """
    Виводить рейтинг гравців на основі переданого словника.

    Параметри:
    - dict (dict[str, int or float]): Словник, де ключ - ім'я 
    гравця, а значення - його рейтинг.

    Не повертає значень. Виводить результат на екран.

    Приклад:
    >>> players_rating({"John": 1500, "Alice": 1550})
    Player John, have rating 1500
    Player Alice, have rating 1550
    """

    for key, value in dict.items():
        print(f'Player {key}, have rating {value}')

    
    
def find_sum_which_equals(list_1, list_2):
    """
    Знаходить пари чисел з двох списків, сума яких дорівнює нулю.

    Параметри:
    - list_1 (list[int or float]): Перший список чисел.
    - list_2 (list[int or float]): Другий список чисел.

    Повертає:
    - list[tuple[int or float, int or float]]: Список пар чисел, 
    де перше число з list_1, а друге з list_2, і їх сума дорівнює нулю.

    Приклад:
    >>> find_sum_which_equals([1, 2, -3], [3, -1, 4])
    [(1, -1), (-3, 3)]
    """

    pairs = []
    
    for i in list_1:
        for j in list_2:
            current_sum = i + j
            if current_sum == 0:
                pairs.append((i, j))
                
    return pairs

    
create_user(persons)
players_rating(players)
result = find_sum_which_equals(list_1, list_2)
print(result)

