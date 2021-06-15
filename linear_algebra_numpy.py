#detreminant of array
import numpy as np
arr=([1,7,5],
      [2,4,3],
      [3,2,3])
print("determinant of array: ",np.linalg.det(arr))

#inverse of array
print("inverse of array: ",np.linalg.inv(arr))
print("trace of array: ",np.trace(arr))

# dot function
arr1=np.array([[10,20],[20,40]])
arr2=np.array([[20,10],[10,25]])
dot_product=np.dot(arr1,arr2)
print(dot_product)

#vdot funtion
arr1=np.array([[10,20],[20,40]])
arr2=np.array([[20,10],[10,25]])
vdot_product=np.vdot(arr1,arr2)
print(vdot_product)

#inner funtion
a=np.array([1,2,8,6,5])
b=np.array([2,3,8,6,5])
inner=np.inner(a,b)
print(inner)

#linear equation solution using solve funtion
arr3=np.array([[1,7],[5,4]])
arr4=np.array([[1,7],[5,4]])
print(np.linalg.solve(arr3,arr4))