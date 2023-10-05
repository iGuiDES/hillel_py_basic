user_name = 'Олександр'
my_root_password = 'P@$w0rd'
password_entered = input('Введіть Ваш пароль: ')

if my_root_password != password_entered:
    print('Відмовлено у доступі!')
else:
    print('Вітаємо Вас,', user_name, 'Ваш пароль прийнято!')
