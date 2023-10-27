# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

user_number = int(input("Input number: "))
with_n = len(str(user_number))

for i in range(user_number):
    line = '1' + '0' * i
    print(f"{i:{with_n}} {line.rjust(user_number + 1)}")
