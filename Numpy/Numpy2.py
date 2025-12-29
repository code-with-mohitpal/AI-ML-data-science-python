# performance comparison
import numpy as np
import time
size=10000000
# python list
python_list=list(range(size))
start=time.time()
list_squared=[x**2 for x in python_list]
end=time.time()
print("python list time:",end-start,"seconds")

# Numpy arrays
np_array=np.array(python_list)
start=time.time()
array_squared=np_array**2
end=time.time()
print("Numpy array time:",end-start,"second")

# Memory usage Comparison
import sys
print("python list size:",sys.getsizeof(python_list)*len(python_list))
print("Numpy array size:",np_array.nbytes)

# creating numpy array from list
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr)
print(type(arr))
print(arr.shape)

arr2=np.array([1,2,3,4,5,"prime",3.14])
print(arr2,type(arr2),arr2.shape)

# 2D array-matrix
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3)
print(type(arr3))
print(arr3.shape)

#  create using build-in methods
arr1=np.zeros((3,4),dtype="int64")  #prefill
print(arr1)
print(arr1.shape)

arr2=np.ones((4,5))
print(arr2)
print(arr2.shape)

arr3=np.full((4,5),100)  #prefill with val
print(arr3,arr3.shape)

arr4=np.eye(4)  #identity matrix
print(arr4,arr4.shape)

arr5=np.arange(0,11,2)  #range elements
print(arr5,arr5.shape)

arr6=np.linspace(1,100,4)  #evenly spaced arrays
print(arr6,arr6.shape)

# Reshaping array 
arr=np.array([[1,2,3],[4,5,6]])
print(arr,arr.shape)
reshaped=arr.reshape((3,2))
print(reshaped,reshaped.shape)
