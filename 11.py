def matrix_statistics(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    elements = []
    row_sums = []
    col_sums = []

    for i in range(rows):
        s = 0

        for j in range(cols):
            elements.append(matrix[i][j])
            s += matrix[i][j]

        row_sums.append(s)

    for j in range(cols):
        s = 0

        for i in range(rows):
            s += matrix[i][j]

        col_sums.append(s)

    total = sum(elements)
    average = total / len(elements)

    print(f"\nРазмер: {rows} x {cols}")
    print(f"Минимальный элемент: {min(elements):g}")
    print(f"Максимальный элемент: {max(elements):g}")
    print(f"Сумма элементов: {total:g}")
    print(f"Среднее значение: {average:.2f}")

    print("\nСуммы строк:",
          [float(f"{x:.10g}") for x in row_sums])

    print("Суммы столбцов:",
          [float(f"{x:.10g}") for x in col_sums])


def input_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(
                    f"Введите строку {i + 1}: "
                ).split()))

                if len(row) != cols:
                    print(f" Нужно ввести {cols} чисел.")
                    continue

                matrix.append(row)
                break

            except ValueError:
                print(" Вводите только числа.")

    return matrix


try:
    m = int(input("Количество строк: "))
    n = int(input("Количество столбцов: "))

    if m <= 0 or n <= 0:
        print(" Размеры должны быть больше нуля.")
    else:
        a = input_matrix(m, n)
        matrix_statistics(a)

except ValueError:
    print(" Введите целое число.")
