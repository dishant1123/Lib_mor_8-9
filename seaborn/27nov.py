import  pandas  as pd
import  seaborn  as  sns
import  matplotlib.pyplot  as  plt

# regplot   or  lmplot :
"""
regression line = y = mx +c    ----> y--->reg     
                                    m -->slop   
                                    x   
                                    c --->intercept 


""" 
# lmplot  / reg plot : 
"""
df=pd.read_csv("pandas/sample_superstore1 copy.csv")

sns.regplot(
    data=df, 
    x="Sales",
    y="Profit",
    scatter_kws={"color":"red"},
    line_kws={"color":"green"}
)
plt.show()
"""

# heatmap  : 
"""
df=pd.read_csv("pandas/sample_superstore1 copy.csv")

corr_with_sample =df.corr(numeric_only=True)

sns.heatmap(corr_with_sample,
            annot=True,
            cmap="coolwarm",
            alpha=0.5
            )

plt.show()
"""
# KDE : kernel density estimation 

# sales distribution  : 

df=pd.read_csv("pandas/sample_superstore1 copy.csv")

sns.kdeplot(
    data=df,
    x="Sales",
    fill=True,
    color="red"
)
plt.show()
