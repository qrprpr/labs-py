def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
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
        print("\nИсходная матрица:")
        a = input_matrix(m, n)

        b = transpose(a)

        print("\nИсходная матрица:")
        print_matrix(a)

        print("\nТранспонированная матрица:")
        print_matrix(b)

except ValueError:
    print("Размеры должны быть целыми числами.")
