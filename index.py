#1. print the index of element
list = [1,2,3,4,5,4,3,1,1,7]
print(list.index(4))

#2.print the index
list1 = ['alka','kajal','pal','line']
print(list1.index('pal'))
print(list.index(3,4,7))

#3.negative index
myList=['iphone','mi','vivo','pixel','oneplus']
print("list content ",myList)
print("item at index -1 is ",myList[-1])

#4.print item in a index range
myList1=['c#','python','c++','c','sql','ruby','fortran']
print("items in range [2:4] is ",myList[2:5])

#5. access items in negative range
print("items in range [-5:-1] is ", myList1[-5:-1])

#6. index of item to the end of the list
l= [7,2,3,4,6,8,5,5]
print(l.index(6 , 1 ))