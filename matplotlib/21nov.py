import  pandas as pd 
import  matplotlib.pyplot as plt 
import  numpy  as np  

df = pd.read_csv("pandas/sample_superstore1 copy.csv")
"""
# sales -----> mean , sales ------> median 
means_sales = df['Sales'].mean()
median_sales = df['Sales'].median()

print(f"mean of sales is {means_sales}")
print(f"median of sales is {median_sales}")

plt.figure(figsize=(10,5))
plt.hist(
    df['Sales'],
    bins=25,
    color='skyblue',
    edgecolor='black'
)
plt.axvline(
    means_sales,
    color='red',
    linestyle='--',
    linewidth=2,
    label='Average Sales'
)
plt.axvline(
    median_sales,
    color='green',
    linestyle='--',
    linewidth=2,
    label="center sales"
)

plt.title('Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.grid()
plt.legend()
plt.show()
"""
# annotated: 

"""
1.month vs  sales 
2. print  highest index of month   and  print  higest value of sales 

hint  : function  : idxmax , idxmin 
"""

