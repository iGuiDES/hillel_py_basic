def func_with_try_except(user_value_one, user_value_two):
    try:
        number_one = float(user_value_one)
        number_two = float(user_value_two)

        return number_one + number_two
    except ValueError:
        return user_value_one + user_value_two

    except Exception as error:
        print(f'Сталася помилка в роботі функції {error}')

    finally:
        print('\nФункція відпрацювала успішно.', end=" ")


if __name__ == '__main__':
    result_with_num = func_with_try_except(
        '3', '12'
    )

    print(f'Результат: {result_with_num}')

    result_with_str = func_with_try_except(
        '10', 'десять'
    )

    print(f'Результат: {result_with_str}')
