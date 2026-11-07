def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        print("Матрицы нельзя умножить.")
        return None

    result = []

    for i in range(len(a)):
        row = []

        for j in range(len(b[0])):
            s = 0

            for k in range(len(b)):
                s += a[i][k] * b[k][j]

            row.append(s)

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
    if matrix is None:
        return

    for row in matrix:
        for num in row:
            print(f"{num:g}", end="  ")
        print()


try:
    m = int(input("Строк матрицы A: "))
    n = int(input("Столбцов матрицы A: "))

    p = int(input("Строк матрицы B: "))
    k = int(input("Столбцов матрицы B: "))

    if m <= 0 or n <= 0 or p <= 0 or k <= 0:
        print("Размеры должны быть больше нуля.")

    elif n != p:
        print("Матрицы нельзя умножить.")

    else:
        print("\nМатрица A:")
        a = input_matrix(m, n)

        print("\nМатрица B:")
        b = input_matrix(p, k)

        c = multiply_matrices(a, b)

        print("\nРезультат A * B:")
        print_matrix(c)

except ValueError:
    print("Введите корректное число.")
