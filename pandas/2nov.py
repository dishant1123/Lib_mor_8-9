import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#sort_index :    

"""df= pd.DataFrame({
    "id" : [1,2,3,4,5],
    "name" : ["heena","chirag","sanju","sid","chirayu"],
    "marks" : [99,80,88,34,89],
    "city" : ["pune","mumbai","chennai","pune","mumbai"]
})

print("original Dataframe :\n",df)  
"""
"""
result =df.sort_index(ascending=False)  # sort by marks col in descending order
print(result)
"""
# reindex :
"""
result= df.sort_values(by="marks",ascending=False)  # sort by marks col in descending order
print("sort :\n",result)

df =df.reindex([0,1,2,3,4])

"""
# outlier : 

#example :

"""
days   sales (clothes)

1      200
2      300
3      250
4      350
5      150 
6      400 
7      550 
8      600
9      15000  

avg sales  = 1977 -----> 
day 1 to  8  avg sales  = 350


outlier  : 2 method 

1. IQR : inter quartile range 
2. Z score :  (x-mean)/std  ---->  if  z score  >3  then  outlier 


IQR = Q3-Q1  
Q3 = 0.75 * sales
Q1 = 0.25 * sales 

lower limit  = Q1-1.5*IQR
upper limit  = Q3+1.5*IQR
 
"""

# df = pd.DataFrame({
#     'days' : [1,2,3,4,5,6,7,8,9],
#     'sales' : [20000,300,250,350,150,400,550,600,150]
# })
# print(df)
# 
# outlier  detection  using  IQR  method :
"""
Q3 = df['sales'].quantile(0.75)
Q1 = df['sales'].quantile(0.25)

IQR = Q3-Q1
print("IQR : ",IQR)

lower_limit = Q1-1.5*IQR   # q1 = 250   q3 =550  iqr =300  
upper_limit = Q3+1.5*IQR

print("lower limit : ",lower_limit)  # -200
print("upper limit : ",upper_limit)   # 1000 

# outlier :
print("outlier :\n",df[(df['sales']<lower_limit) | (df['sales']>upper_limit)])  # 15000
"""
# graph : box plot  :

"""
plt.boxplot(df['sales'])
plt.title("box plot")
plt.show()
"""

#z-score 

"""from scipy import stats 

z_score = stats.zscore(df['sales'])
print("z score :\n",z_score)
print("outlier :\n",df[(z_score>2.5) | (z_score<-2.5)])  # 15000
"""
# cilp ,winsorize :
