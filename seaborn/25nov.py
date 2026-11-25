import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

"""df=pd.read_csv("pandas/sample_superstore.csv")

df['Order Date'] =pd.to_datetime(df['Order Date']) 
df['Month']= df['Order Date'].dt.to_period('M')
month_wise =df.groupby('Month')['Sales'].sum() 
# print(month_wise)
# print(month_wise.index)
# print(month_wise.values)

sns.set_theme(style="darkgrid")
sns.lineplot(
             x=month_wise.index.astype(str),
             y=month_wise.values,
             linestyle="--",
             linewidth=3,
             marker='o'
             )
plt.title("sales vs  date")
plt.show()  
"""

# bar plot  : 
"""import pandas as pd

data = {
    'City': ['Ahmedabad', 'Mumbai', 'Delhi', 'Jaipur', 'Pune',
             'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Surat'],
    'Temperature': [38, 32, 35, 40, 30, 36, 27, 34, 33, 37],
    'Season': ['Summer', 'Summer', 'Summer', 'Summer',
               'Winter', 'Winter', 'Winter', 'Winter' ,"Monsoon", "Monsoon"]   
}
df = pd.DataFrame(data)
print(df)

bars =sns.barplot(
    x='City',
    y='Temperature',
    data=df,
    palette='coolwarm',
    hue='Season'
    
)
# bars.bar_label(bars.containers[3])  # for loop  
plt.show()
"""

# count plot  : 

"""import pandas as pd

data = {
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR',
                   'IT', 'Sales', 'Finance', 'IT', 'HR',
                   'Finance', 'Sales', 'IT', 'HR', 'Sales'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female',
               'Male', 'Female', 'Male', 'Male', 'Female'],
    'Status': ['Active', 'Active', 'Inactive', 'Active', 'Active',
               'Active', 'Inactive', 'Active', 'Active', 'Inactive',
               'Active', 'Active', 'Inactive', 'Active', 'Active']
}
df = pd.DataFrame(data)
print(df)

bars=sns.countplot(
    x='Department',
    hue='Gender',
    data=df,
    palette='Set2'
)
for i in bars.containers:
    bars.bar_label(i)
plt.show()
"""
# box plot : 
import pandas as pd

data = {
    'Department': ['IT', 'HR', 'Sales', 'IT', 'HR',
                   'Sales', 'IT', 'HR', 'Sales', 'IT',
                   'HR', 'Sales', 'IT', 'HR', 'Sales'],
    'Salary': [8000, 30000, 35000, 55000, 32000,
               40000, 60000, 35000, 42000, 70000,
               38000, 45000, 80000, 40000, 150000],
    'Experience': [2, 1, 3, 5, 2, 4, 7, 3, 5, 8,
                   4, 6, 10, 5, 7],
    'Gender': ['Male', 'Female', 'Male', 'Male', 'Female',
               'Female', 'Male', 'Female', 'Male', 'Male',
               'Female', 'Female', 'Male', 'Female', 'Male']
}
df = pd.DataFrame(data)
print(df)

"""
sns.boxplot(
    x='Department',
    y='Salary',
    data=df,
    palette='Set2'
)
plt.show()
"""
# violin plot :

"""sns.violinplot(
    x='Department',
    y='Salary',
    data=df,
    palette='Set2'
    
)
plt.show()
"""

# swarmplot : 
"""
sns.swarmplot(
    x='Department',
    y='Salary',
    data=df,
    palette='rocket',
    hue='Gender'
    
)
plt.show()
"""

# pointplot :
sns.pointplot(
    x='Department',
    y='Salary',
    data=df,
    palette='deep',
    hue='Gender'
    
)
plt.show()
