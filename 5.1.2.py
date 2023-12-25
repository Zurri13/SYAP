import numpy as np

X_col1 = np.ones(12)
X_col2 = np.random.randint(16, 28, size=12)
X_col3 = np.random.randint(60, 83, size=12)
X = np.column_stack((X_col1, X_col2, X_col3))

Y = np.random.randint(13.5, 18.6, size=12).reshape(-1, 1)
print("Y: ")
print(Y)

# A = (X^T * X)^(-1) * X^T * Y
A = np.linalg.inv(X.T @ X) @ (X.T @ Y)

Y_p = X@A

print("Вектор оценок от матрицы A:")
print(A)

print("\n Полученные значения Y:")
print(Y_p)
