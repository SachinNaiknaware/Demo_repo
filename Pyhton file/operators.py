#  Types of Python Operators
#     Type	    Description	                  Example
# 1. Arithmetic	Perform math operations	      +, -, *, /
# 2. Assignment	Assign values to variables    =, +=, -=
# 3. Comparison	Compare two values (True/False)	==, !=, >
# 4. Logical	Combine conditional statements	and, or, not
# 5. Bitwise	Work on bits	                &, `
# 6. Identity	Compare memory locations	    is, is not


# # Operators 
# # +	    Addition	    x + y	
# # -	    Subtraction	    x - y	
# # *	    Multiplication	x * y	
# # /	    Division	    x / y	
# # %	    Modulus	        x % y	
# # **	Exponentiation	x ** y	
# # //	Floor division	x // y

# #Assignment Operators

# x=5
# x+=5
# print("+" ,x)

# s=5
# s-=2
# print("-" ,s)

# k=5
# k*=5
# # print("*", k)

# # o=30
# # o/=5
# # print("/",o)


# # Comparison Operators
# # Comparison operators are used to compare two values:
# # == Equal
#  != Not Equal
#  >  Greater than
#  <  Less than
#  >=  Greater than or equal to
#  <= Less than or equal to

#  Evry time return true or false

# Logical Operators
# Logical operators are used to combine conditional statements

#and  Returns True if both statements are true	x < 5 and  x < 10
# #or  Returns True if one of the statements is true	x < 5 or x < 4
# #not  Reverse the result, returns False if the result is true

# #Identity Operators
# Identity operators are used to compare the objects, 
# not if they are equal, but if they are actually the same object, with the same memory location:
#is Returns True if both variables are the same object	x is y
#is not  Returns True if both variables are not the same object	x is not y

#  Membership Operators
# Membership operators are used to test if a sequence is presented in an object:
#in Returns True if a sequence with the specified value is present in the object
# #not in  Returns True if a sequence with the specified value is not present in the object

# x=['SACHIN','Naiknaware']
# print('SACHIN' in x)

# x=['SACHIN','Naiknaware']
# print('JIVAN'not in x)

#The precedence order is described in the table below, starting with the highest precedence at the top:

# Operator	Description	Try it
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR


#ternary  operators

# X=10
# results= "Positive" if X > 0 else "Nigative or ziro"
# print(results)

##Bitwise Operators

# a=5
# b=3

# result=a&b
# print(result            )






##floor division
# a=10
# b=2
# print(a/b)

# a=10
# b=3
# print(a//b)

# c=10
# b=4
# print(c//b)




##Exponentiation (power)

# a=3
# b=3
# print(a **b)

# a=4
# b=4
# print(a**b)

# a=5
# b=5
# print("Power is:-",a**5)




##modulus operators 
# a=9
# b=81
# print(a%b)




##assiment operators

#add and assign
# a=2
# a+=3
# print(a)



#subtract and assign
# a=10
# a-=2
# print(a)

#multiply and assign

# a=2
# a*=2
# print(a)

#divide and assign
# a=100
# a/=2
# print(a)

#floor devide and assign

# a=15
# a//=2
# print(a) normal division print result print 7.5 but floor dicide results showing 7 
# bcz floor divide ans will whole number not float valuur aither equal or less t
#this case showing lees means 7


#Exponentiate and assign
# x=2
# x**=3
# print(x)
#it works 2*2*2 ans is 16


#Modulus and Assign 
# x=12
# x%=5
# print(x)
#it will show the reminder
# x=10
# for i in range(x):
#     if i % 2:
#         print("IS even  NUMBER ",i)
#     else:
#         print("is odd number:-",i) 


## comparison operators

#equal to  ==
# x=10
# b=10
# if x==b:
#     print("X and B is Equal")

# x=10
# b=10
# if x!=b:
#     print("x and b is  not equal ")
# else:
#     print("is equl")

#greater than
# x=5
# v=1
# if x>v:
#     print("X IS BIG")
# else:
#     print("v is small")


#lesser than

# x=5
# v=10
# if x<10:
#     print("v is big")


#greater than equal to

# x=50
# v=10
# if v>=x:
#     print("x is big")
# else:
#     print("v is big number")

# #lesser than equal to
# a=10
# b=10
# if a<=b:
#     print("a is big ")
# else:
#     print("b is big")


#menbership operators
# #in
# l=[1,2,3]
# print(1 in l)
#return true if value is present

#not in 
#rerturn true if vallue is  not present
# x=[1,2]
# print(1 not in x)



##identify operators

#is 

# x=1
# w=1
# print(x is w)
# s='Munmbai'
# k='munbai'
# print(s is k)

#is not
# x= 10
# y=9
# print(x is not y)

# x=10
# y=10
# print(x is not y)


##ternary operator 
#ternary operator is conditional operators

# results=10
# results= "even" if results ==10  else "odd"
# print(results)

#bitwise operators
# &  :-  Bitwise AND,  
# |  :-  Bitwise OR,  
# ^  :-  Bitwise XOR,    
# << :-  Left Shift,  
# >> :-  Right Shift,

#in python bitwise operators used to perform operation on at the bit level
#this operation work with the individual bits of integer



# division
# print(12/3) #diveds two number and return a flaot

#moduls 
#modules return the reminder after division

# print(3%9)
# print(10%20)
#print(10%2)
# it will print reminder

#exponentiation **
#raises a number to the power of another
# print(2 ** 5)
#print(2*2*2*2*2)
#2 ला चार वेळा स्वतःशी गुणणे — 2 × 2 × 2 × 2 = 16

#floor division 
#divides and return the largest integer hass less than or equal to the result 
# print(12//5)
#12 ला 5 ने भागून पूर्णांक उत्तर काय येईल Floor division म्हणजे भागाकाराचे पूर्णांक उत्तर — दशांश (decimal) भाग काढून टाकतो.



