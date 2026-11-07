def determinant(matrix):
    n = len(matrix)

    if n == 0:
        return 1

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1]
                - matrix[0][1] * matrix[1][0])

    det = 0

    for j in range(n):
        minor = []

        for i in range(1, n):
            row = []

            for k in range(n):
                if k != j:
                    row.append(matrix[i][k])

            minor.append(row)

        det += (-1) ** j * matrix[0][j] * determinant(minor)

    return det


def get_minor(matrix, row, col):
    n = len(matrix)

    if row < 0 or row >= n or col < 0 or col >= n:
        raise ValueError("Неверные индексы.")

    result = []

    for i in range(n):
        if i == row:
            continue

        new_row = []

        for j in range(n):
            if j != col:
                new_row.append(matrix[i][j])

        result.append(new_row)

    return result


def cofactor(matrix, row, col):
    minor = get_minor(matrix, row, col)
    return (-1) ** (row + col) * determinant(minor)


try:
    n = int(input("Размер квадратной матрицы: "))

    if n <= 0:
        print("Размер должен быть больше нуля.")
    else:
        a = []

        for i in range(n):
            while True:
                try:
                    row = list(map(float, input(
                        f"Введите строку {i + 1}: "
                    ).split()))

                    if len(row) != n:
                        print(f"Нужно ввести {n} чисел.")
                        continue

                    a.append(row)
                    break

                except ValueError:
                    print("Вводите только числа.")

        i = int(input("Индекс строки (от 0): "))
        j = int(input("Индекс столбца (от 0): "))

        minor = get_minor(a, i, j)

        print("\nМинор:")
        for row in minor:
            print(row)

        print("Алгебраическое дополнение:",
              f"{cofactor(a, i, j):g}")

except ValueError as e:
    print("Ошибка!", e)
