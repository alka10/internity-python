#fibonacci using generators
def fib(range):
    n1,n2=0,1
    while n1<range:
        yield n1
        n1,n2=n2,n1+n2
f=fib(6)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

#prime numbers
def prime():
    num=1
    while num<100:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
        num += 1

for item in prime():
    print(item)

# arithmetic progression
def AP(first, dif, length):
    count = 1
    while count <= length:
        yield first
        first += dif
        count += 1

for i in AP(2, 3, 10):
    print(i)

#table 
def Table(numb):
   for y in range(1, 11):
       yield y * numb
       y += 1

t = Table(15)
for a1 in t:
   print(a1)    

#even squares in a list   

def even_squares(element):
  for k in range(element):
    if k**2%2==0:
      yield k**2
print(list(even_squares(20)))