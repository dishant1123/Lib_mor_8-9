import  matplotlib.pyplot as plt 
import pandas as pd 
import  numpy as np 

"""
data = pd.DataFrame({
       
       "company" : ["apple","vivo",'oppo',"samsung","MI","RealME"],  
       "market_share" : [40,30,20,10,5,3]
})
"""
# pie : 

"""
plt.pie(data["market_share"],
        labels=data["company"],
        autopct="%1.1f%%")
plt.title("market share of mobile phones")
plt.show()
"""
# task : pie chart  ---> using sample superstore csv 

# donut chart :
"""plt.pie(data["market_share"],
        labels=data["company"],
        autopct="%1.1f%%",
        wedgeprops={"edgecolor":"black","linewidth":1, "width" :0.4}
        )
plt.title("market share of mobile phones")
plt.show()

"""

# box  plot  : outlier  detection   

data = pd.DataFrame({
       
       "company" : ["apple","vivo",'oppo',"samsung","MI","RealME"],  
       "sales" : [400,300,200,100,50,3000]
})

plt.boxplot(
    x=data["sales"],
    vert=False
)
plt.title("sales of mobile phones")
plt.show()
"""
1. outlier  detection  using IQR : 
    IQR = Q3 - Q1
    
    upper limit = Q3 + 1.5 * IQR
    lower limit = Q1 - 1.5 * IQR
  
    print()
2. Z-score 
    from scipy import  stats    
    
    zscore ------> outlier print 
    

"""
