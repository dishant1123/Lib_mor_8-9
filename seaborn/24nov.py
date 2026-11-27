# two level charts :
"""

Axes level charts  : 
Relational plots:
    sns.scatterplot()
    sns.lineplot() ----> done 

Distribution plots:
    sns.histplot()
    sns.kdeplot()
    sns.ecdfplot()
    sns.rugplot()

Categorical plots:
    sns.boxplot() ----> done 
    sns.violinplot() ---> done
    sns.barplot() ----> done  
    sns.countplot() ----> done   ----> pending  : bar_label,hue 
    sns.swarmplot() ----> done
    sns.pointplot() ----> done 

Regression plots:
    sns.regplot()   ---> done

Matrix plots:
    sns.heatmap()  ----> done 

figure level charts:

Relational plots:
    sns.relplot() → wraps scatterplot() / lineplot()

Distribution plots:
    sns.displot() → wraps histplot(), kdeplot(), ecdfplot()
    sns.jointplot() → combines scatter + marginal histograms
    sns.pairplot() → grid of pairwise plots

Categorical plots:

    sns.catplot() → wraps boxplot(), violinplot(), barplot(), countplot(), stripplot(), swarmplot()

Regression plots:
    sns.lmplot() → wraps regplot() with faceting

"""
import  pandas as pd 
import  seaborn as sns
import  matplotlib .pyplot as plt 

# line  plot  : month vs sales

"""
df = pd.read_csv("seaborn/customer_sales.csv")
month_sales = df.groupby('Month')['Sales'].sum()

sns.lineplot(
    x=month_sales.index,
    y=month_sales.values,
    marker='o',
    color='red',
    linewidth=2,
    linestyle='--',
    label='Sales'
        
)
plt.title("month vs sales")
plt.show()
"""

# bar  plot  : 

"""
df = pd.read_csv("seaborn/customer_sales.csv")
# month_sales = df.groupby('Month')['Sales'].sum().reset_index()
df['Gender'] =df['Gender'].map({'M':1,'F':0})

month_sales = df.groupby(['Month','Gender'])['Sales'].sum().reset_index()
bars =sns.barplot(
    data=month_sales,
    x='Month',
    y='Sales',
    color='red'
    
)
plt.title("month vs sales")
plt.show()  

"""

# count plot  : 

df = pd.read_csv("seaborn/customer_sales.csv")
sns.countplot(
    data=df,
    x='Gender',
    color="green"
   
)
plt.title("count  plot  gender wise ")
plt.show()
