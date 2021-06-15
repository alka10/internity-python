#addition using unfunc
import numpy as np

arr1 = np.array([11, 11, 12, 10, 14, 15])
arr2 = np.array([10, 21, 21, 20, 24, 25])
arr = np.add(arr1, arr2)
print(arr)
arr = np.subtract(arr1, arr2)
print(arr)
arr = np.multiply(arr1, arr2)
print(arr)

#summation over axis

arr=np.sum([arr1,arr2],axis=1)
print(arr)

#cummulative sum
arr=np.cumsum(arr1)
print(arr)
arr=np.cumsum(arr2)
print(arr)

#lcm 
n1=6
n2=8
x=np.lcm(n1,n2)
print(x)

#gcd in array
arr=np.array([10,20,16,18,20,36])
x=np.gcd.reduce(arr)
print(x)

#union of arrays
arr1=([10,12,16,8,6])
arr2=([2,8,17,6,5])
arr=np.union1d(arr1,arr2)
print(arr)

#intersection of array
arr=np.intersect1d(arr1,arr2,assume_unique=True)
print(arr)