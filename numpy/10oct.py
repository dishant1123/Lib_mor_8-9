import numpy as np

"""arr=np.array([
    [31,7,45,12,28],
    [90,52,3,41,16],
    [8,27,64,5,39],
    [22,11,36,58,14],
    [49,2,18,33,71]
])

print(arr[-3 : ,-3 :])
"""
#fancy indexing : 
"""arr=np.array([
    [31,7,45,12,28],
    [90,52,3,41,16],
    [8,27,64,5,39],
    [22,11,36,58,14],
    [49,2,18,33,71]
])
"""

# task :1 print : [[31,52,64,58,71]]
"""
task :2 
print : [[12,28],
         [58,14],
         [33,71]]
"""
# print(arr[[0,1,2,3,4],[0,1,2,3,4]])  # answer  : task :1 
# print(arr[[0,3,4],3:5])

# reshape , np.zero ,np.one ,np.full ,np.eye ,np.identity : 

"""
arr = np.arange(1,11).reshape(5,2)
arr = np.arange(1,12,2).reshape(2,3)  # row  col 
arr = np.arange(1,33).reshape(4,4,2)
print(arr)
"""

# np.zero : 
arr1 =np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])
# arr=np.zeros(arr1.shape)
# arr=np.ones(arr1.shape)
# arr=np.full(arr1.shape,11)
# arr1[2:4] =99
arr1[2:4:2,: :-1] =100
print(arr1)
"""
[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

"""

# task  : 1 

"""
input  : 
[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
convert : np.zeros , using fancy indexing or  slicing  
output  : 
[
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,9,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]


"""
