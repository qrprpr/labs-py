def input_matrix():
    while True:
        try:
            m = int(input("Количество строк: "))
            n = int(input("Количество столбцов: "))

            if m > 0 and n > 0:
                break

            print("Размеры должны быть больше нуля.")

        except ValueError:
            print("Введите целые числа.")

    matrix = []

    for i in range(m):
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


def print_matrix(matrix):
    if matrix is None:
        print("Матрица отсутствует.")
        return

    for row in matrix:
        for x in row:
            print(f"{x:10.4g}", end=" ")
        print()


def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
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
        return None

    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] - b[i][j])
        result.append(row)

    return result


def multiply_by_scalar(matrix, scalar):
    result = []

    for row in matrix:
        new_row = []

        for x in row:
            new_row.append(x * scalar)

        result.append(new_row)

    return result


def transpose(matrix):
    result = []

    for j in range(len(matrix[0])):
        row = []

        for i in range(len(matrix)):
            row.append(matrix[i][j])

        result.append(row)

    return result


def multiply_matrices(a, b):
    if len(a[0]) != len(b):
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


def inverse_matrix(matrix, eps=1e-12):
    n = len(matrix)
    a = []

    for i in range(n):
        row = matrix[i].copy()

        for j in range(n):
            row.append(1.0 if i == j else 0.0)

        a.append(row)

    for i in range(n):
        pivot = i

        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[pivot][i]):
                pivot = j

        if abs(a[pivot][i]) < eps:
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

    print(f"Размер: {rows} x {cols}")
    print(f"Минимум: {min(elements):g}")
    print(f"Максимум: {max(elements):g}")
    print(f"Сумма: {total:g}")
    print(f"Среднее: {total / len(elements):g}")
    print("Суммы строк:", row_sums)
    print("Суммы столбцов:", col_sums)


def is_square(matrix):
    return len(matrix) == len(matrix[0])


def get_matrix(matrices, name):
    if name not in matrices:
        print(f"Матрица {name} ещё не введена.")
        return None

    return matrices[name]


def main():
    matrices = {}

    while True:
        print("\n===== МАТРИЧНЫЙ КАЛЬКУЛЯТОР =====")
        print("1. Ввести матрицу")
        print("2. Вывести матрицу")
        print("3. Сложить две матрицы")
        print("4. Вычесть две матрицы")
        print("5. Умножить матрицу на число")
        print("6. Транспонировать матрицу")
        print("7. Умножить две матрицы")
        print("8. Найти определитель")
        print("9. Найти обратную матрицу")
        print("10. Вывести характеристики матрицы")
        print("0. Завершить программу")

        choice = input("\nВыберите пункт: ")

        if choice == "0":
            print("Программа завершена.")
            break

        elif choice == "1":
            name = input("Имя матрицы (A, B и т.д.): ").strip()

            if not name:
                print("Имя не может быть пустым.")
                continue

            matrices[name] = input_matrix()
            print("Матрица сохранена.")

        elif choice == "2":
            name = input("Имя матрицы: ").strip()
            a = get_matrix(matrices, name)

            if a is not None:
                print_matrix(a)

        elif choice in ("3", "4", "7"):
            name_a = input("Первая матрица: ").strip()
            name_b = input("Вторая матрица: ").strip()

            a = get_matrix(matrices, name_a)
            b = get_matrix(matrices, name_b)

            if a is None or b is None:
                continue

            if choice == "3":
                result = add_matrices(a, b)

            elif choice == "4":
                result = subtract_matrices(a, b)

            else:
                result = multiply_matrices(a, b)

            if result is None:
                print("Ошибка! Несовместимые размеры.")
            else:
                print("\nРезультат:")
                print_matrix(result)

        elif choice in ("5", "6", "8", "9", "10"):
            name = input("Имя матрицы: ").strip()
            a = get_matrix(matrices, name)

            if a is None:
                continue

            if choice == "5":
                try:
                    k = float(input("Введите число: "))
                    result = multiply_by_scalar(a, k)
                    print_matrix(result)

                except ValueError:
                    print("Ошибка! Введите число.")

            elif choice == "6":
                result = transpose(a)
                print_matrix(result)

            elif choice == "8":
                if not is_square(a):
                    print("Ошибка! Матрица не квадратная.")
                else:
                    print("Определитель:", determinant(a))

            elif choice == "9":
                if not is_square(a):
                    print("Ошибка! Матрица не квадратная.")
                else:
                    result = inverse_matrix(a)

                    if result is None:
                        print("Обратной матрицы не существует.")
                    else:
                        print_matrix(result)

            elif choice == "10":
                matrix_statistics(a)

        else:
            print("Ошибка! Такого пункта нет.")


if __name__ == "__main__":
    main()
