class TriangleChecker:
    @staticmethod
    def is_valid(a, b, c):
        return (
                a > 0 and b > 0 and 0 < c < a + b and a + c > b and b + c > a
        )


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class ExtTriangle(Triangle, TriangleChecker):
    def is_triangle(self):
        if not all(isinstance(side, (int, float)) for side in
                   [self.a, self.b, self.c]):
            return "Потрібно вводити тільки числа!"
        if any(side < 0 for side in [self.a, self.b, self.c]):
            return "З негативними числами нічого не вийде!"
        if self.is_valid(self.a, self.b, self.c):
            return "Ура, можна побудувати трикутник!"
        else:
            return "Жаль, але з цього трикутник не зробити."


if __name__ == '__main__':
    print(f"\n\n{'*' * 50}\n\n")

    res_1 = ExtTriangle(3, 4, 5)
    print(f"Результат: {res_1.is_triangle()}")

    res_2 = ExtTriangle(-3, 4, 5)
    print(f"Результат: {res_2.is_triangle()}")

    res_3 = ExtTriangle(3, "a", 5)
    print(f"Результат: {res_3.is_triangle()}")

    res_4 = ExtTriangle(1, 2, 3)
    print(f"Результат: {res_4.is_triangle()}")

    print(f"\n\n{'*' * 50}")
