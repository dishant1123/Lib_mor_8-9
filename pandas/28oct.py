import  pandas as pd 
import numpy as np 

# loc ,iloc : 

df = pd.read_csv("pandas/mckinsey.csv")
# print(df.head())

# loc : label  based ,row ----> number  ,col  ------> col_name 
"""
result = df.loc[2:5]  # both  index included in loc 
result = df.loc[2 :10 :2]  # start   : 2  end  10  step :2 
result = df.loc[2:5,"population" :"gdp_cap"]
result = df.loc[2:5,["country","gdp_cap"]]

print(result)
"""
# iloc :  index based 

"""result = df.iloc[2:5]  # last index excluded 
result = df.iloc[2:10 :2]  # last index excluded 
result = df.iloc[2:10,1:4]  # 2:10 row  slicing , 1:4 col  slicing
result = df.iloc[2:10:3,0:5:2]
print(result)
"""

# task : 1 
"""
print data  only when  country ==india , and  life_exp >60   and  print  only country  and life_exp. 
hint  : loc or iloc , & , |  

"""
"""
result = df.loc[(df['country'] =="India") & (df['life_exp'] >60)] [['country','life_exp']] 
print(result)
"""

# isnull : 
"""df = pd.DataFrame({
    "id" : [1,2,3,np.nan,5],
    "name" : ["heena",np.nan,"chirag","sanju","sid"], 
    "marks" : [np.nan,89,88,99,np.nan],
    "city":["pune","mumbai",np.nan,"chennai",np.nan]
    
})
print(df)
"""
"""
result = df.isnull()
print(result)
"""
# count the  missing  values : 
"""
result = df.isnull().sum()
print(result)
"""

# drop : 
"""result = df.drop(columns="id") 
result = df.drop(columns ='name',axis=1)  # axis =1 col wise remove 
result = df.drop(index=3,axis=0)  # axis =0 row wise remove  ----> index 

print(result)
"""