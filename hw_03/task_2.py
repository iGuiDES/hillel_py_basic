# pylint: disable=missing-module-docstring

e_class_1 = int(input('Скільки учнів у класі №1: '))
e_class_2 = int(input('Скільки учнів у класі №2: '))
e_class_3 = int(input('Скільки учнів у класі №3: '))

several_desks = (e_class_1 + 1) // 2 + (e_class_2 + 1) // 2 + (e_class_3 + 1) // 2

print('Кількість парт, що треба закупити: ', several_desks, 'одиниць')
