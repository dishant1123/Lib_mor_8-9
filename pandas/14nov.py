#pivort in  pandas : 

import  pandas as pd 
"""
df = pd.read_csv("pandas/sample_superstore1 copy.csv")
print(df.head())
"""
# total sales  for all  category : furni , ofc supp ,techo

"""summary_table = pd.pivot_table(
    data =df,
    values="Sales",
    index="Category",
    aggfunc='sum'
   
)
print("total category  sales : \n ",summary_table)
"""
# total sales  for all  sub-category : 
"""
summary_table_all_sub_cat = pd.pivot_table(
    data =df,
    values="Sales",
    index="Sub-Category",
    aggfunc='sum'
   
)
print("total category  sales : \n ",summary_table_all_sub_cat)
"""

# join  : 

import pandas as pd
"""
df_emp = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 104, 105],
    'Name': ['John', 'Alice', 'Bob', 'David', 'Eva']
})

df_dept = pd.DataFrame({
    'Emp_ID': [101, 102, 104, 106],
    'Department': ['HR', 'IT', 'Finance', 'Marketing']
})

df_salary = pd.DataFrame({
    'Emp_ID': [101, 103, 104, 105, 107],
    'Salary': [50000, 60000, 55000, 65000, 70000]
})

df_location = pd.DataFrame({
    'Emp_ID': [102, 103, 105, 108],
    'Location': ['Ahmedabad', 'Mumbai', 'Delhi', 'Pune']
})

print("Employees\n", df_emp)
print("\nDepartments\n", df_dept)
print("\nSalaries\n", df_salary)
print("\nLocations\n", df_location)
"""
"""
1. inner : when two table  have  one common column.
2. right : right  side all  row  and  left side only  matching row print 
3. left  : left  side all  row  and  right  side only  matching row print 
4. outer : 

"""
# inner  join  for  two  table  : employees , department 

"""result = pd.merge(
    df_emp,
    df_dept,
    how='inner'
)
print("inner  join : \n",result)
"""

# left  and  right  join  two tables : salary  , locations 

"""
result = pd.merge(
    df_salary,
    df_location,
    how='left'
)
print("left join  : \n", result)  # salary  ----> left --->all rows  locations ----> right ----> matching  
"""

"""
result = pd.merge(
    df_salary,
    df_location,
    how='right'
)
print("right join  : \n", result)  # locations ----> right ----> all rows  salary  ----> left --->matching rows  
"""
"""
task : 
1. movies 
2. directors 
 this  two  table  join  using  director_id , id don't rename  the  col  
 
 hint  : right_on ,left_on 
"""

movies = pd.read_csv("pandas/movies.csv")
directors = pd.read_csv("pandas/directors.csv")

print(movies.head())
print(directors.head())

