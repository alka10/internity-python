import pandas as pd
import numpy as np
data=np.array([16,25,98,34,10])
d=pd.Series(data)
print(d)

#print using index value
print(d[0])
print(d[:3])
print(d[[0,1,4]])

#creating series and index

s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
print(s[[0,2]])
print(s[-3:])

#creating series using dictionary
data = {'apple' : 0., 'banana' : 1., 'cherry' : 2.,}
s = pd.Series(data)
print(s)
