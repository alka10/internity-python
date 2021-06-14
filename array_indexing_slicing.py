#array indexing and slicing

#array with specified start stop and step
import numpy as np
arr=np.array([1,2,5,8,3,6,8,9,3])
a=arr[2:8:2]
print(a)

#integer indexing
arr2 = np.array([[1 ,9 ],[5 ,8 ],[3 ,8 ]])
print("array before indexing: ")
print(arr2)
print("array after indexing: ")
print(arr2[[0 ,1 ,2 ],[0 ,0 ,1]])

#boolean indexing

arr3=np.array([19,40,10,23,80,20])
print(arr3[arr3<40])
print(arr3[arr3%10==0]**2)

#slicing
arr4=np.array([1,7,4,3,2,9])
print(arr4[3:])

#multidimensional array slicing 
arr5=np.array([[1,3,5],[7,5,2],[8,6,4]])
print("array before slicing: ")
print(arr5)
print("after slicing: ")
print(arr5[1:])
print(arr5[...,1:])