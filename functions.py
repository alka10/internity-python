#return the largest from a list
l1=[6,7,3,19,35,24,9,6]
print(max(l1))

#return addition and subtration of number
def calc(a1,a2):
    return a1+a2, a1-a2
result=calc(25,13)
print(result)    

#sum all the numbers in a list

def sum(n):
    total = 0
    for x in n:
        total += x
    return total
print(sum((8,4,3,2,6)))      

#multiplication of numbers

def mul(number):
    total1 = 1
    for i in number:
        total1 *= i
    return total1
print(mul((2,8,4,5,1,6)))      

#swap the first and last element in list
def swap(li):
    size=len(li)
    t=li[0]
    li[0]=li[size-1]
    li[size-1]=t
    return li
li=[15,98,23,45,11]
print(swap(li))
