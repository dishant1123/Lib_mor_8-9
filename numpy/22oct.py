import numpy as np
# stack  : vstack , hstack ,dstack 

# arr = np.array([[1,2,3],
                # [4,5,6]])
# arr =np.array([1,2,3,4,5,6])

# arr =np.array([
#     [
#         [1,2,3],
#         [4,5,6]
#     ]
# ])
# arr1 =np.array([1,2,3])
# arr2 =np.array([4,5,6])
"""
arr1 =np.array([
    [1,2,3],
    [4,5,6]
])

arr2 =np.array([
    [7,8,9],
    [10,11,12]
])

print("original : \n",arr1)
print("original : \n",arr2)

# result = np.vstack(arr)
# result = np.hstack(arr)

result = np.dstack((arr1,arr2))
print(result)
"""

# split , array_split : 

"""
arr = np.array([1,2,3,4,5,6])
result =np.split(arr,3)

arr2 =np.array([7,8,9,10,11])
result2 =np.split(arr2,2)

print(result)
print(result2)  # error : bcz of  total array element  is  odd number so  split is not  possible 
"""

# array_split :
"""
arr2 =np.array([7,8,9,10,11,33,55])
result2 =np.array_split(arr2,4)
print(result2)
"""
# insert , append , delete : 
"""
arr2 =np.array([7,8,9,10,11,33,55])

print(arr2)
print(np.append(arr2,89))
print(np.insert(arr2,6,900))   # ------> insert 
arr2[-2] =333  # ------> update 
print(np.delete(arr2,2))  # ----> index wise  delete
print(np.delete(arr2))  # ------> error : its compulsory to give arg / index
print(arr2)
"""

# power ,sqrt , floor ,ceil ,round ,unique ,where 

arr = np.array([1,2,3,4,5,6,7,9])

print(arr)
# print(np.power(arr,2))
# print(np.sqrt(arr))
# print(np.floor(arr))
# print(np.ceil(arr))
# print(np.round(arr))
# print(np.unique(arr))

print(np.where(arr>3))

# np.loadtxt , np.genfromtxt  -----> 