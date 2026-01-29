import numpy as np

identity_matrix = np.eye(3)
diagonal_array = np.diag([1, 2, 3])
zeros_like_array = np.zeros_like(diagonal_array)
ones_like_array = np.ones_like(diagonal_array)

print(identity_matrix)
print(diagonal_array)
print(zeros_like_array)
print(ones_like_array)