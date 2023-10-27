def has_pair_sum(lst_nums, target_num):
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
