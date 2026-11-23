import pandas as pd  
import matplotlib.pyplot as plt 

# sub  plot  : 

"""
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [12000, 15000, 18000, 14000, 22000, 25000],
    'Profit': [2000, 3000, 4000, 2500, 5000, 6000],
    'Quantity': [100, 120, 150, 110, 180, 200],
    'Category': ['Furniture', 'Technology', 'Office Supplies',
                 'Furniture', 'Technology', 'Office Supplies']
}

df = pd.DataFrame(data)
print(df.head()) 

# line , bar, pie,scatter  
plt.figure(figsize=(12,8))
plt.subplot(2,2,1) 
plt.plot(
    df['Month'],
    df["Sales"],
    color="red",
    marker="o",
    linestyle="--"
)
plt.title("sales vs month") 

plt.subplot(2,2,2)
bars =plt.bar(
    df['Category'],
    df["Sales"],
    color="green",
  
)
# plt.bar_label(bars,padding=3,fmt="%.2f")
plt.title("sales vs category bar chart")

plt.subplot(2,2,3)
plt.pie(
    df["Profit"],
    labels=df["Category"],
    autopct="%1.1f%%"
)
plt.title("Profit vs category pie chart")

plt.subplot(2,2,4)
plt.scatter(
    df["Sales"],
    df["Profit"],
    color="blue",
    s=50,
    alpha=0.5
)
plt.title("Profit vs sales scatter chart")
plt.tight_layout()
plt.show()
"""

# axes plot : 

"""data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [12000, 15000, 18000, 14000, 22000, 25000],
    'Profit': [2000, 3000, 4000, 2500, 5000, 6000],
    'Quantity': [100, 120, 150, 110, 180, 200],
    'Category': ['Furniture', 'Technology', 'Office Supplies',
                 'Furniture', 'Technology', 'Office Supplies']
}

df = pd.DataFrame(data)
print(df.head()) 

fig,ax =plt.subplots(2,2,figsize=(12,8))

ax[0,0].plot(df['Month'],df['Sales'],color="red")
ax[0,0].set_title("sales vs month")
ax[0,0].set_xlabel("Month")
ax[0,0].set_ylabel("Sales")

ax[0,1].bar(df['Category'],df['Sales'],color="pink")
ax[0,1].set_title("cat vs sales")
ax[0,1].set_xlabel("cat")
ax[0,1].set_ylabel("sales")

ax[1,0].pie(df['Profit'],labels=df['Category'],autopct="%1.1f%%")
ax[1,0].set_title("Profit vs category pie chart")

ax[1,1].scatter(df['Sales'],df['Profit'],color="blue",s=50,alpha=0.5)
ax[1,1].set_title("Profit vs sales scatter chart")
ax[1,1].set_xlabel("Sales")
ax[1,1].set_ylabel("Profit")

plt.tight_layout()
plt.show()
"""

