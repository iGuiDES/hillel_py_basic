user_number = int(input('Enter your number: '))

result = ''

for i in range(0, user_number):
    result += '*'
    print(result)

print(f'\n\n{"-" * 30}\n\n')

for i in range(0, user_number + 1):
    if i % 2 == 0:
        print(f'{i} is EVEN')
    else:
        print(f'{i} is ODD')
