# function in python

'''def function_name(a,b):
    s= a+b
    print(sum)
    return s

print (function_name(5,8))
'''
# function in python
'''def rajab_name(a,b,c):
    sum= a+b*c 
    print(sum)
    return(sum)
rajab_name(5,7,3)
rajab_name(8,12,74)
rajab_name(3,5,1)'''


# convert usdt to pkr

def conveter(usdt_value):
    pkr_value = usdt_value * 278.43
    print(usdt_value, "usdt  =", pkr_value, "pkr " ) 

conveter( int( input("convert pkr to usdt : ")))    