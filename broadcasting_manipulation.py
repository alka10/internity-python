import numpy as np
arr1=np.array([1,2,7,5,9,3,4,2])
arr2=7
arr=arr1+arr2
print(arr)

#broadcasting
arr1=np.array([[10,19,12],[8,5,3]])
arr2=6
arr=arr1+arr2
print(arr)

#3.
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
a.shape = (3,2)
print(a)

#4.

v = np.array([10, 20, 6]) 
w = np.array([10, 15])   
print(np.reshape(v, (3, 1)) * w)
 
x = np.array([[12, 22, 33], [45, 55, 66]])
print(x + v)
print((x.T + w).T)
print(x + np.reshape(w, (2, 1)))
print(x * 2)