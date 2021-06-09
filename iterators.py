#iterator over list
list4=[1,2,5,6,8,3,9,5]
iter2=iter(list4)
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))

#iterating over a string
string='language'
for iter1 in string :
 print(iter1)

#print elements in a list using iterators

list=['maths','english','science','computers']
list_iter=iter(list)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))

#iterate upto 10 counter
class counter:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=10:
          x=self.a
          self.a+=1
          return x
        else:
            raise StopIteration
myclass = counter()
iter=iter(myclass)
for x in iter:
    print(x)            

# even numbers
class Even:
    end = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.end += 2
        if self.end > 16:
            raise StopIteration
        return self.end
e = Even()
for num in e:
    print(num)              