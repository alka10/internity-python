#1 String slicing 
String ='SLICING'
  
s1 = slice(3)
s2 = slice(1, 5, 2) 
print("String slicing") 
print(String[s1]) 
print(String[s2]) 

#2.slicing of range function
a=range(101)
ans=a[10:80:4]
print(ans)
ans=a[::5]
print(ans)

#3 list slicing
lst=list(range(1,20))
print(lst)
print(lst[1:18])
print(lst[3:16])
print(lst[11:20])

#4. print sliced string
str='abgsrfehyufbjd'
print("sliced string",str[2:11:2])
print("sliced string",str[3:13:2])
print("sliced string",str[0:10:2])
print("sliced string",str[1:14:2])

#5. get sublist and subtuple
list5 = ['P', 'y', 't', 'h', 'o', 'n']
tuple = ('P', 'y', 't', 'h', 'o', 'n')

slice_object = slice(3)
print(list5[slice_object]) 

slice_object = slice(1, 5, 2)
print(tuple[slice_object])  