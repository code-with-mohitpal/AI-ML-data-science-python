import numpy as np

zeros_array = np.zeros((2, 3))
ones_array = np.ones((3, 3))
constant_array = np.full((2, 2), 7)
range_array = np.arange(0, 10, 2)  # start, stop, step
linspace_array = np.linspace(0, 1, 5)  # start, stop, num

print("Zero Array:","\n",zeros_array)
print("Ones Array:","\n",ones_array)
print("Constant Array:","\n",constant_array)
print("Range Array:","\n",range_array)
print("Linspace Array:","\n",linspace_array)