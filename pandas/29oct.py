import pandas as pd 
import numpy as np

"""
df = pd.DataFrame({
    "id" : [np.nan,np.nan,np.nan,4,5],
    "name" : ["heena",np.nan,"chirag","sanju","sid"], 
    "marks" : [99,89,88,99,np.nan],
    "city":[np.nan,"mumbai",np.nan,"chennai",np.nan]
    
})
print(df)
"""
# dropna :
"""
result = df.dropna()  # remove  all rows  which  have  any  missing  values defult axis =0 
result = df.dropna(axis=1)  # remove  all col  which  have  any  missing  values 
result =df.dropna(subset=["name","marks"])  # remove  all rows  which  have  any  missing  values in name and marks col
result = df.dropna(how="all",axis=1)  # remove  all rows  which  have  all  missing  values
result =df.dropna(thresh=3,axis=1)  # remove  all rows  which  have  any  missing  values  atleast 3 non missing values  in col
print(result)
"""

# drop_duplicates : 

# fillna : 

"""df =pd.DataFrame({
    'id':[1,2,3,4,5],
    'age' :[np.nan,24,25,np.nan,27],
    'salary' :[12000,15000,np.nan,20000,np.nan]
})

print(df)
"""
# fillna :

# result =df.fillna(0)
# print(result)

"""df['age'] =df['age'].fillna(df['age'].mean()).astype(int)
df['salary'] =df['salary'].fillna(df['salary'].mean())
print(df)
"""
"""
1. csv ,tsv ,json ,excel ,sql
2. seris : one demensional  data  structure ,  homogenous  data  type , index  based
3. head ,tail ,info ,describe ,shape ,columns ,index  -----> attributes
4. Dataframe :  two demensional  data  structure , heterogenous  data  type , index based
    2 method : 1. dict , 2. list of list 
    
5. loc ,iloc  
6. isnull -----> null print  true  ----> False
7. missing value  count  : isnull().sum() 
8. drop  : DF  ----> remove  ----> axis =0 row wise , axis =1 col wise
   dropna : missing value  remove  ----> default  axis =0  row wise , axis =1 col wise
            subset ----> particular  col  missing value  remove 
            thresh  ---> minimum  non missing value  in col  or row
            how ----> all  ----> all value are  null then only  remove     
   fillna : missing value  fill  
9.inplace : True  ----> original  df  change , False  ----> original  df  not change 

"""

# sort_values : 

df= pd.DataFrame({
    "id" : [1,2,3,4,5],
    "name" : ["heena","chirag","sanju","sid","chirag"],
    "marks" : [99,80,88,34,89],
    "city" : ["pune","mumbai","chennai","pune","mumbai"]
})

print(df)

# sort by  marks  col  in ascending order :
# sort_by_marks = df.sort_values(by="marks",ascending=True)  # asc to desc by default 
sort_by_marks = df.sort_values(by="marks",ascending=False)  # desc to asc 

print(sort_by_marks)
