import numpy as np

# loadtxt : 
"""
1. read only  clean data  from  csv  file
2. not handle the missing value
"""

# ex :1 
"""arr = np.loadtxt("numpy/student.csv",
                 delimiter=",",
                 skiprows=1,dtype=int)
print(arr)

# findout the  mean  of  salary  : 
mean_salary  = np.mean(arr[:,2])
print(mean_salary)
"""

# ex :2 genfromtxt :

"""arr =np.genfromtxt("numpy/student1.csv",
                  delimiter=",",
                  skip_header=1,
                  dtype=None ,
                  filling_values=0
                   )
print(arr)
"""

# np.nan : 
"""arr=np.array([1,2,3,4,np.nan,6,7,8,np.nan])
print(np.isnan(arr))
print(np.isnan(arr).sum())
print(arr)
"""

# boardcasting :
"""
when  possible : 
    1. both shape are same  
    2. 1st array col and 2nd array row are same 
    3. any array have  1 demention then also  possible
    
not  possible :
    1. shape  is  not  match. 
"""



# ex :1 
"""arr = np.array([1,2,3,4,5,6,7,8,9])
arr2 = arr**2

print(arr)
print(arr2)
print("shape of arr is  : ",arr.shape)
print("shape of arr2 is  : ",arr2.shape)
"""

# ex :2  shape  is not  match so  boardcasting  is  not  possible.


"""arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

arr1 =np.array([1,2,3,4,5,6,7,8,9])
result = arr1*arr2
print(arr2)
print("result is :",result)

"""
# ex :3

"""arr1 =np.array([[11,12,13],
                [5,6,7]])

arr2 =np.array([1,2,3]) 

result = arr1 +arr2
print(arr1.shape)
print(arr2.shape)
print(result)
"""