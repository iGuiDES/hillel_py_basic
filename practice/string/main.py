word = 'Hello, Python!'
word_list = list(word)

print(word)

word_list.append('!!')
result = "".join(word_list)
print(result.upper())
print(result.lower())
print(result.capitalize())

print(word_list)
print(result)
print(len(word))


text = 'football,basketball,skate,drive'
hobbies = text.split(',')

hobbies_list = []

for item in hobbies:
    hobbies_list.append(item.capitalize())

print(hobbies_list)

for i in range(0, len(hobbies)):
    hobbies[i] = hobbies[i].capitalize()

print(hobbies)

result_list = ",".join(hobbies)

print(hobbies_list)

# Index and slice

list_numbers = [5, 4, True, "Some text", [6, 8]]

# тільки останній елемент
print(list_numbers[-1])

# все, окрім останього елементу списку
print(list_numbers[:-1])

# тільки до 2-го елементу з індексом 1
print(list_numbers[:2])

# все від першого елементу до останього з кроком 2 (тобто парні елементи будуть пропущені)
print(list_numbers[0::2])

# для того, що розвернути список у зворотньому порядку можемо використати
# наступну конструкцію
print(list_numbers[::-1])

# для того, щоб вибрати діапазон, в якому будуть вибрані значення списку,
# можемо скористатися наступним виразом, де 0 - старт, 4 - стоп та 1 - крок
print(list_numbers[0:4:1])

# всі елементи будуть виводитися в зворотньому порядку з лімітом в 4 символи
print(list_numbers[:-4:-1])
