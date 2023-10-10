print("*" * 10, 'A', "*" * 10)

first_tuple = (1, 2, 3)
second_tuple = (3, 4, 5)

result = list(set(first_tuple + second_tuple))
print("Результат 'List': ", result)

print("*" * 10, 'B', "*" * 10)

tuple_result = (result, first_tuple[::-1], second_tuple[::-1])
print("Результат 'Кортежу': ", tuple_result)

print("*" * 10, 'С', "*" * 10)

print(tuple_result[0][2])
print(tuple_result[1][2])
print(tuple_result[2][2])
