

def factorial(n):
    result = 1
    for i in range(1, n + 1, 1):
        result *= i
    return result


def harmonic_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / i
    return total


def multiplication_table(n):
    print("Парні числа:", list(range(2, n + 1, 2)))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()


def main():
    n = int(input("Введіть число n: "))

    if n < 1:
        print("Введіть додатне ціле число")
        return

    print(f"{n}! = {factorial(n)}")
    print(f"Гармонічна сума H({n}) = {harmonic_sum(n):.6f}")
    print(f"\nТаблиця множення {n}x{n}:")
    multiplication_table(n)


if __name__ == "__main__":
    main()
