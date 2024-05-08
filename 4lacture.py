# dictionary in python

'''subject=  {
    "name" : "rajab",
    "class" : "2year",
    "marks" :{                         #nusted dictionary
        "chemistry":35,
        "urdu": 45,
        "english" : 45
    }
}'''

# distionary methood
'''print(subject.keys()) '''             # dict.keys() and dict.values()

'''subject1={
    "name": "rajab ",
    "class": "2year",
    "marks" : "60%"
}
print(subject1.get(2))'''     # subject.get() return the key according to value.
 
'''subject ={
    "name": "rajab ",
    "age" : "20",
    "height" : "5.6",
}

subject.update({"height" : "5.7" })

print(subject)          # subject.update ({}).
'''

# set in python

set1= {1,2,3,4,5 }
set2=  {3,4,5,6,7}

print(set1.intersection(set2))

# question ::You are given a list of subject for students. assume one classroom is required for 1 subject. how many classroom are needed by all student. 

#answer: 
subject= {
    "python", "c++", "html", "javascript", "c++", "python", "java", "python", 
}
print(subject)
print(len(subject)) 

# enter marks of three subject and store in distionary 

# answer:  

subject1 =  int(input("English: ",))
subject2 =  int(input("Math: ",))
subject3 =  int(input("Urdu: ",))

dict=  {
    "English": subject1 ,
    "Math": subject1,
      "Urdu": subject1, 
    }
print(dict)