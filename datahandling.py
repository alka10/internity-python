#create series using pandas
import pandas as pd
import numpy as np

arr=np.array([100,101,104,103,107])
s=pd.Series(arr)
print(s)

#create series uisng mutable index

import pandas as pd
import numpy as np
arr1=np.array(['apple','mango','banana','guava','pineapple'])
s=pd.Series(arr1,index=(['1st','2nd','3rd','4th','5th']))
print(s)

#creating a series from dictionary

import pandas as pd
dict={'name':'akanksha','roll_no':106,'subject':'python'}
s=pd.Series(dict)
print(s)

#addition/subtraction in series

import pandas as pd
s1=pd.Series([4,8,5,5,3,9])
s2=pd.Series([6,8,3,2,9,6])
print("Addition of s1 and s2: ")
print(s1+s2)
print("/n")
print("subtraction of series")
print(s1-s2)

#head and tail in series
import pandas as pd
arr2=np.array([12,24,35,61,24,10,18])
s=pd.Series(arr2)
print("series: ")
print(s)
print("head: ")
print(s.head(5))
print(s.head(3))
print("tail: ")
print(s.tail(5))
print(s.tail(3))