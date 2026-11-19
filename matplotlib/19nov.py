import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

# trend  line  : 

"""
df = pd.read_csv("pandas/sample_superstore1 copy.csv")

X =np.arange(len(df))
print(X)

# linear regression  : y = m x +c 
slope,intercept = np.polyfit(X,df['Sales'],1)
trend = slope * X + intercept

# order_date  convert in to  datetime format  : 

df['Order Date']=pd.to_datetime(df['Order Date'])
df['Month']=df['Order Date'].dt.month

# graph : 
plt.plot(
    df['Month'],
    df['Sales'],
    color='red',
    label='Sales',
    linewidth=2
)
plt.plot(
    df['Month'],
    trend,
    color='blue',
    label='trend',
    linewidth=2
)
plt.title(" line trend line")
plt.xlabel("Sales")
plt.ylabel("Month")
plt.legend()
plt.grid()
plt.show()
"""
"""
exp_yrs  salary 
0        25000 
1        30000
2        38000
3        45000
4        50000 


"""
month = [1,2,3,4,5,6,7,8,9,10,11,12]
sales = [100,150,200,90,350,450,560,400,800,650,790,1200] 

x=np.arange(len(month))

# linear regression  : y = m x +c
slope,intercept = np.polyfit(x,sales,1)
trend = slope * x + intercept

# graph : 
"""
plt.plot(
    month,
    sales,
    color='red',
    label='Sales',
    linewidth=2
)
plt.plot(
    month,
    trend,
    color='blue',
    label='trend',
    linewidth=2
)
plt.title(" line trend line")
plt.xlabel("month")
plt.ylabel("sales")
plt.legend()
plt.grid()
plt.show()
"""

# barh : 
"""df = pd.read_csv("pandas/sample_superstore1 copy.csv")

plt.barh(
    df['Category'],
    df['Sales'],
    color='red',
    label='Profit'
)
plt.title("Barh")
plt.xlabel("Profit")
plt.ylabel("Category")
plt.legend()
plt.grid()
plt.show()
"""

# scatter plot  : 

