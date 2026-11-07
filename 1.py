def input_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        while True:
            try:
                line = input(f"Введите строку {i + 1}: ")
                row = [float(x) for x in line.split()]

                if len(row) != cols:
                    print(f"Нужно ввести {cols} чисел.")
                    continue

                matrix.append(row)
                break

            except ValueError:
                print("Вводите только числа.")

    return matrix


def print_matrix(matrix):
    print("\nМатрица:")

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
        matrix = input_matrix(m, n)
        print_matrix(matrix)

except ValueError:
    print("Размеры должны быть целыми числами.")
