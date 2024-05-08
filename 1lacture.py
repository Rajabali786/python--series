'''light= "blue"

if (light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go") 
else:
    print("dont move") '''

'''
age = 17

if( age>= 18):
    print(" you are voter of imran khan")
elif(age <=  18 ):
    print("dont cast vote")  ''' 


'''
name= input("what is your name : ",)
age= int(input( "How old are you : ", ))
print("Name= : ",name)
print("age= : ",age)


if(age>=18):
    print("please cast your vote")
elif(age<18):
    print("dont cast vote")
else:
    print("your are not pakistani citizen")'''


'''
a = int( input("enter first numb : ",))
b= int (input("enter secound numb : ",) )
c= int(input("enter third numb : ",))
d= int(input("enter fourth numb : ",))

if(a>b and a>c and a>d ):
    print("first numb is largest: ",)
elif(b>c and b>d ):
    print("b is largest numb: ",)
elif(c>d):
    print("c is largest mumb")
else:                 
    print("d is largest numb")        

'''

name1= input("Student name: ", )
rolnumb1=int(input("student roll number: ", ))
clas = [input("class: ",)]
marks= int(input("1) English: ", ))
marks1=int(input("2) Math: ",))
marks2=int(input("3) Urdu: ",))


dict={
    "name": name1, 
     "rolnumb1": rolnumb1,
      "class": clas,  
      "marks": {
          "English": marks,
          "Math" : marks1, 
          "Urdu" :   marks2 ,     
      }
}
print(dict.items())




if(marks>=33):
    print("congurelation you are PASS ")
if(marks1>=33):
    print("congurelation you are PASS")
if(marks2>=33):
    print("congurelation you are PASS")        

elif(marks<33):
    print("better luck for next time")    
elif(marks1<33):
    print("better luck for next time") 
elif(marks2<33):
    print("better luck for next time") 
