# numpy  : fast , array  operation ,mulplication , vectorization,statistical analysis
"""
            numpy             vs  list 
1. store :  1 data type          multiple data type
2. speed     fast                slow
3. storage   low                 high
4. vecotor   possible            impossible 

ex : 

l1 =[[1,2,3],[4,5,6]]-------> [1,2,3,4,5,6]

pip install  numpy 
"""
import numpy as np
# create  array  : 

"""
arr = np.array([1,2,3,4,5,6,7,8,9])   #
print(arr)
"""
# multi ple  data type store in  array  : 

"""
arr1 =np.array([12,34,56,78,90.78,234]) 
print(arr1)
print(type(arr1))

arr2 =np.array([12,34,56,"heena","sanjay","sid",90.78,234])
print(arr2)
print(type(arr2))
"""
# 78+90j-----> 1.real:78   2.imaginary:90j

# 2d array : 
"""
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr)

arr1 = np.array([
    [
        [2,3],
        [4,5],
        [6,7]
    ]
])

print(arr1)
"""

# array  arrtributes : ndim,shape,dtype,size,itemsize

"""arr = np.array([[1.23,2,3],
                [4,5,6],
                [7,0,9]],dtype=bool)

print(arr)
print(arr.ndim)   #  number of dimension
print(arr.shape)  #  shape of array   row col  
print(arr.dtype)  #  data type
print(arr.size)   #  total number of elements
print(arr.itemsize)  #  size of each element

"""

# methods : arange 

arr =np.arange(1,10)
print(arr)
print(arr.ndim)

arr1 = np.arange(10,20,2)  # start 10  stop 20   step 2  
print(arr1)

arr2 = np.arange(-2 ,-20,-1)
print(arr2)

# -20 