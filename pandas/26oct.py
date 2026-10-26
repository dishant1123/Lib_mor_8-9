#pip install pandas

import pandas as pd
import numpy as np

"""
use : 

1. cleaning  
2. data analysis
3. data  manupulation
4. EDA report  : exploratory data analysis ----> yprofiling 


1. seris 
2. dataframe
"""

"""s1 =pd.Series([12,24,35,4,5,6,7,8,9,10])
print(s1)

s2  =pd.Series([12,24,35,"badal",5,6,7,8,9.90,10])
print(s2)
print(s2.dtypes)

s3 = pd.Series([90,89,88,99,91],index=["heena","badal","chirag","sanju","sid"])
print(s3)

s4 =pd.Series({"heena":90,"badal":89,"chirag":88,"sanju":99,"sid":91})
s4['sanju'] =67
print(s4) 
"""
# head ,tail ,info ,describe ,describe_all
"""
s1 = pd.Series([12,24,35,4,5,6,7,np.nan,9,10])

print(s1)
print(s1.head(2))  # by default it shows first 5 rows
print(s1.tail(3))  # by default it shows last 5 rows
print(s1.info()) # shows info about the series
print(s1.describe()) # shows summary statistics
print(s1.shape) # shows shape of the series
print(s1.dtypes) # shows data type of the series

"""

# read csv ,tsv ,json ,excel : 

# csv :
"""
df = pd.read_csv("pandas/student_batch.csv")
print(df)
print(df.head(2))
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.shape)
print(df.describe(include='all'))

"""

# tsv : tab separated values

"""
df =pd.read_csv("pandas/student.tsv",sep="\t")
print(df)
"""

# excel : 

"""
df =pd.read_excel("pandas/numpy_dataset.xlsx")
print(df)
"""

# json :

df =pd.read_json("pandas/student.json")
print(df)


# next session  : SQL read , dataframe 