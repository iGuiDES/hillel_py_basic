# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

import random

random_set = {random.randint(100, 200) for _ in range(15)}

odd_sum = sum(x for x in random_set if x % 2 != 0)
even_sum = sum(y for y in random_set if y % 2 == 0)

if odd_sum > even_sum:
    print('Так')
else:
    print('Ні')
