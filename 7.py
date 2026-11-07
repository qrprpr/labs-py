def determinant(matrix):
    n = len(matrix)

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


def input_matrix(n):
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
                print("Вводите только числа.")

    return matrix


try:
    n = int(input("Размер квадратной матрицы: "))

    if n <= 0:
        print("Размер должен быть больше нуля.")
    else:
        a = input_matrix(n)

        print("\nОпределитель:", f"{determinant(a):g}")

except ValueError:
    print("Введите целое число.")
