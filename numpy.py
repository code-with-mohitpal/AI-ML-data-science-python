import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# Array properties
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Dimension:", arr2.ndim)
print("Data Type:", arr2.dtype)
