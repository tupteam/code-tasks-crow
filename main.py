def validate_matrix(matrix: list[list[int]]) -> None:
    """
    Проверяет корректность входной матрицы.

    :param matrix: матрица для проверки.
    :raises Exception: если матрица не соответствует требованиям.
    """
    if matrix is None:
        raise Exception("Параметр не является трехдиагональной матрицей")

    # Проверка, что матрица является списком и не пустая
    if not isinstance(matrix, list) or len(matrix) < 1:
        raise Exception("Параметр не является трехдиагональной матрицей")

    row_first_len = len(matrix[0])
    # Проверка строк
    for row in matrix:
        if not isinstance(row, list) or len(row) != row_first_len:
            raise Exception("Параметр не является трехдиагональной матрицей")
        for item in row:
            if not isinstance(item, int):
                raise Exception("Параметр не является трехдиагональной матрицей")

    # Проверка, что матрица квадратная
    if len(matrix) != row_first_len:
        raise Exception("Параметр не является трехдиагональной матрицей")

    # Проверка на трехдиагональность
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise Exception("Параметр не является трехдиагональной матрицей")
                # Проверка элементов на верхней диагонали (элементы на позиции i, j при j = i + 1)

    # Проверка одинаковости значений на главной диагонали
    for i in range(1, len(matrix)):
        if matrix[i][i] != matrix[0][0]:
            raise Exception("Параметр не является трехдиагональной матрицей")

    # Проверка диагонали
    if len(matrix) > 1:
        # Проверка одинаковости значений на верхней диагонали
        for i in range(len(matrix) - 1):
            if matrix[i][i + 1] != matrix[0][1]:
                raise Exception("Параметр не является трехдиагональной матрицей")

        # Проверка одинаковости значений на нижней диагонали
        for i in range(len(matrix) - 1):
            if matrix[i + 1][i] != matrix[1][0]:
                raise Exception("Параметр не является трехдиагональной матрицей")

def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    validate_matrix(matrix)

    order = len(matrix)

    if order == 1:
        return matrix[0][0]

    if order == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det_prev2 = matrix[0][0]
    det_prev1 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    for i in range(2, order):
        a = matrix[i][i]
        b = matrix[i][i - 1]
        c = matrix[i - 1][i]
        det_current = a * det_prev1 - b * c * det_prev2
        det_prev2, det_prev1 = det_prev1, det_current

    return det_prev1



def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    if matrix is not None:
        print("Трехдиагональная матрица")
        for row in matrix:
            print(row)


    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
