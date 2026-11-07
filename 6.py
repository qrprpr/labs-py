def main_diagonal(matrix):
    result = []

    for i in range(len(matrix)):
        result.append(matrix[i][i])

    return result


def secondary_diagonal(matrix):
    result = []
    n = len(matrix)

    for i in range(n):
        result.append(matrix[i][n - 1 - i])

    return result


def trace(matrix):
    return sum(main_diagonal(matrix))


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


try:
    n = int(input("Размер квадратной матрицы: "))

    if n <= 0:
        print("Размер должен быть больше нуля.")
    else:
        a = input_matrix(n, n)

        main = main_diagonal(a)
        secondary = secondary_diagonal(a)

        print("\nГлавная диагональ:", main)
        print("Побочная диагональ:", secondary)

        print("Сумма главной диагонали:", sum(main))
        print("Сумма побочной диагонали:", sum(secondary))
        print("След матрицы:", trace(a))

except ValueError:
    print("Введите целое число.")
