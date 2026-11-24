import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns
# pip install seaborn 
"""
1. matplotlib 
2. seaborn  : 

difference  between  matplot lib  and seaborn : 
                matplotlib               seaborn
1.use           basic  graph            statistical  graph,analysis 
2.code          more code               less code 
3.dataset       import                  by  defult
4.performance   faster                  slower  

"""
# load_dataset : tips , titanic ,diamond , iris ---> flower 
"""
df =sns.load_dataset("tips")
df =sns.load_dataset("titanic")

print(df.head())
print(df.info())
"""

# line  plot  : 

days =[1,2,3,4,5,6,7,8,9]
sales =[200,300,134,567,890,210,349,560,789]

sns.lineplot(x=days,
             y=sales,
             marker='o')
plt.title("line plot")
plt.show()

"""
1. figure level charts:  
2.axes level charts : 
"""
"""
Task 4 : Regional Sales Dashboard: Create a 2 * 2 subplot dashboard showing regional sales, 
regional profit, monthly sales trends, and sales vs profit using Matplotlib.
"""

