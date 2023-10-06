year = int(input('Введіть рік: '))

if year < 1900 or year < 1_000_000:
    print('Рік', year, 'не відповідає вимогам!')
else:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, '- is leep year')
    else:
        print(year, '- is not leep year')
