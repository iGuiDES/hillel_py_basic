list_numbers = [10, 75, 43, 15, 25, -4, 27]


def bubble_sort(lst):
    last_item = len(lst) - 1

    for i in range(0, last_item):
        for j in range(0, last_item):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


result = bubble_sort(list_numbers)
print(result)
