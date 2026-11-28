"""
Histogram :
Definition: A histogram displays the frequency distribution of numerical data by dividing values into different intervals (bins).
Business example: How many orders fall into different sales ranges?

ECDF Plot :
Definition: ECDF stands for Empirical Cumulative Distribution Function. It shows the proportion or percentage of observations that are less than or equal to a particular value.
Business example: What percentage of orders have sales below ₹500?
    example  : 
    Suppose ECDF shows 0.60 at Sales = 500.
    It means 60% of orders have sales values less than or equal to 500.

Rug Plot :
Definition: A rug plot displays individual data points as small vertical marks along an axis. It helps us understand where observations are concentrated.
Business example: See the individual sales values of orders.

jointplot() :
Definition: jointplot() combines two numerical variables in one visualization. It displays a relationship plot in the center and their individual distributions along the top and right sides.

Business example: Is there a relationship between Sales and Profit?

sns.pairplot() :
Definition: pairplot() creates a grid of plots showing relationships between multiple numerical variables. It uses scatter plots for relationships and distribution plots on the diagonal.
"""
import pandas as pd  
import  seaborn as sns 
import matplotlib.pyplot as plt

# using sample  super store  : 

"""
df =pd.read_csv("pandas/sample_superstore1 copy.csv")
print(df.head()) 


sns.histplot(
    data=df,
    x="Sales",
    bins=30,
    color="black",
    hue="Category"
        
)
plt.title("sales distribution")
plt.show()
"""
# ecdfplot() :
"""
df =pd.read_csv("pandas/sample_superstore1 copy.csv")

sns.ecdfplot(
    data=df,
    x="Sales",
    color="black"
    
)
plt.show()
"""

# joint  plot  : 
"""
df =pd.read_csv("pandas/sample_superstore1 copy.csv")

sns.jointplot(
    data=df,
    x="Sales",
    y="Profit",
    kind="scatter",
    color="black",
    height=8
    
)
plt.title("joint plot")
plt.show()
"""

# pair plot  : 

df =pd.read_csv("pandas/sample_superstore1 copy.csv")

sns.pairplot(
    data=df,
    vars=['Sales','Profit','Quantity','Discount']
)
plt.savefig("pairplot.png", dpi=300)
plt.show()