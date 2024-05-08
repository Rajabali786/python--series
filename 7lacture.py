'''f = open("sample.txt" , "r" )
line1= f.readline()
print(line1) 
line2= f.readline()
print(line2)

f.close()

import os
os.remove("demo.txt")'''

# practies question

#1. create a new file "practic.txt" using python add the following data init.
                       #1 methood
'''f= open("sample.txt",  "r" )
line =f.read()

print(line)
'''
                    #2 methood
'''with open("demo.txt", "w") as f:
   f.write("hello everyone\nwe are learning file I/O\n")
   f.write("using java\ni like programing in java")'''

#........................................................................

#2. waf that replace all occurance of "java" with "python" in above file. 

'''with open("demo.txt", "r" ) as f:
   data = f.read()

new_data= data.replace("java", "python" )
print(new_data)

with open("demo.txt", "w" ) as f:
   print(new_data)'''

#........................................................................

#3. search if the world "learning" exist in the file or not.

'''world="learning"
with open ("sample.txt", "r") as f:
   data= f.read()
   if(data.find(world)  !=-1 ):
      print("found")
   else:
      print("not found")  ''' 

a = 5
b = 2

sum= a+b 
print(sum)