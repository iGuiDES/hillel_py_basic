_str = "Hello, Python 3"

print(_str.lower())
print(_str.upper())

print(_str[2::5])
print(_str[::-1])
print(_str[0::len(_str)])

name = 'Oleksandr'
surname = 'Yatsenko'
age = 30

my_string = "My name is {}. My surname is {}. I`m {} years old."
print(my_string.format(name, surname, age))

print(f"My name is {name}. My surname is {surname}. I am {age} years old")

result = _str.isdigit

print(result)

for letter in _str:
    print(letter)

print(_str)
