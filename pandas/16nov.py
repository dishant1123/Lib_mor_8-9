# eda :Exploratary  data  analysis 
"""
Univariate analysis : 
Bivariate analysis  : 

data set  : sample suprtstore  :  -----> missing  value ----> fillna 

1. total orders : order_id ------> group by  ----> agg ---> count or sum
2. date  : 
        convert  ----> pd.to_datetime :  month   -----> month wise  sale , profit  
                                         year   ------> year wise  sale ,profit 
                                         day    ------> day wise sales , profit  ----> group by 
                                         
3. customer name highest  sales or  highest  profit earn  ----> name ----> group by  , sort_value ,head 
4. segemant  ------> 3 types 
                        1. consumer   -----> profit  sales 
                        2. corporate  -----> profit  sales 
                        3. home Office ----->profit  sales  
5. city  state ----> profit sale 
6. region -----> profit  sale 
7. category  ,  sub cat -----> profit  , sales 
8. total sales 
9. total profit 
10.discount    -----> print which  sub catgory give the  highest  discount  
               ------> calculate the  net  sales ----> after  deducted  the  discount 
             
"""
import  pandas as pd 

import ydata_profiling as ydp  # pip install ydata-profiling

sample_superstore = pd.read_csv("pandas/sample_superstore1 copy.csv")

result = ydp.ProfileReport(sample_superstore, 
                           title='EDA report',
                           explorative=True)
result.to_file("pandas/EDA_report.html")


# movies and  directors -----> insights 

import sweetviz as sv
report =sv.compare()
report.to_file("pandas/EDA_report.html")




