# pylint: disable=missing-module-docstring

user_number = input('Введіть число:')

checker = False

for i in range(len(user_number)):
    for j in range(i + 1, len(user_number)):
        if user_number[i] == user_number[j]:
            checker = True
            break

if checker:
    print('Так')
else:
    print('Ні')
