#print("sachin")
#to check python version
#python --version
#check the version usinf sys Module
"""
import sys 
print(sys.version)

#Indetation 
if 5 > 2:
 print("Five is greater than two!")
print("Five is greater than two!")

#casting

x=int(3)
y=str(3)
z=float(3)
print(x)
print(y)
print(z)
print(type(y))

#Case Sensitive
a=4
A="SACHIN"
print(a)
print(A)

#assign Multiply vallue
x,y,z = "Orange","Banana","Chery"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x=y=z="SACHIN"
print(x)
print(y)
print(z)

#Unpack of Collection 

Fruits=["Banana","Mango","Chery"]
a,b,c=Fruits
print(a)
print(b)
print(c)


#Global Variable
s="Naiknaware"
def sn():
 print("Sachin" + s)
sn()


#Data type
x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None  #Nonetype

print(x)

#DATA TYPES
#INT Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
S=9
print(S)

z = -3255522
print(z)

#Float Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

k=5.5
print(type(k))

#complex
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

f=9j
print(f)

#type Conversion
a="sachin"
b=78
s=float(b)
print(s)
#Type conversion works convrt a data type
""" 
# Random    Python does not have a random() function to make a random number,
#  but Python has a built-in module called random that can be used to make random numbers:
"""
import random
print(random.randrange(0, 10))
"""

#Casting 
#There may be times when you want to specify a type on to a variable.
# # This can be done with casting. Python is an object-orientated language, and #
# as such it uses classes to define data types, including its primitive types.
"""

x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

"""
"""

for x in "BANANA":
    print(x)   
    """

#String Slicing from start 

sa="SACHIN NAIKNAWARE"
print(sa[7:17])
print(sa[:17])
print(sa[7:])
#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])