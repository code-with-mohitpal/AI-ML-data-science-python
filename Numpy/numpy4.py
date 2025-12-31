import numpy as np

arr = np.random.random((3, 3, 3))
print(arr)

arr = np.ones((3, 3))
bordered = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
print(bordered)



import numpy as np

print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)


mat = np.zeros((5, 5))
np.fill_diagonal(mat[1:], [1, 2, 3, 4])
print(mat)


checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
print(checkerboard)


shape = (6, 7, 8)
index = np.unravel_index(99, shape)
print(index)


pattern = np.array([[0, 1],
                    [1, 0]])

checkerboard = np.tile(pattern, (4, 4))
print(checkerboard)


mat = np.random.random((5, 5))
normalized = (mat - mat.min()) / (mat.max() - mat.min())
print(normalized)


color_dtype = np.dtype([
    ('R', np.uint8),
    ('G', np.uint8),
    ('B', np.uint8),
    ('A', np.uint8)
])

color = np.array((255, 100, 50, 255), dtype=color_dtype)
print(color)


A = np.random.random((5, 3))
B = np.random.random((3, 2))

result = A @ B
print(result)


arr = np.array([1, 4, 6, 9, 2, 7, 10])
arr[(arr > 3) & (arr < 8)] *= -1
print(arr)
