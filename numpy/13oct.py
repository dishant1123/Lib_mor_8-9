import numpy  as np  
import random 
from scipy import stats as st
# identity  matrix : 

arr = np.identity(4)
arr =np.eye(4,dtype=int)
print(arr)


# transpose :
"""
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("original array :\n",arr)

tran = arr.T
tran =arr.transpose()
print("transpose :\n",tran)
"""

# random  : 
"""np.random.seed(90)

arr = np.random.random((4,3))  # 0-1 
arr = np.random.randint(low =-10 ,high =10 ,size =12).reshape(3,4)
arr = np.random.randint(low =-10 ,high =10 ,size =(4,3))
arr =np.random.choice(range(20),size =(4,3))
arr =np.random.choice(["heena","badal","sid","sanju","chirag","pratibha"],size =(3,3))
print(arr)
"""

# statistics :

"""
arr =np.array([11,2,3,43,5,65,7,8,90,10])
print("mean :",np.mean(arr))# 24.4
print("median :",np.median(arr))  # center 

print("variance  : ",np.var(arr)) 
print("std dev  : ",np.std(arr))
"""
# asc to desc : 2,3,5,7,8,10,11,43,65,90  ----> n1 +n2 /2  ----> 10 +8  /2 ===> 9
#   odd elements  : 2 3 5 7 8 10 11 43 65 ----> median  ---->8
"""
mode : 
10   ----> 3 ----> 0
2    ----> 2 ----> 1
3    ----> 2 ---->2 
"""
# print("mode is  : ",st.mode(arr)[0])

# matrix : addition  , subtraction , multiplication , division , dot product  

"""a= np.array([
    [1,12,3],
    [14,5,16],
    [12,45,67]
])
b= np.array([
    [11,12,13],
    [14,15,16],
    [17,18,19]
])
print("a array :\n",a)
print("b array :\n",b)

print("addition :\n",a+b)
print("subtraction :\n",a-b)
print("multiplication :\n",a*b)  # not  matrix multiplication
print("division :\n",a/b)
print("mod :\n",a%b)
print("floor division :\n",a//b)
"""
# matrix multiplication : matmul , dot , @ 
"""
a= np.array([
    [11,12],
    [14,15],
])

b= np.array([
    [4,5],
    [6,7],
])

print("matrix multiplication :\n",a@b)
print("dot product :\n",np.dot(a,b))
print("matmul :\n",np.matmul(a,b))


"""