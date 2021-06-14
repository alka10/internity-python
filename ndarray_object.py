#ndarray object
import numpy as np

#1 dimension array
arr=np.array([1,4,8,9])
print("1 dimensional array: ")
print(arr)

#two dimension array
arr1=np.array([[1,2,3],[4,5,6]])
print("2 dimensional array: ")
print(arr1)

#3 dimension array
arr2=np.array([1,2,3,7,5],ndmin=3)
print("array with minimum 3 dimension: ")
print(arr2)

#array of complex type
arr3=np.array([1,7,5],dtype=complex)
print("complex dtype parameter: ")
print(arr3)

#array with float dtype
arr4=np.array([[1,6,7],[4,9,0]], dtype='float')
print("float type array: ")
print(arr4)

#zero array
arr5=np.zeros((3,3))
print("array with all the zeroes: ")
print(arr5)

