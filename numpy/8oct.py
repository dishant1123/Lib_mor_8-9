import  numpy as np 
"""
arr =np.array([23,45,67,89,1,2,3,4,90])
print(arr)
print(arr.ndim)

arr1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,0]
],dtype=complex)
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1.itemsize)
print(arr1.dtype)
"""
# slicing  :  in 1d array  , 2d array  : 
"""
arr =np.array([23,45,67,89,1,2,3,4,90])
# positive  index :   l to  r  ------> start  0 
# neg  index :   r to  l  ------> start  -1
print(arr)
print(arr[2])
print(arr[-2])
print(arr[2:5])# start  : 2   end  : 5 
print(arr[ : 9])
print(arr[1: ])
print(arr[-9 : -2])
print(arr[2 : 8 :2]) # start  : 2   end  : 8   step  : 2
print(arr[0 : 7 :3]) # start  : 0   end  : 7   step  : 3
print(arr[-2 : -9  :-1])
"""

# slicing  : 2 d array  : 
arr = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])
print(arr)
print(arr.shape)
print(arr.size)
"""
1 row  -----> 1 2 3 4 5 ----> 0 
2 row  -----> 6 7 8 9 10 ----> 1 
3 row  -----> 11 12 13 14 15 ----> 2 
4 row  -----> 16 17 18 19 20 ----> 3 
5 row  -----> 21 22 23 24 25 ----> 4

1 col  ------> 1,6,11,16,21 ----> 0
2 col  ------> 2,7,12,17,22 ----> 1
3 col  ------> 3,8,13,18,23 ----> 2
4 col  ------> 4,9,14,19,24 ----> 3
5 col  ------> 5,10,15,20,25 ----> 4
"""
print(arr[2])  # 1 part : row  slice   2 part col 
print(arr[2:4])
print(arr[0:4:2])
print(arr[1:4,2:4])# row  : 1:4  col  :2:4 
