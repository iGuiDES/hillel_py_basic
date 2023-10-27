# pylint: disable=missing-module-docstring

list_for_keys = [1, 2, 3, 4, 5]
list_for_values = ['one', 'two', 'three', 'four', 'five']

dict_with_lists = dict(zip(list_for_keys, list_for_values))

print(dict_with_lists)
