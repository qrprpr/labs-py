def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Размеры матриц не совпадают.")
        return None

    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)

    return result


def subtract_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Размеры матриц не совпадают.")
        return None

    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] - b[i][j])
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
    m = int(input("Количество строк: "))
    n = int(input("Количество столбцов: "))

    if m <= 0 or n <= 0:
        print("Размеры должны быть больше нуля.")
    else:
        print("\nМатрица A:")
        a = input_matrix(m, n)

        print("\nМатрица B:")
        b = input_matrix(m, n)

        print("\nA + B:")
        print_matrix(add_matrices(a, b))

        print("\nA - B:")
        print_matrix(subtract_matrices(a, b))

except ValueError:
    print("Размеры должны быть целыми числами.")
