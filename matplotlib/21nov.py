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

df = pd.read_csv("pandas/sample_superstore1 copy.csv")
"""
df['Order Date']=pd.to_datetime(df['Order Date'])
df['Month']=df['Order Date'].dt.to_period('M')
monthly_sales =df.groupby('Month')['Sales'].sum()

higest_month = monthly_sales.idxmax()  #  ----> index   # 12   ----> 114289
highest_sales = monthly_sales.max()   #  -----> value 

max_index =monthly_sales.values.argmax()
print(f"highest month is  : \n{higest_month}  highest sales is  : \n{highest_sales} max index month : \n {max_index}")

# graph  : 

for i , value in enumerate(monthly_sales.values):
    plt.text(i,
             value+100,
             fmt="{:.2f}",
             ha='center')

plt.annotate(
    highest_sales,
    xy=(higest_month, highest_sales),
    xytext=(higest_month, highest_sales+100),
    arrowprops=dict(
        arrowstyle='->',
        color='red')
    
)
plt.savefig("annotated.png",dpi=300)
plt.show()
""" 

# sub plot ,axex plot : 