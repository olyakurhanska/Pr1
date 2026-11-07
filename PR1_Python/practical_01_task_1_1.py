
import math

def main():
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    sum_squares = a ** 2 + b ** 2 + c ** 2
    average = (a + b + c) / 3
    discriminant = b ** 2 - 4 * a * c
    hypotenuse = math.sqrt(a ** 2 + b ** 2)

    
    # Перевірка можливості існування трикутника
    is_triangle = (
        a > 0 and b > 0 and c > 0 and
        not (a + b <= c or a + c <= b or b + c <= a)
    )


    remainder = a % b if b != 0 else None
    integer_division = a // b if b != 0 else None

    print(f"Сума квадратів: {sum_squares:.2f}")
    print(f"Середнє арифметичне: {average:.2f}")
    print(f"Дискримінант: {discriminant:.2f}")
    print(f"Гіпотенуза: {hypotenuse:.2f}")
    print(f"Чи утворюють числа трикутник: {is_triangle}")
    print(f"Залишок від ділення a на b: {remainder}")
    print(f"Цілочисельне ділення a на b: {integer_division}")

if __name__ == "__main__":
    main()
