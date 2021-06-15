#arrays 
import numpy as np

arr = np.array([[1, 2, 3], [3, 4, 5]])
print(arr)

arr = np.array([[1.1, 2, 3], [3, 4, 5]]) 
print(arr)

arr = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) 
print(arr)

#matrix addition
arr1=np.array([[1,2],[5,6]])
arr2=np.array([[1,7],[2,5]])
sum=arr1+arr2
print(sum)

#matrix multiplication using dot funtion
mul=np.dot(arr1,arr2)
print(mul)

#transpose of matrix
print(arr1.transpose())

#slicing
A = np.array([[1, 4, 5, 12, 14], 
    [-5, 8, 9, 0, 17],
    [-6, 7, 11, 19, 21]])
print(A[:2,:4])
print(A[:1,1])
print(A[:,2])    