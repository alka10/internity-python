#creating dataframe from a csv file
import pandas as pd
data=pd.read_csv('D:\Placement_Data_Full_Class.csv')
data.head()
data.describe()
#creating dataframe from a database
import sqlite3
con=sqlite3.connect('EMPLOYEE.db')
sql=pd.read_sql("SELECT * FROM EMPLOYEE;",con)
data.head()
data.describe()

#API
df=pd.read_json(r'C:\Users\Neha Pal\OneDrive\Documents\data1.json')
print(df)
