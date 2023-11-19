def sum_of_columns(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    if num_rows == 0 or num_cols == 0:
        return "Матрица пустая"

    column_sums = [0] * num_cols

    for col in range (num_cols):
        has_negative = False

        for row in range(num_rows):
            if matrix[row][col] < 0:
                has_negative = True
                break

        if not has_negative:
            column_sums[col] = sum(matrix[row][col] for row in range(num_rows))

    return sum(column_sums)

matrix = [
    [1, 2, 3],
    [4, -5, 6],
    [7, 8, 9]
]

result = sum_of_columns(matrix)
print(f"Сумма элементов в столбцах без отрицательных элементов: {result}")
