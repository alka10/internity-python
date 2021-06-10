#1.

class Desc(object):
  
    def __init__(s, word =''):
        s.word =word
  
    def __get__(s, obj, objtype):
        return "{}for{}".format(s.word, s.word)
  
    def __set__(s, obj, word):
        if isinstance(word, str):
            s.word = word
        else:
            raise TypeError("Word should be a string type")
          
class descriptor(object):
    word = Desc()
    
t = descriptor()
t.word = "world"
print(t.word)

#2.
class OneDigitNumVal():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

class Fun():
    number = OneDigitNumVal()

d1 = Fun()
d2 = Fun()

d1.number = 3
print(d1.number)
print(d2.number)

d3 = Fun()
print(d3.number)

#3.

class prop:
    def __init__(self, val):
        self._val = val
          
    def getValue(self):
        print('Getting value')
        return self._val
          
    def setValue(self, val):
        print('Setting value to ' + val)
        self._val = val
    val = property(getValue, setValue, )    
x = prop('PythonProgramming')
print(x.val)
  
x.val = 'PP'      



