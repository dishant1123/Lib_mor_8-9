import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

# bar chat  : category  vs sales -----> label  

df = pd.read_csv("pandas/sample_superstore1 copy.csv")
"""
category_wise = df.groupby("Category")["Sales"].sum()
print(category_wise)
# graph  :

plt.figure(figsize=(10,5))
bars=plt.bar(
    category_wise.index, 
    category_wise.values,
    color ="green"
    
)
plt.bar_label(bars,padding=3,fmt="%.2f")
plt.title("category vs sales")
plt.xlabel("category")
plt.ylabel("sales")
plt.show()

"""

# scatter plot  :   reg  line  : y = mx +c  
df = pd.read_csv("pandas/sample_superstore1 copy.csv")

plt.scatter(
    df['Sales'],
    df["Profit"],
    s=50,
    c="red",
    alpha=0.5
)
plt.title("sales vs profit")
plt.xlabel("sales")
plt.ylabel("profit")
plt.show()

# next session  : subplot , ax chart ,annotated , style , theme , save

