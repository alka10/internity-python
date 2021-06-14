
#array creation
import numpy as np

a=np.array(5)
print("zero dimension array: ")
print(a)

# 1 dimension array
arr=np.array([1,4,8,9])
print("1 dimensional array: ")
print(arr)

#two dimension array

arr1=np.array([[1,2,3],[4,5,6]])
print("2 dimensional array: ")
print(arr1)

#3 dimension array

arr2=np.array([[[1,5,4],[6,4,9],[9,1,1]]])
print("3 dimension array: ")
print(arr2)

#number of dimensions
print(a.ndim)
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)

#array with specified dimension
arr3=np.array([1,8,5,7],ndmin=4)
print(arr3)
print(arr3.ndim)