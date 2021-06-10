#addition of two numbers
class add():

    def sum(x, n1, n2):
        x = n1 + n2
        return x


n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

newAdd = add()
x = newAdd.sum(n1, n2)

print("Sum is:", x)
#area of rectangle
class rect():
    def __init__(self,b,l):
        self.b=b
        self.l=l

    def area(self):
        return self.b*self.l
m=int(input("enter length: "))
n=int(input("enter breadth: "))
obj=rect(m,n)
print("area of rectangle: ",obj.area())  
print()         

#convert the string in uppercase
class string():
    def __init__(c):
        c.str=""
    def getstring(c):
        c.str=input("enter the string: ")
    def printstring(c):
        print("string in uppercase",c.str.upper())
str=string()
str.getstring()
str.printstring()    

#area of circle and perimeter
class Circle():
    def __init__(d, radius):
        d.r = radius

    def area(d):
        return d.r**2*3.14
    
    def perimeter(d):
        return 2*d.r*3.14
rad=int(input("enter the radius: "))
ob = Circle(rad)
print("area of circle: ",ob.area())
print("perimeter of circle: ",ob.perimeter())

#complex number addition

class addComplex ():
    def Complex(ele):
        ele.real = int(input("Enter the Real Part: "))
        ele.img = int(input("Enter the Imaginary Part: "))            
    def display(ele):
        print(ele.real,"+",ele.img,"i", sep="")
    def sum(ele, c1, c2):
        ele.real = c1.real + c2.real
        ele.img = c1.img + c2.img
c1 = addComplex()
c2 = addComplex()
c3 = addComplex()
print("Enter first complex number")
c1.Complex()
print("Enter second complex number")
c2.Complex()
print("Sum of two complex numbers is ", end="")
c3.sum(c1,c2)
c3.display()
