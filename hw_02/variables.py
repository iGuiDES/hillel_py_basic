"""
    In this module, the practice of working with variables and their use
    has been worked out built-in function input for interaction with users
    and print for outputting the result
"""

# A
print("___________A___________")

# Variant 1

first_number_one = 100
second_number_one = 200

print(first_number_one, second_number_one)

third_number_one = first_number_one
first_number_one = second_number_one
secondNumber = third_number_one

print(first_number_one, secondNumber)

# Variant 2

first_number_two = 1000
second_number_two = 2000

print(first_number_two, second_number_two)

first_number_two, second_number_two = second_number_two, first_number_two

print(first_number_two, second_number_two)

# Variant 3
first_number_three = 10000
second_number_three = 20000

print(first_number_three, second_number_three)

first_number_three = first_number_three + second_number_three
second_number_three = first_number_three - second_number_three
first_number_three = first_number_three - second_number_three

print(first_number_three, second_number_three)

# B
print("___________B___________")

username = input("ваше ім'я: ")
surname = input("ваше прізвище: ")
age = int(input("ваш вік: "))

print("Привіт", surname)
print(username, "це гарне ім'я - мені подобається.")
print("До 100 років тобі залишилося жити", 100 - age, "років")

# C
print("___________C___________")

five_digit_number = int(input("введіть 5 значне число -> : "))

thousands = (five_digit_number // 1000) % 10
hundreds = (five_digit_number // 100) % 10
tens = (five_digit_number // 10) % 10
ones = five_digit_number % 10

count_of_threes = five_digit_number // 3
count_of_sixes = five_digit_number // 6

print("тисячі:", thousands)
print("сотні:", hundreds)
print("десятки:", tens)
print("одиниці:", ones)
print("трійок у числі:", count_of_threes)
print("шісток у числі:", count_of_sixes)
