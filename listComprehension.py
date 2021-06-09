
#even number using list comprehension
list=[7,8,23,80,6,4,1,9,35,69,24]
even=[list for list in list if list %2==0]
print(even)

#print all number in a range and divisible by 7
div=[number for number in range(1,999) if number %7==0]
print(div)

#count the number of spaces in a string
str= 'the sky is pink'
space=[s for s in str if s == ' ']
print(len(space))

#all words in a sring greater than 5
string='python list comprehension is a great topic and it is quite interesting too'
a=string.split()

output=[word for word in a if len(word)>5]
print(output)

#squares of numbers in a given range
sqr=[a*a for a in range(1,20)]
print(sqr)