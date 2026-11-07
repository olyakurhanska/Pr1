
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 82:
        return "B"
    elif score >= 74:
        return "C"
    elif score >= 64:
        return "D"
    elif score >= 60:
        return "E"
    elif score >= 35:
        return "FX"
    else:
        return "F"


def main():
    try:
        score = int(input("Введіть оцінку (0-100): "))
    except ValueError:
        print("Помилка: введіть ціле число")
        return

    if score < 0 or score > 100:
        print("Помилка: оцінка має бути від 0 до 100")
    else:
        grade = classify_grade(score)
        print(f"Оцінка {score} - ЄКТС: {grade}")

        if grade == "FX" or grade == "F":
            print("Результат: Не зараховано")
        else:
            print("Результат: Зараховано")


if __name__ == "__main__":
    main()
