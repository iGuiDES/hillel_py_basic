user_string = input('Введіть рядок довжиною 15 символів: ')

if len(user_string) == '':
    print('Введені дані не відповідають вимогам!')
else:
    if len(user_string) < 15:
        user_string += user_string * 3

    char_list = list(user_string)
    print('Повний список: ', char_list)
    print('Останні 5 елементів: ', char_list[-5:])

    reverse_list = char_list[::-1]
    print('Список у зворотній послідовності: ', reverse_list)

    even_list = [char_list]