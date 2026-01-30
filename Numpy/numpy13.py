import numpy as np
 
# First Array
arr1 = np.array([[4, 7], [2, 6]], 
                 dtype = np.float64)
                  
# Second Array
arr2 = np.array([[3, 6], [2, 8]], 
                 dtype = np.float64) 
 
# Addition of two Arrays
Sum = np.add(arr1, arr2)
print(Sum)
 
# Addition of all Array elements
Sum1 = np.sum(arr1)
print(Sum1)
 
# Square root of Array
Sqrt = np.sqrt(arr1)
print(Sqrt)
 
# Transpose of Array
Trans_arr = arr1.T
print(Trans_arr)
