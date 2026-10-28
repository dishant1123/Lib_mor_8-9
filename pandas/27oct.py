import  pandas as pd 
import mysql.connector as mysql  
import psycopg2 as psy   # for  pgadmin 

# sql 
"""user = "root"
password ="root"
host = "localhost"
port = 3306
database ="da_students"

mydb = mysql.connect(user=user,
                     password=password,
                     host=host,port=port,
                     database=database)

df=pd.read_sql_query("select * from students_info",mydb)
print(df)
print(df.head(2))
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.shape)
"""

# Dataframe : 
"""
2 ways : 
1. from dict
2. from list of list

"""

# ex :1 create dataframe from dict

"""
df = pd.DataFrame({
    "id" : [1,2,3,4,5],
    "name" : ["heena","badal","chirag","sanju","sid"], 
    "marks" : [90,89,88,99,91],
    "city":["pune","mumbai","delhi","chennai","kolkata"]
    
})
# print(df)

# new col add in Dataframe : 
df["gender"] = ["female","male","male","male","male"]
print(df)
"""

# ex :2 create dataframe from list of list

"""
df = pd.DataFrame([
    [1,"heena",90,"pune"],
    [2,"badal",89,"mumbai"],
    [3,"chirag",88,"delhi"],
    [4,"sanju",99,"chennai"],
    [5,"sid",91,"kolkata"]
],columns=["id","name","marks","city"])
print(df)
"""

# read the  mckinsey data set  : 

df = pd.read_csv("pandas/mckinsey.csv")
print(df)
print(df.shape)
"""

# print  only  country col   -------> single col
print(df['country'])
"""

"""
# print country , populations  -------> multiple col 
country_population = df[['country','population']]
print(country_population)
"""

# task : 
"""
1. create  the dataframe using dict . 
    col names is : id ,name ,salary 
    output  : 
        id  name  salary
        1   heena  10000
        2   badal  20000
        3   chirag 30000
        4   sanju  40000
        5   sid    50000

2. changes the  sid  salary to 90000 
3. update  chirag name with salman . 

hint  : index  ------> df['salary'][4] =90000
"""






