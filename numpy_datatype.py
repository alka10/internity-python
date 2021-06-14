import numpy as np
#datatype
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr1=np.array(['addition','subtraction','multiplication','division'])
print(arr1.dtype)

#defined data type
arr2=np.array([6,5,4,3,2],dtype='S')
print(arr2)
print(arr.dtype)

#changing data type float to int
arr3 = np.array([1.6, 7.1, 9.1])
newarr = arr3.astype('i')
print(newarr)
print(newarr.dtype)

#int to bool
arr4 = np.array([0, 6, 3])
newarr = arr4.astype(bool)
print(newarr)
print(newarr.dtype)