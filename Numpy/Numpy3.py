import numpy as np
print(np.__version__)
np.show_config()
arr = np.zeros(10)
print(arr)

arr = np.zeros(10)
print(arr.nbytes)

print(np.add.__doc__)

arr = np.zeros(10)
arr[4] = 1
print(arr)

arr = np.arange(10, 50)
print(arr)


arr = np.array([1,2,3,4,5,6,7,8])
reverse_arr = arr[::-1]
print(reverse_arr)


arr = np.arange(9).reshape(3,3)
print(arr)


arr = np.array([1,2,0,0,4,0])
print(np.nonzero(arr))


identity = np.eye(3)
print(identity)
