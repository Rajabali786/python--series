'''name = input("what is your name : ",)
age = int(input("how old are you : ",))
print("Name= ", name )
print("age= ", age ) 

if(age>=18):
    print("cast your vote",)
elif(age<18):
    print("you are not elligable for vote",)
else:
    print("error!")'''

# LIST IN PYTHONE 

'''mark = 15
mark= 20
mark = 45
mark = 50
mark = 60'''

'''marks=[15,20,45,50,60]
print(marks)
print(type(marks))'''

'''student=["rajab", 62.5, 20, "rawalpindi"]
print(student)       
student[0]="RAJAB ALI,"
student[3]="Islamabad"
print(student) '''

'''list = [1,5,3,2,4,]
print(list.append(6))
print(list.sort())

print(list)'''

#tuple method
'''
tup =(1,5,2,1,4,1,5,1) 
print(tup.count(1))
print(tup.index(5))'''
   
                                #lets practics


#Question: write a program to ask the user enter name of their 3 favourit movies and store them in a list ;
#Answer
'''
fav_language= (input("Enter your favourit computer language 1 : "   ))
fav_language1= (input("Enter your favourit computer language 2: "   ))
fav_language2= (input("Enter your favourit computer language 3: "   ))
print(list [fav_language , fav_language1, fav_language2 ])'''

#Question: wap if a list contains a palindroms of elements (hint:use copy() method ) 
#Answer
'''list1=[1,1,1,2,1,1,1] 
list=[1,2,3]
copy_list1= list1.copy 
list1.reverse()

if(copy_list1==list1):
    print("palindrom")
else:
    print("non palindrom")    '''


name= input ( "what is your name: ", )
age=  int( input  ("what is your age: ",))
adrees= input ("adress: ",)
str.capitalize(name)
print( "wlecome",name )
print("your age is ",age )
print("your  adress is ", adrees)

if(age>=18):
    print("please cast your vote")
elif(age<18):
    print("you are not eligable")