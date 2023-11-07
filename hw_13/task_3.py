def update_hero(**kwargs):
    """
    Оновлює значення у файлі конфігурації героя.

    Параметри:
        **kwargs: Через аргументи ключ-значення передаються поля та їх
        нові значення.

    Приклад виклику:
        update_hero(hero="Halk", power=450, Y=2.3)
    """

    with open('hero.ini', 'r') as file:
        hero_lst = file.readlines()

    updated_list = []
    for line in hero_lst:
        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            if key in kwargs:
                updated_list.append(f'{key}={kwargs[key]}\n')
            else:
                updated_list.append(line)
        else:
            updated_list.append(line)

    with open('hero.ini', 'w') as file:
        file.writelines(updated_list)


update_hero(hero="Halk", power=550, Y=2.3)
