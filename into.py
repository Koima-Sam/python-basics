#Basic intro to coding
weeks = 2
print("I'll finish this course in ", weeks,"weeks time")

age = 12.0
name = "Joan"

print(name,"is",age,"years old!")

#casting is specifying the datatype of a particular variable
x = str(age)
if(isinstance(age,str)):
    print("X is  a string")
elif(isinstance(age,float)):
    print("naah it's a float")
else:
    print("none of the above!")

# Multi assigning of variables

a,b,c = 12, "Joe", 33.30

print(a)
print(isinstance(b,str))
print(c)

# Assign single value to multiple variables

d = e = f = 23
print(e,"is equal to",f)

#unpacking values to variables 
fruits = ['Mango','Peaches','Banana','Apples']
g,h,i,j = fruits
print(h)