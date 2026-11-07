
def main():
    raw_input = input("Введіть ціле число: ")

    try:
        number = int(raw_input)
    except ValueError:
        print("Помилка: введене значення не є цілим числом")
        return

    print(f"Ціле число: {number}, тип: {type(number)}")
    print(f"Дійсне число: {float(number):.2f}")
    print(f"Логічне значення: {bool(number)}")
    print(f"Рядок: {str(number)}, тип: {type(str(number))}")
    print(f"Перевірка типу int: {isinstance(number, int)}")

    name = input("Введіть ім'я: ")
    age = int(input("Введіть вік: "))

    print(f"Ім'я: {name:<12} Вік: {age:03d}")
    print(f"Вік через 5 років: {age + 5}")

    numbers = list(range(2, 13, 2))
    print("Список чисел:", numbers)
    print("Довжина списку:", len(numbers))
    print("ID списку:", id(numbers))


if __name__ == "__main__":
    main()
