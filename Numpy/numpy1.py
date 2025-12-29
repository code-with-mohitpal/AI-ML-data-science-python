# Import NumPy library
import numpy as np

# Create array from 1 to 12
arr = np.arange(1, 13)

# Reshape the array into 3 rows and 4 columns
matrix = arr.reshape(3, 4)

# Print results
print("Original Array:", arr)
print("Reshaped Matrix:\n", matrix)

# Create a 3x3 matrix
matrix = np.array([[2, 4, 6],
                   [1, 3, 5],
                   [7, 9, 11]])

# Print matrix
print("Matrix:\n", matrix)

# Calculate sum of each row
print("Row-wise Sum:", np.sum(matrix, axis=1))

# Calculate sum of each column
print("Column-wise Sum:", np.sum(matrix, axis=0))

# Create an array
arr = np.array([1, 4, 6, 8, 3, 10, 2])

# Apply condition to filter elements
filtered = arr[arr > 5]

# Print result
print("Elements greater than 5:", filtered)

# Create an array
arr = np.array([25, 10, 40, 5, 30])

# Sort the array
sorted_arr = np.sort(arr)

# Find index of maximum element
max_index = np.argmax(arr)

# Print results
print("Sorted Array:", sorted_arr)
print("Index of Maximum Element:", max_index)



# Create first matrix
A = np.array([[1, 2],
              [3, 4]])

# Create second matrix
B = np.array([[5, 6],
              [7, 8]])

# Perform matrix multiplication
result = np.dot(A, B)

# Print matrices and result
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Multiplication Result:\n", result)
