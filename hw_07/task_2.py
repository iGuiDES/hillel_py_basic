# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

numbers = {}
for i in range(20):
    numbers[i] = i+1

_sum = 1
for number in numbers.values():
    _sum *= number

print("Згенерований словник:", numbers)
print("Результат множення чисел:", _sum)
