# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

user_input = input("Будь ласка, введіть рядок з 15-ма символами: ")

if len(user_input) == 0:
    print("Рядок не може бути пустим. Спробуйте ще раз")
else:
    while len(user_input) < 15:
        user_input += user_input * 3

    char_list = list(user_input[:15])

    print('Повний список: ', char_list)
    print('Останніх 5 елементів списку: ', char_list[-5:])
    print('Список в зворотній послідовності: ', char_list[::-1])
    print('Елементи з парними послідовностями: ', char_list[::2])

    if char_list[:5] == char_list[-5:]:
        print("Перші 5 елементів такі ж, як останні 5 елементів списку.")
    else:
        print("Перші 5 елементів НЕ такі ж, як останні 5 елементів списку.")
