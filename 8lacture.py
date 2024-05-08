                    #oops in python 
#to map with real world scenarirrs we started using object in code.
#this is called object oriented programming. 

          # class and object in python..
#class is a blue print for creating object. 
 
'''class student:               # class
    name ="Rajab ali"
    
s1=  student()               # object
print(s1.name)'''

#...................................................

           #   __init__function

'''class student:
    def __init__(self , fullname,marks ):
        self.name = fullname
        self.marks= marks

s1 = student("rajab ali", 91 )
print(s1.name, s1.marks)

s2= student("Awais khan", 95 )
print(s2.name,s2.marks )

s3= student ("usama mehboob" , 99 )
print(s3.name, s3.marks )'''

#...............................................
             
             # Methood

'''class student:
    def __init__(self , name, marks ):
        self.name = name
        self.marks= marks

def wellcome (self):                                  # methood
    print("wellcome students ,", self.name)
            
def marks (self):
    return self.marks              

s1=student ("rajab ali", 65 )

s1(wellcome)
print(s1.get_marks() )'''


                # practics question
  # Q.  create student class that take name and marks of three subject as argument in costructor. then create a methood to print the average.  

'''class student :
    def __init__(self , name , marks ):
        self.name = name
        self.marks= marks

        def get_avg(self):
            sum=0
            for val  in self.marks:
                sum+= val
            print("hello", s1.name , "your average score is" , sum/3  )    


s1 = student("Rajab Ali" , [45, 52, 62 ])
s1.get_avg()'''



        # static methood 

# methood that dont use the self parameter(work at class level)

'''class student:
    @staticmethod                     # static methood 
    def college():
      print("apna college")'''

#..............................................................................

'''class car:
    def __init__(self):
        self.acc = False
        self.ing = False
        self.brk = False

    def self(self):
        self.acc = True
        self.ing = True
        self.brk = True
        print("car started..")  

car1 = car()
car1.start()
'''
#.......................................................

                         #  practic question
#Q. create account class with two attributes-balance and account numb. 
#   create methood for debit, creadit and printing the blance.
"""
pin= int(input("please enter your pin: ",  )  ) 
if ( pin == 1196 ):
    print ( "thank you for using HBL atm" )
    
else:
    print(   "please correct your password " ,  )

class Account:
    
    def __init__(self, blance, acc):
        self.blance      = blance
        self.account_no  = acc
        print("total blance: ", self.get_blance() )
        print("..................................")
        # debit methood
    def debit( self, amount ):
        self.blance -= amount
        print("Rs:", amount, " was debit")
        print("total blance: ", self.get_blance() )
        print("..................................")

    def creadit( self, amount ):
        self.blance += amount
        print("Rs:", amount, " was creadit") 
        print("total blance: ", self.get_blance() ) 
        print("..................................")
        print("Thank you for using HBL atm ")

    def get_blance(self):
        return self.blance  

acc1 =  Account (35000, 1196)

acc1.debit (int (input( "Debit: ", )))
acc1.creadit (int(input("Creadit: ")))
"""



        #  inheritance in oop.



'''class car :
    @staticmethod
    def start():
        print ("car started")

    @staticmethod
    def stop():
        print("car stopped")


class toyatacar(car):
    def __init__(self, name  ):
        self.name= name

car1 = toyatacar("fortuner")
car2 = toyatacar("prado")

print(car1.start())'''

str= "awais"
str1=  len(str)
print(str1)