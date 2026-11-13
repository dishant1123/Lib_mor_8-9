import  pandas as pd 
import  numpy as np 

data = {
    'Emp_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
               111, 112, 113, 114, 115],

    'Emp_Name': ['Rahul', 'Priya', 'Amit', 'Neha', 'Karan',
                 'Pooja', 'Vishal', 'Riya', 'Sahil', 'Anjali',
                 'Meet', 'Kavya', 'Jay', 'Nisha', 'Rohan'],

    'Department': ['IT', 'HR', 'Finance', 'IT', 'Sales',
                   'HR', 'IT', 'Finance', 'Sales', 'IT',
                   'HR', 'Sales', 'Finance', 'IT', 'HR'],

    'Joining_Date': [
        '15-01-2022', '20-03-2021', '10-06-2023',
        '25-12-2020', '05-08-2022', '12-04-2021',
        '18-09-2023', '30-11-2020', '22-02-2022',
        '14-07-2021', '01-01-2024', '19-05-2023',
        '27-10-2022', '08-03-2024', '16-06-2020'
    ],

    'Salary': [35000, 42000, 50000, 38000, 45000,
               40000, 55000, 48000, 32000, 52000,
               30000, 46000, 58000, 41000, 39000]
}

df = pd.DataFrame(data)

df['Joining_Date'] = pd.to_datetime(df['Joining_Date'],format='%d-%m-%Y')
df['Month']=df['Joining_Date'].dt.month 
df['Year']=df['Joining_Date'].dt.year
df['Day']=df['Joining_Date'].dt.day

# print(df)

"""
Que :1 
count 2022 ----> hire   ----> count  4 
total salary -----> 170000  
group  by 
"""
# ans : 
"""
result = df.groupby('Year').agg(
    total_emp =('Emp_ID','count'),
    total_salary=('Salary','sum')
)
print(result)
"""
# using loc  print  only detalis year =2022 and  total salary. 

"""
que :2 
how  much days employees stay  in  our company (till the date )
"""
# ans : 

today_date =pd.Timestamp.today().normalize()  # 13-11-2026
df['total_days'] =(today_date - df['Joining_Date']).dt.days
print(df)