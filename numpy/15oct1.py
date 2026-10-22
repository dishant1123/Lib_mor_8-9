
"""l1 =[1,2,3,4,5]
l2 =l1 

l1[2] = "kanvi"

print(l1)
print(l2)
"""
# ===================================

"""l1 =[1,2,3,4,5]
l2 =l1.copy()

l1[-2] = "smit"

print(l1)
print(l2)
"""

import numpy  as np

"""arr =np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("original array :\n",arr)
print(arr.shape) # give a shape of  array  that is row and  column 
print(arr.ndim)  # number of  dimension
print(arr.size)  # total  number of  element in array 
print(arr.dtype)  # 
print(arr.itemsize)  # size of  each element

"""

"""arr = np.array([1,2,3,4,5,6,89.90]) 
print(arr)
print(arr.ndim)
print(arr.dtype)
"""

# reshape : 

"""
arr = np.array([1,2,3,4,5,6,7,8])
print(arr)
print(arr.reshape(2,4))

"""
"""
arr =np.arange(1,33).reshape(4,2,4)    # 
print(arr)
"""

# slicing : 
arr = np.array([11,12,13,14,15,16,17,18,19,20])

print(arr[0])
print(arr[3:6])
print(arr[2 :6 :2 ])  #start 2 stop 6   step  2 

print(arr[-2 : -6])

print(arr[-2 : -6 :-1 ])