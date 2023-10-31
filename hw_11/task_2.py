import random


def func_generator(start: int, stop: int):
    """
        Дана функція буде перевіряти чи просте число
        та повертати їх

        Параметри:
        start - ціле число, згенероване за допомогою модуля random
        stop - ціле число, згенероване за допомогою модуля random
        yield - це наступне просте число в діапазоні
    """

    for gen_num in range(start, stop + 1):
        if gen_num <= 1:
            continue
        if gen_num <= 3:
            yield gen_num
            continue
        if gen_num % 2 == 0 or gen_num % 3 == 0:
            continue

        next_number = 5
        is_prime = True

        while next_number * next_number <= gen_num:
            if gen_num % next_number == 0 or gen_num % (next_number + 2) == 0:
                is_prime = False
                break
            next_number += 6
        if is_prime:
            yield gen_num


if __name__ == "__main__":
    g_nums_start = random.randint(1, 50)
    g_nums_stop = random.randint(50, 100)

    prime_numbers = func_generator(g_nums_start, g_nums_stop)

    print(f"Створення простих чисел між {g_nums_start} and {g_nums_stop}:")
    print(" ".join(
            map(str, prime_numbers)
        )
    )

