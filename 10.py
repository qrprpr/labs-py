def identity_matrix(n):
    result = []

    for i in range(n):
        row = []

        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)

        result.append(row)

    return result


def is_identity(matrix, eps=1e-9):
    n = len(matrix)

    if n == 0 or any(len(row) != n for row in matrix):
        return False

    for i in range(n):
        for j in range(n):
            expected = 1 if i == j else 0

            if abs(matrix[i][j] - expected) >= eps:
                return False

    return True


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


try:
    n = int(input("Размер матриц: "))

    if n <= 0:
        print("Размер должен быть больше нуля.")
    else:
        matrices = []

        for name in ["A", "Обратная A"]:
            print(f"\nМатрица {name}:")
            matrix = []

            for i in range(n):
                while True:
                    try:
                        row = list(map(float, input(
                            f"Введите строку {i + 1}: "
                        ).split()))

                        if len(row) != n:
                            print(f"Нужно ввести {n} чисел.")
                            continue

                        matrix.append(row)
                        break

                    except ValueError:
                        print(" Вводите только числа.")

            matrices.append(matrix)

        a = matrices[0]
        inverse = matrices[1]

        product = multiply_matrices(a, inverse)

        print("\nЕдиничная матрица:")
        for row in identity_matrix(n):
            print(row)

        print("\nПроизведение:")
        for row in product:
            print(row)

        if is_identity(product):
            print("\nПроверка пройдена!")
        else:
            print("\nПроверка не пройдена.")

except ValueError:
    print("Введите целое число.")
