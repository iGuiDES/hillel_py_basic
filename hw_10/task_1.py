def has_pair_sum(lst_nums, target_num):
    """
        Функція has_pair_sum приймає на вхід список чисел lst_nums та
        одне ціле число target_num. Завданням функції є визначити, чи
        існує пара чисел у списку, сума якої рівна значенню target_num.

        Ось як функція працює:

        1. Створюється порожній список numbers.
        2. Починаємо ітерацію по кожному числу в lst_nums.
        3. Для кожного числа перевіряємо, чи існує число в списку numbers,
        яке є різницею між target_num та поточним числом. Якщо так, повертаємо
        True, бо ми знайшли пару, що задовольняє умову.
        4. Якщо попередня умова не виконується, додаємо поточне число до
        списку numbers.
        5. Якщо ітерація завершена і пару не знайдено, повертаємо False.
    """

    numbers = []

    for number in lst_nums:
        if target_num - number in numbers:
            return True
        numbers.append(number)
    return False


lst_1 = [2, 7, 11, 15, 4, 12, 18]
num_target_1 = 20

lst_2 = [1, 3, 5, 7, 14, 20, 99]
num_target_2 = 11


result_1 = has_pair_sum(lst_1, num_target_1)
result_2 = has_pair_sum(lst_2, num_target_2)

print(f"У результаті виклику функції в 'result_1' отримаємо: {result_1}")
print(f"У результаті виклику функції в 'result_2' отримаємо: {result_2}")
