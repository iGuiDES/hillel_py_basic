"""
    Цей модуль надає функціонал для створення та форматування текстових
    повідомлень з різними стилями та кольорами.
    Він включає функції для застосування кольорів тексту, стилів тексту,
    та генерації стилізованих повідомлень для різних
    рівнів журналів, таких як помилка, попередження та інформація.
    Коди кольорів та стилів визначені заздалегідь та можуть бути застосовані
    до тексту.
"""

colour = {
    'red': '31m',
    'black': '30m',
    'green': '32m',
    'yellow': '33m',
    'blue': '34m',
    'purpure': '35m',
    'biruza': '36m',
    'white': '37m',
}


def color_text(text: str, colour_name: str) -> str:
    """
        Застосовує вказаний колір до заданого текстового рядка.

        Ця функція додає ANSI-коди кольору навколо тексту, змінюючи його
        колір в терміналі.

        Параметри:
        text (str): Текст, який потрібно забарвити.
        colour_name (str): Назва кольору, яка повинна бути ключем
        зі словника 'colour'.

        Повертає:
        str: Текст, обрамлений ANSI-кодами відповідного кольору.
    """
    coloured_txt = '\033[' + colour_name + text + '\033[0m'
    return coloured_txt


def styled(text: str, code: str = "3m") -> str:
    """
        Застосовує вказаний ANSI-стиль до заданого текстового рядка.

        Функція додає ANSI-коди стилю навколо тексту, що дозволяє стилізувати
        текст, наприклад, зробити його жирним або курсивним в терміналі.

        Параметри:
        text (str): Текст, який потрібно стилізувати.
        code (str): ANSI-код стилю, який буде застосований.
        За замовчуванням "3m" (курсив).

        Повертає:
        str: Текст, обрамлений вказаними ANSI-кодами стилю.
    """

    clean_style_code = '\033[0m'
    styled_txt = f'\033[{code}{text}{clean_style_code}'
    return styled_txt


def background_color(text: str, bg_colour: str = '45m') -> str:
    """
        Застосовує вказаний колір фону до заданого текстового рядка.

        Параметри:
        text (str): Текст, для якого потрібно змінити фон.
        bg_colour_name (str): Назва кольору фону зі словника 'colour'.

        Повертає:
        str: Текст зі зміненим кольором фону.
    """
    bg_colour_code = '\033[' + bg_colour
    return f'{bg_colour_code}{text}\033[0m'


def error_message(message: str) -> str:
    """
        Генерує повідомлення про помилку з певним форматуванням.

        Функція створює відформатоване повідомлення про помилку,
        забарвлюючи статус "ERROR" в червоний колір, а повідомлення - в жовтий.

        Параметри:
        message (str): Повідомлення про помилку для відображення.

        Повертає:
        str: Відформатоване повідомлення про помилку.
    """

    status = "ERROR"
    error = color_text(f"{status:<8} ", colour['red'])
    _message = color_text(message, colour['yellow'])
    err_message = error + _message
    return err_message


def warning_message(message: str) -> str:
    """
        Генерує попереджувальне повідомлення з певним форматуванням.

        Функція створює відформатоване попереджувальне повідомлення,
        забарвлюючи статус "WARNING" в жовтий колір,
        а повідомлення - в колір бірюзи.

        Параметри:
        message (str): Попереджувальне повідомлення для відображення.

        Повертає:
        str: Відформатоване попереджувальне повідомлення.
    """

    status = "WARNING"
    warn = color_text(f"{status:<8} ", colour['yellow'])
    _message = color_text(message, colour['biruza'])
    warn_message = warn + _message
    return warn_message


def info_message(message: str) -> str:
    """
        Генерує інформаційне повідомлення з певним форматуванням.

        Функція створює відформатоване інформаційне повідомлення, забарвлюючи
        статус "INFO" в колір пурпуру.

        Параметри:
        message (str): Інформаційне повідомлення для відображення.

        Повертає:
        str: Відформатоване інформаційне повідомлення.
    """

    status = "INFO"
    info = color_text(f"{status:<8} ", colour['purpure'])
    info_msg = info + message
    return info_msg
