
import math

def triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "не є трикутником"

    if a + b <= c or a + c <= b or b + c <= a:
        return "не є трикутником"

    if a == b and b == c:
        return "рівносторонній"
    elif a == b or a == c or b == c:
        return "рівнобедрений"
    else:
        sides = sorted([a, b, c])
        if abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-9:
            return "прямокутний"
        else:
            return "різносторонній"


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def main():
    try:
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        c = float(input("Введіть сторону c: "))
    except ValueError:
        print("Помилка: введіть числа")
        return

    kind = triangle_type(a, b, c)
    print("Тип трикутника:", kind)

    if kind != "не є трикутником":
        print(f"Площа трикутника: {triangle_area(a, b, c):.2f}")


if __name__ == "__main__":
    main()
