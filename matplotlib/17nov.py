"""
matplotlib : basic  graph  use 
seaborn   :  statistical  graph  use 

pip install matplotlib.pyplot

graphs : 

1. plt.plot : line  graph 
2. plt.bar : bar  graph
3. plt.pie / donut : pie  graph
4. plt.scatter : scatter  graph
5. plt.hist : histogram  graph
6. plt.boxplot : boxplot  graph -----> outlier  detection 
7. plt.subplot  : mutiple graph  in one  frame 

plt.show() -----> graph show 
plt.xlable -----> x axis label 
plt.ylable -----> y axis label
plt.title  -----> graph title
plt.xticks -----> x axis ticks  rotation  of  font  
plt.yticks -----> y axis ticks  rotation  of  font  
plt.figure -----> line , width  -----> arg ----> fig size   ---> box
plt.grid()
plt.legend() -----> graph  legend

"""
import  matplotlib.pyplot as plt 
import  pandas as pd 
import numpy as np 

# line  graph : 
"""days = [1,2,3,4,5,6,7,8,9]
sales =[300,200,150,390,500,600,800,650,900]

plt.plot(
    days,
    sales,
    color = 'red',
    linestyle = '--',  # -------- , ; : 
    linewidth = 3,   # line thickness
    marker = 'o',   # intercept  : o , * ,
    markerfacecolor = 'blue',
    markersize = 5
    
)
plt.xlabel("days")
plt.ylabel("sales")
plt.title("sales  vs  days")
plt.grid()
plt.legend("sales",loc="upper left")
plt.show()
"""

"""data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],

    '2024_Sales': [12000, 15000, 14000, 18000, 20000, 22000,
                   19000, 25000, 23000, 27000, 30000, 35000],

    '2025_Sales': [15000, 17000, 16000, 21000, 24000, 26000,
                   23000, 28000, 27000, 31000, 34000, 40000]
}
df = pd.DataFrame(data)

plt.plot(
    df['Month'],
    df['2024_Sales'],
    color = 'red',
    linewidth = 3,   # line thickness
    marker = '*',   # intercept  : o , * ,
    markersize = 10
)
plt.plot(
    df['Month'],
    df['2025_Sales'],
    color = 'blue',
    linewidth = 3,   # line thickness
    marker = 'o',   # intercept  : o , * ,
    markersize = 10
)

plt.xlabel("month")
plt.ylabel("2024-25 sales")
plt.title("sales  vs  month")
# plt.grid()
plt.legend("24_25sales",loc="upper left")
plt.show()
"""

# bar chart : 

df=pd.read_csv("pandas/sample_superstore1 copy.csv")
plt.figure(figsize=(10,8))
plt.bar(
    df['Sub-Category'],
    df['Sales'],
    color = 'green',
    width = 0.8
)
plt.xlabel("subcategory")
plt.ylabel("sales")
plt.xticks(rotation=45)
plt.title("sales vs subcategory")
plt.show()

