#creating a view
import numpy as np
arr1=np.array([2,7,9,5,4])
view1=arr1.view()
arr1[1]=12
print("original array: ",arr1)
print("view of array: ",view1)

#copy using copy()

arr2=np.array([2,8,9,4,3])
copy1=arr2.copy()
arr2[1]=12
print("original array: ",arr2)
print("copy of array: ",copy1)

#multidimensianal array
arr4 = np.array([[20,10], [3,3], [8,5]]) 

print("array: ") 
print(arr4)

print("copy of array: ") 
b = arr4.copy()  
print(b)
 
print("change the element of b") 
b[0,0] = 30

print("after changing the value: ")
print(b)

#checking their base
arr = np.array([7, 6, 5, 3, 9])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)