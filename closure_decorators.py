#addition using closure
def add():
    total=0
    def sum1(num):
        nonlocal total
        total +=num
        return total
    return sum1
print("addition:") 
s1=add() 
print(s1(9))
print(s1(46))
print(s1(29))
print(s1(25))  

#accessing outer function
def f1():
    name = "Alka"

    def f2():
        return f"Hey, {name}"

    return f2
func = f1()
print(func())

#3.
def multiplier(x):
    def multiply(y):
        return x*y
    return multiply

multipliers =[]
for x in range(1,4):
    multipliers.append(lambda y: x*y)
m1,m2,m3 = multipliers
print(m1(10))
print(m2(10))
print(m3(10))    

#addition using decorator 
from operator import*
a1=10
def func1():
    b1=20
    def func2():
        c1=30
        print(add(b1,c1))
        print(a1)
    func2()  
func1() 

# quadratic equation using closure
def quadratic(a,b,c):
    def equation(x):
        return a*x**2+b*x+c
    return equation
   
f=quadratic(1,1,1)
for i in range(5):
    print("f({})={} ".format(i,f(i)),end=" ")
print("\n")


