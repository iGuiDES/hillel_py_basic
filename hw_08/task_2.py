list1 = [1, 2, 3, 4, 5, 5, 5]
list2 = [4, 5, 6, 7, 8, 8, 8]

set1 = set()
set2 = set()

for number in list1:
    set1.add(number)

for number in list2:
    set2.add(number)

common_elements = set1.intersection(set2)

print("Елементи, які містяться як у першому, так і у другому списку:", common_elements)
print("Кількість таких елементів:", len(common_elements))
