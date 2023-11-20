users_input_dict = dict()


for n in range(3):
    question_key = input('Введіть ключ: ')
    question_value = input('Введіть значення: ')

    users_input_dict[question_key] = question_value

print(users_input_dict)
