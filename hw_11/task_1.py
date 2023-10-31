hypotenuse = lambda x=1, y=1: (x ** 2 + y ** 2) ** 0.5

add_ten = lambda x: x + 10

sum_of_two_lists = lambda x, y: x + y

if __name__ == "__main__":
    print(f"\n\n{'*' * 20} Task 1.1 {'*' * 20} \n\n")

    print(
        f'Довжина гіпотенузи без параметрів: {round(hypotenuse(), 1)}'
    )

    print(
        f'Довжина гіпотенузи з параметрами: {round(hypotenuse(10, 12), 1)}'
    )

    print(f"\n\n{'*' * 20} Task 1.2 {'*' * 20} \n\n")

    single_list_result = map(
        add_ten,
        [x for x in range(10, 40, 3)]
    )

    double_list_result = map(
        sum_of_two_lists,
        [x for x in range(0, 10)],
        [y for y in range(10, 20)]
    )

    print(
        f'З одним список: {list(single_list_result)}'
    )

    print(
        f'З двома списками: {list(double_list_result)}'
    )
