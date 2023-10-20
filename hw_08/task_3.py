lst = [1, 2, 3, "text", (4, 5), [6, 7], {"key": "value"}, 8, 9, 10]

result_set = set()
lst_no_hashable = []

hashable_types = (int, float, str, tuple, frozenset, bytes)
for item in lst:
    if type(item) in hashable_types:
        result_set.add(item)
    else:
        lst_no_hashable.append(item)


print('Хешуємі значення:', result_set)
print('Не хешуємі значення:', lst_no_hashable)
