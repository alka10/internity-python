#file opening in read mode
file = open("python_file.text", "r") 
print (file.read())

#writing in a file in write mode
file = open('python_file.txt','w')
file.write("This is a python file")
file.write("this file contains data about python")
file.close()

#split function
with open("python_file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

#copy content of one file to another
with open('f1.txt','r') as firstfile, open('f2.txt','a') as secondfile:
      
    for line in firstfile:
               
             secondfile.write(line)   

#reversing the content of a file and storing in another file
f2 = open("op2.txt", "w") 
 
with open("python_file.txt", "r") as myfile:
    data = myfile.readlines()
data_2 = data[::-1]
f2.writelines(data_2)
  
f2.close()                  