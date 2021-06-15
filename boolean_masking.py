import numpy as np
arr=np.array([5,9,10,8,5,4,5])
print(arr==5)
print(arr<8)

#multidimensional array
b = np.array([[42,56,80,67],
              [11,80,42,10],
              [50,42,71,18]])

print(b >= 56)
#
arr=np.random.RandomState(0)
x=arr.randint(10,size=(3,4))
print(x)
print(x<6)

#bool array
a = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
b = np.array([1, 0, 0, 0, 1, 1], dtype=bool)
print(a | b)

#
x = np.arange(10)
print((x > 4) & (x < 8))
