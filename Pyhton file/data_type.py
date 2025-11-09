# String Concatenation 
# a="SACHIN"
# B="NAIKNAWARE"
# C=a+" "+B
# print(C) 

# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# age =23
# txt= f"My age is age  {age}"
# print(txt)

#Escape Carectors
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value	


#Booleans

# In programming you often need to know if an expression is True or False.

# You can evaluate any expression in Python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

# print(5>=2)
# print(6>=8)
# print( 7 == 7)

# a=200
# b=100

# if a >b:
#     print("A IS BIG ")
# else:
#     print("B IS BIG")

# print(bool("SACHIN"))
# print(bool(5))


#synatax
#print("First")

#Data types

#python have built-in-datatypes

# 1 str => where we can store text type data
        # it is swquences of charactiors enclosed within single quotes and double quotes.
        
# x='sachin'
# print(x)

# my_first_var="Sachin"
# print(my_first_var)



# 2 Numric Data-types

#1.int
#2.float
#3.complex

#  2 int=> int represent any whole number,where we store numric datatype.
         #is type of number that does not have frational part it can be any whole number 
#d=10
#print(d)

#  3 float   => represent  real number with decimal point
           #float use when more percision is needed than integer especially representing 
           #real world quantities like measurement or scientific data  
#s=4.4
#print(type(s))



#  4 complex =>complex number is type of number that has two parts the first on is real part and second one is imaginary part 
   
# s=2+4j
# print(type(s)) 
# print(s)

#  5  list   => list is collections of items that are ordered, mutable (can be changed), allow to store duplicate value
          #we can multiple vallue in single variable
          #store diffrent type of data

#k=[1,2,4,5]
#print(k)


#  6  tuple  => tuple is similor to list but once created we cant modify add edit & modify 
               #allow duplicates
               #immutable
               #orderd  means we access them by index
               #we can store any type of data like str,int, float
               
#t=(1,2)
#print(type(t))   


#  7 range   => range is datatype represent sequencce of numbers used in loop speacly in for loop itreat over series of numbers
             #range function generate a series of number but it does not store in memory
             #range is not list
             #you can convert to list
             #immutable once created cannot modify
             #range function have three argumrnts  

#for i in range(1,100, 2):
#  print(i)


#  8   dict  => dictionry data type is muttable(changeble), unordered collection of key value pairs, each key is unique in dict is associated with a specfic value 
              # you can access,modify,add or remove key vallue from dictionary
              #unordered items not stored in oredered 
              #muttable
              #Unique keys: Each key in a dictionary must be unique.
              # value can be any type
#s={1:"sachin",2:"s"}
#print(s) 
 

# 9    set   =>  set is unordered collection of unique elements dont store duplicate itmes
            #unoredered 
            #unique set cannot allow duplicate values any duplicate value added to set automaticly delet
            #mutable
            #No indexing 
#s={'sacjom'}
#print(s)
#d=set([1,2,3,4])
#print(d)


# 10  Boolean => boolean datatype used for truth value it has two possible vallue
            #True
            #False
            #used conditional statment boolean typically used in if, while expresion to contorl flow of the program 
            #results of comparisons
            
#e=2
#t=2
#if e==t:
# print("Equal")
#else:
# print("not equal")
 
#a= True
#b= False
#print(a and b)
#print(a or b)
#print(not b)


#mutable data-types
#1=list
#2=set
#3=Dictionaries

#immutable data-types
#1=Tuples
#2=string
#3=integr



#built-in types
#1. booleans

# logical operations like and, or , not only perform on booleans

#2. Numbers
#     -int  :-integer number
#     -float :-
    
# #3. Strings
#     -str
#     -bytes

# #4. Sequences of collections
#     -list
#     -tuple
#     -set
#     -dict
    
    
# #immutable Data-types
# -int,float,complex,long
# -str
# -bytes
# -tuple
# -frozenset

# #mutable Data Types
# -bytearry
# -list
# -set
# -dict

# s=b'sachin'
# print(type(s))

# s={1,2,5,7,4,4,6}
# print(s)
# print(type(s))
 
# import math

# a=2
# b=4
# #print(a ** b)
# p=math.pow(a,b)
# print(p)

# p=None
# print(p)

# X=None
# if X is None:
#         print('Not a surprize')

# type converting type between datatype
# a= '123423'
# b=int(a)
# print(type(b))

# a='23.4'
# B=float(a)
# print(B)

# var='Hellow Sachin'
# print(set(var))
# print(list(var))
# print(tuple(var))

# normal= 'foo\nbar'
# print(normal)


