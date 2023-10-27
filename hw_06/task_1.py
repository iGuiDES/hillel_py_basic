# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

loan_amount = int(input("Введіть суму кредиту: "))

periods = [12, 60]

for period in periods:
    remaining_principal = loan_amount

    print(f"\nПлатежі для погашення кредиту за {'1 рік' if period == 12 else '5 років'}:")

    headers = "{:<15} {:<20} {:<25}".format("Номер місяця", "Сума виплати", "Проценти нараховано")

    print(headers)
    print("-" * 60)

    for month in range(1, period + 1):
        if month <= 24:
            monthly_rate = 0.02
        else:
            monthly_rate = 0.04

        percent = remaining_principal * monthly_rate
        principal_payment = (loan_amount / period)
        monthly_payment = principal_payment + percent
        remaining_principal -= principal_payment

        row = "{:<15} {:<20.2f} {:<25.2f}".format(month, monthly_payment, percent)
        print(row)

        if month == 12 or month == 24 or month == 36 or month == 48 or month == 60:
            print("-" * 60)
