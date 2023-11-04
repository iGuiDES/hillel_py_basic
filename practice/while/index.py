x = 0

while x < 3:
    print(f'x equals {x}')
    x += 1

while x < 3:
    print(f'x equals {x}')
    x += 1
else:
    print('Condition is not met')

while x < 3:
    if x == 2:
        break
    print(f'x equals {x}')

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0

for i in vals:
    if i % 2 == 0:
        continue
    else:
        sum += i
    if sum > 10:
        break

print(sum)

for i in vals:
    pass  # У випадку, коли даний блок коду нічого не робить


