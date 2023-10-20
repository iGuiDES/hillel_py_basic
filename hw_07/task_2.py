numbers = {i: i+1 for i in range(20)}

_sum = 1
for number in numbers.values():
    _sum *= number

print("Згенерований словник:", numbers)
print("Результат множення чисел:", _sum)
