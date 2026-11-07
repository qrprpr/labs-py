def multiply_by_scalar(matrix, scalar):
    result = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j] * scalar)
        result.append(row)

    return result


def input_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(
                    f"Введите строку {i + 1}: "
                ).split()))

                if len(row) != cols:
                    print(f"Нужно ввести {cols} чисел.")
                    continue

                matrix.append(row)
                break

            except ValueError:
                print("Вводите только числа.")

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f"{num:g}", end="  ")
        print()


try:
    m = int(input("Количество строк: "))
    n = int(input("Количество столбцов: "))

    if m <= 0 or n <= 0:
        print("Размеры должны быть больше нуля.")
    else:
        print("\nМатрица A:")
        a = input_matrix(m, n)

        k = float(input("\nВведите число k: "))

        b = multiply_by_scalar(a, k)

        print("\nРезультат:")
        print_matrix(b)

except ValueError:
    print("Введите корректное число.")
