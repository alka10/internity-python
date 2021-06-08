#find string that has a followed by zero or one b
import re
s='my 2 nd most favourite number is 10'
print(re.findall('[0-9]+',s))

#search regular expressions
import re
p=re.compile('[b-g]')
print(p.findall("the cat is walking in the garden"))          

#find all five character word
import re
text='the quick brown dog jumps over the hut'
print(re.findall(r"\b\w{5}\b",text))

#find all 3 4 5 character long words
print(re.findall(r"\b\w{3,5}\b",text))

#splitting
import re
print(re.split('\d+','on 12th today is a good day',1))

#find substring and replace
import re
print(re.subn('av', '***' , 'they have left us'))
t = re.subn('av', '***' , 'they have left us here to have some food')
print(t)