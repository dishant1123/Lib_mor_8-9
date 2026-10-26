import numpy  as np

# shallow copy 
"""l1= [1,2,3,4,5,6]  # view  ----> memory  share 
#    0 1 2 3 4 5 

l2=l1 # l2 =[1,2,3,4,5,6]   l1 =[1,2,"heena",4,5,6]

l2[2] = "heena"

print(l1) 
print(l2)
"""
# ================================
# deep copy : 
"""
l1= [1,2,3,4,5,6]
l2=l1.copy()   # l2 =[1,2,3,4,5,6]

l2[-2] = "sanju_baba"

print("l1 :",l1) 
print("l2",l2)
"""

# flatten : converted any demensional array to 1-d array , same  as deep copy
"""
arr =np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
flattern_array =arr.flatten()

arr[1]=99
print("original array :\n",arr)
print("flattern_array :\n",flattern_array)
"""
# ravel :  memory  share -----> same as shallow copy
"""
arr =np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
ravel_array =arr.ravel()

arr[1]=99

print("original array :\n",arr)
print("ravel_array :\n",ravel_array)

"""

# sum , min ,max ,sorted :
arr =np.array([
    [11,2,23],
    [4,-5,6],
    [7,38,-9]
])
print("sum :",np.sum(arr))
print("col sum :",arr.sum(axis =0))  # col wise sum 
print("row sum :",arr.sum(axis =1))  # row wise sum

print("min :",arr.min())
print("col min :",arr.min(axis =0))  # col wise min
print("row min :",arr.min(axis =1))  # row wise min

print("arg min :",arr.argmin())  # return index number of min element 
print("arg min :",arr.argmin(axis =0))  # col wise argmin
print("arg min :",arr.argmin(axis =1))  # row wise argmin

print("max :",arr.max())
print("col max :",arr.max(axis =0))  # col wise max
print("row max :",arr.max(axis =1))  # row wise max

print("arg max :",arr.argmax())  # return index number of max element 
print("arg max :",arr.argmax(axis =0))  # col wise argmax
print("arg max :",arr.argmax(axis =1))  # row wise argmax



