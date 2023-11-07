file_path = 'article.txt'


def longest_words(file):
    """
    Знаходить та виводить слово або слова з максимальною довжиною
    у текстовому файлі.

    Параметри:
        file_path (str): Шлях до текстового файлу для аналізу.

    Повертає:
        list: Список, що містить найбільші за довжиною слова.
    """

    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
        max_length = len(max(words, key=len))
        l_words = [word for word in words if len(word) == max_length]

    print(f"В файлі ми маємо такі найдовші слова як: {l_words}")
    return l_words


longest_words(file_path)
