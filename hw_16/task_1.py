import argparse


def parse_word():

    """
        Парсить аргументи командного рядка.

        Використовує argparse для встановлення і парсингу аргументів
        командного рядка.
        Повертає об'єкт із зібраними аргументами.

        Returns:
            Об'єкт argparse.
    """

    parser = argparse.ArgumentParser(
        description="Знайти найдовше слова у файлі",
        epilog="The program was developed by Oleksandr Yatsenko",
        prog="words_longest_find"
    )

    parser.add_argument(
        '-f', '--file',
        required=True,
        type=str,
        help="Шлях до даного файлу, у якому треба знайти слова (слова)"
    )

    return parser.parse_args()


def searching_longest_word(file):
    """
        Знаходить найдовші слова у заданому файлі.

        Відкриває файл, читає його вміст, розділяє на слова і знаходить
        слова з максимальною довжиною.

        Args:
            file (str): Шлях до файлу для аналізу.

        Returns:
            list: Список найдовших слів у файлі.
    """

    with open(file, 'r', encoding='utf-8') as file:
        words = file.read().split()
        max_length = len(max(words, key=len))
        l_words = [word for word in words if len(word) == max_length]

    return l_words


def main():
    """
        Головна виконавча функція.

        Парсить аргументи командного рядка, знаходить найдовші
        слова у вказаному файлі, і виводить їх.
        Обробляє помилки, пов'язані з файлом.
    """
    args = parse_word()

    try:
        l_words = searching_longest_word(args.file)
        print(f'В файлі ми маємо такі найдовші слова як: {l_words}')
    except FileNotFoundError:
        print(f'Файл не знайдено {args.file}')
    except Exception as error:
        print(f'Сталася помилка при обробці файлу: {error}')
    finally:
        print('\nФайл успішно оброблено')


if __name__ == '__main__':
    main()
