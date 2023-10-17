user_number = int(input("Input number: "))

for i in range(user_number):
    line = '1' + '0' * i
    print(f"{i} {line.rjust(user_number + 1)}")
