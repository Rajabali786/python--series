# loops in python 
 
   ################# while condition ###################################:  

'''count = 1 
while count <=50:
    print( count , "rajab"  )
    count += 1
   '''
    


# print number 1 to 5 

'''count = 1
while count <=5:
    print(count)
    count +=1  

print("end loop")'''

'''i = 5
while i >= 1 :
    print(i)
    i -=1

print("end loop")
..........................................................................'''

# practic question

#1. print number 1 to 100

'''count = 1
while count <=100:
    print(count)
    count+=1
    print("end loop")'''


#2. print number 100 to 1

'''count= 100
while count >= 1:
    print(count )
    count -=1   '''         # done 


#3. print the multiplication table of a numb n 

'''n= int(input("TABLE : "))   
count =1
while count <=10:
    print(count*n)
    count+=1'''

 
#4. print the element of the following list using a loop:

'''L=[1,5,9,17,25,46,75,84,99,100]

i=0
while i < len(L):
    print(L[i])
    i+=1'''


#5.  surch for a numb  x in this tuple using loop:     

'''L=(1,5,9,17,25,46,75,84,99,100)
print(L)
x=int(input("find number: "))

i=0
while i < len(L):
    if (L[i]==x):
        print("found at idx", i )
    i+=1'''

 # again

'''L = (5,4,8,77,55,15,94,61,164,15,154)   
print(L)
x= int(input("find idx: "))
i=0
while i < len(L):
    if ( L[i]==x ):
        print("found idx", i)
    i+=1'''

# break and continue 

'''i=0
while i<=50:
    
    if (i%2 !=0):
        i+=1
        continue
    print(i)
    i+=1'''

################  for loops ############################

'''list={1,2,3,4,5,6,7,8,9}
for el in list:
    print(el)'''

  
  # for loop with else:
'''list=("my name is rajab")
for a in list:
  
    if (a=="i"):
        print(" i find ")
        break
    print(a)
else:
    print("END")   '''    


         #lets practics using for loop :::

#1. print the  element of the following list using for loop:

'''list=(1,25,78,65,45,89,77,66,59)
for a in list:
    print(a)   '''

#2. search for a numb x in this tuple using loop.

'''list=(1,25,78,65,45,89,77,66,59)
print(list)
x= int(input("find numb of x: " )) 
for a in list:
    if (a == x):
        print("x value is", x )'''

 
             # using for & range loop
 #3. print numb from 1 to 100          

'''for numb in range(1 , 101):
    print(numb)'''


#4. print numb from 100 to 1

'''for numb in range(100,0,-1):
    print(numb)''' 

#5.  print the multiplication table numb of n

n=int(input("Multiplication numb of n : "))
for numb in range(1,11 ):
    print(n * numb)

#6. wap to find sum first n number 

'''n= int(input("put value: " ))
i=1
sum=0
while i <= n:
    sum+=i
    i+=1 
print("total sum = ", sum )'''
                    
                                                                                                                                  
#7. wap to find factorial first n number.
'''
n=5
factorial =1
for i in range (1 , n+1):
    factorial *= i
print("factorial = " , factorial)'''
