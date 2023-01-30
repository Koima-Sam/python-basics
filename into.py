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


# Local and global  variables

x = "United" #global

def win():
    x ="City" #local
    print("Manchester",x)

win()


#Python Numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#random numbers
import random
print(random.randrange(1,10))

# Strings - are surrounded by either single or double quotes 
a = '''
This is a multi
line string in
python 
'''

print(a)

#string is like an array and we can loop  through it

b = "Banana"

for c in b:
    print(c)

'''
len() - gets the length of a string
strip() - removes any white space
replace(a,b) - replaces character a with b
split()- returns a list where the text between the specified separator becomes the list items.
'''
#slicing a string

card = "Joker Is Back!"
print(card[:2])
print(card[2:5])


#format() - combines strings with numbers
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# Let's talk about you
jj ="Jemila Jemeli"
age = 22.25

greet = "Hello {}, How old are you?, {} years old?"
print(greet.format(jj,age))
