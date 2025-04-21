# integer methods
num1= 10
num2= 20
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1//num2)
print(num1**num2)

# float methods
# round method
print(round(10.5))
print(round(10.4))
print(round(10.51))

# absolute method

# absolute value is always positive
print(abs(-10))

# positive value is always positive
print(abs(10))

# string methods

# lower()
names="shahmeer"
print(names.lower())

# upper()
print(names.upper())

# replace

replaces ="shahmeer,zian"
print(replaces.replace("zian","ali"))

# split

split="shahmeer,Ali,Zian"

print(split.split(","))

#  strip

strip ="  shahmeer   "

print(strip.strip())

# list methods
list=[ "apple","banana","orange"]

# append
list.append("grapes")


# insert
list.insert(1,"mango")
print(list)

# pop

removed = list.pop() 
print(list)           
print(removed)          

list.pop(0)  
# sort
alphabet = ['e', 'a', 'd', 'c', 'b']
alphabet.sort()
print(alphabet)

# reverse

alphabet.reverse()
print(alphabet)
# tuple methods

t = (1, 2, 1, 3, 1)
print(t.count(1))  

t = (1, 2, 3, 2, 4)
print(t.index(2))  

# dictionary methods

# key
person = {"name": "Ali", "age": 20}
print(person.keys())  


# values
print(person.values())

# items
print(person.items())

# clear
person.clear()
print(person)

# get
print(person.get("name"))

# set methods
# Method | Kaam kya karta hai
# add() | Nayi value add karta hai
# remove() | Specific value hataata hai (error if not found)
# discard() | Value hataata hai safely (no error)
# pop() | Random value hataata hai
# clear() | Set empty kar deta hai
# union() | Do sets ko combine karta hai
# intersection() | Common values deta hai
# difference() | Unique values of set A from set B


set = {1, 2, 3}
# print(set[0]) # Error not allowed index