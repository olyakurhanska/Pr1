
def calculator():
    history = []

    print("Калькулятор")
    print("Введіть: число оператор число")
    print("Команди: history, quit")

    while True:
        user_input = input("\n> ").strip()

        if user_input == "quit":
            print("Завершення роботи")
            break

        if user_input == "history":
            if not history:
                print("Історія порожня")
            else:
                for item in history:
                    print(item)
            continue

        parts = user_input.split()

        if len(parts) != 3:
            print("Неправильний формат")
            continue

        try:
            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])
        except ValueError:
            print("Введіть правильні числа")
            continue

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                print("Ділення на нуль неможливе")
                continue
            result = a / b
        elif operator == "//":
            if b == 0:
                print("Ділення на нуль неможливе")
                continue
            result = a // b
        elif operator == "%":
            if b == 0:
                print("Ділення на нуль неможливе")
                continue
            result = a % b
        elif operator == "**":
            result = a ** b
        else:
            print("Невідомий оператор")
            continue

        record = f"{a:g} {operator} {b:g} = {result:g}"
        print(record)
        history.append(record)


if __name__ == "__main__":
    calculator()
