import pandas as pd
dataset = [1,2,3,4,5,6,7,8,9,0]
df = pd.DataFrame(dataset)
print(df) 

#creating dataframe with column names
data=[['student1',1],['student2',2],['student3',3],['student4',4]]
df=pd.DataFrame(data,columns=['name','roll_no'])
print(df)

#creating dataframe using ndarray
data = {'Name':['student1', 'student2', 'Student3', 'student4'],'Age':[12,13,12,14]}
df = pd.DataFrame(data)
print(df)

#creating dataframe using series
data={'name':pd.Series(['alka','karan','manya','diksha','ajay'],index=[1,2,3,4,5]),'age':pd.Series([20,19,18,21,22],index=[1,2,3,4,5])}
df=pd.DataFrame(data)
print(df)

#adding new column
df['salary']=pd.Series([20000,22000,30000,15000,12000],index=[1,2,3,4,5])
print(df)