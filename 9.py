def inverse_matrix(matrix, eps=1e-12):
    n = len(matrix)

    if n == 0 or any(len(row) != n for row in matrix):
        print("Матрица должна быть квадратной.")
        return None

    a = []

    for i in range(n):
        row = matrix[i].copy()

        for j in range(n):
            if i == j:
                row.append(1.0)
            else:
                row.append(0.0)

        a.append(row)

    for i in range(n):
        pivot = i

        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[pivot][i]):
                pivot = j

        if abs(a[pivot][i]) < eps:
            print("Обратной матрицы не существует.")
            return None

        a[i], a[pivot] = a[pivot], a[i]

        div = a[i][i]

        for j in range(2 * n):
            a[i][j] /= div

        for k in range(n):
            if k != i:
                factor = a[k][i]

                for j in range(2 * n):
                    a[k][j] -= factor * a[i][j]

    result = []

    for i in range(n):
        result.append(a[i][n:])

    return result


def multiply_matrices(a, b):
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


def is_identity(matrix, eps=1e-9):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            expected = 1 if i == j else 0

            if abs(matrix[i][j] - expected) >= eps:
                return False

    return True


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

        inverse = inverse_matrix(a)

        if inverse is not None:
            print("\nОбратная матрица:")

            for row in inverse:
                for num in row:
                    print(f"{num:.4g}", end="  ")
                print()

            product = multiply_matrices(a, inverse)

            print("\nПроверка A * A^(-1):")

            for row in product:
                for num in row:
                    print(f"{num:.4g}", end="  ")
                print()

            if is_identity(product):
                print("Проверка пройдена!")
            else:
                print("Проверка не пройдена.")

except ValueError:
    print("Введите корректное число.")
