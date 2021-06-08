#1. exception indexerror
lst=[5, 10, 20]

try:
    print(lst[5])
except IndexError:
    msg="You're out of list range"

print(msg)

#2.
a=5
b=0

try:
    print(a/b)
except ZeroDivisionError:
    print("you can't divide with 0")

 #3.

def divide(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
divide(5.0, 5.0)
divide(5.0, 3.0)
#4.
p = 50
try:
    p = p/10
except ZeroDivisionError:
    print('Cannot divide by 0 ')
finally:
    print('finally block ')
#5.
value = [1, 2, 3, 4]
val1= 0
try:
    data = value[4]
except IndexError:
    print('indexError occured')
