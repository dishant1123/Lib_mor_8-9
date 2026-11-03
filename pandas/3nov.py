import pandas as pd
import  numpy as np

# string operation  : 

import pandas as pd

"""df = pd.DataFrame({
    'Name': ['John Smith', 'Alice Brown', 'David Miller', 'Emma Wilson'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Email': [
        'john@gmail.com',
        'alice@yahoo.com',
        'david@outlook.com',
        'emma@gmail.com'
    ]
})
"""
# print(df)

#string function  : upper ,title and  lower  

"""
df['Name'] =df['Name'].str.lower()
df['City_upper'] =df['City'].str.upper()
df['email_title']=df['Email'].str.title()
print(df)
"""
# replace  :
"""
df['new_email'] =df['Email'].str.replace('gmail','yahoo')
print(df)
"""

# split : 
"""
df['first_name'] = df['Name'].str.split().str[0]
df['last_name'] = df['Name'].str.split().str[1]
print(df)
"""

# map  : 

"""
df = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'name': ["heena","chirag","sanju","sid","chaitali"],
    'marks' : [99,80,88,34,89],
    'gender': ["female","male","male","male","female"]
})

print("original : \n",df)

df['gender'] =df["gender"].map({"male":1,"female":0})
print("after  using map : \n",df)
"""
# group by  : 

import pandas as pd

data = {
    'Employee': ['John', 'Alice', 'Bob', 'Emma', 'David', 'Sophia', 'James', 'Olivia'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 45000, 60000, 55000, 48000, 62000, 70000, 52000],
    'Experience': [2, 3, 5, 4, 2, 6, 8, 3]
}

df = pd.DataFrame(data)

print(df) 

# group by  : 

"""
total_salary_Depat_wise = df.groupby('Department')['Salary'].sum()
print("total salary of IT department :\n",total_salary_Depat_wise)
"""
# count  : 
"""
total_count_Depat_wise = df.groupby('Department')['Salary'].count()
print("total count of each department :\n",total_count_Depat_wise)
"""

# min  salary  depart_wise , max depart_wise , mean depart_wise   ,count depart_wise  : .agg()

group_by_depat =df.groupby('Department')['Salary'].agg(['min','max','mean','count']) 
print("min ,max ,mean ,count depart_wise :\n",group_by_depat)

# tasks : 
"""
using sample_superstore dataset  :

1. find the  total sales category wise . 
2. findout the  top  3 sub-category highest sales. 
3. findout the  bottom  3 sub-category lowest profit. 
4. findout the  top 5 customer name  who earn highest profit .

"""


