##1 Converting an integer into Decimals
# import decimal

# integer = 10
# print(decimal.Decimal(integer))              # Output: 10
# print(type(decimal.Decimal(integer)))        # Output: <class 'decimal.Decimal'>


##2 Convertin an string of ingegers into Decimals

# import decimal
# string='12345'
# print(decimal.Decimal(string))
# print(type(decimal.Decimal(string)))

##3. reverting a string using an extended slicing technnique

# string= "Python Programming"
# print(string[::-1])

# ##4 Counting vowels in given list
# vowel=['a','e','i','o','u']
# word='wilwkoiurznbvcxzqwqertyuiolmnbvcxzasyubvjml'
# count=0
# for charecter in word:
#     if charecter in vowel:
#         count+=1
# print(count) 

# ii=input('enter :: --')
# vowel=['a','e','i','o','u']
# c=0
# for i in ii:
#     if i in vowel:
#         c+=1
# print(c)


##5.  Counting CONSONANTS
# vowel=['a','e','i','o','u']
# count=0
# wk=input("Enter input--")
# for i in wk:
#     if i not in vowel:
#         count+=1
#     else:
#         pass
# print(count)


# vowel=['a','e','i','o','u']
# input_1='lsdofiuhb'
# c=0
# for i in input_1:
#     if i in vowel:
#         c+=1
#     else:
#         pass
# print(c)

##6 Counting the number of occuranced of a character in a string

# word=['p']
# name=input("Enter:-")
# count=0
# for i in name.lower():
#     if i in word:
#         count += 1
#     else:
#         pass
# print(count)

##7. Writing FIBONACCI Series
# fib=[0,1]
# n=10
# for i in range(n):
#     fib.append(fib[-1] + fib[-2])
    
# print(fib)
# print(','.join(str(e) for e in fib))

# fib=[0,1]
# n=20
# for i in range(n):
#     fib.append(fib[-1] + fib[-2])
# print(fib)

# fib=[0,1]
# fib_num=15
# for i in range(fib_num):
#     fib.append(fib[-1]+ fib[-2])
# print(fib)


##8 Finding the Maxomum Numnber in a lis
# num1=[32,43,34,3,32,45,5,2,23,32,453]
# ma=num1[0]
# for i in num1:
#     if i > ma:
#         ma=i
# print(ma)        
# import statistics
# nn=statistics.
# print(nn)


##9 Finding the minimam Number in a List

# number_list=[22,2,4,32,67,144,15,15]
# min=number_list[0]
# for i in number_list:
#     if i > min:
#         min=i
# print(min)

#print(max(22,2,4,32,67,144,15,15))


##10 Finding the middle Elemrnt in a list
# numlist=[22,2,4,32,67,144,15,15]
# middle_list=int((len(numlist)/2))
# print(numlist[middle_list])

# num=[12,23,3,34,5,25,6]
# mid=int((len(num)/2))
# print(num[mid])

##11 Converting a list into a string

# ls=['P','y','t','h','o','n',20]
# string="".join(map(str,ls))
# print(string)

# name=['S','A','C','H','I','N',10]
# new_name="".join(map(str, name))
# print(new_name)


##12 Adding Two vallue List Element Together
# l1=[12,4,4,2]
# l2=[34,4,34,23]
# new_list=[]
# for i in range(0, len(l1)):
#     new_list.append(l1[i] + l2[i])
# print(new_list)


# l3=[122,3,4,4,5]
# l4=[24,5,5,5,5    ,9]
# emplist=[]
# for i in range(0,len(l3)):
#     emplist.append(l3[i]+ l4[i])
# print(emplist)



##13 Comparig two Strings for ANAFRAMS
# str1="Listen"
# str2="Skinet"
# str1=str1.replace("","").upper()
# str2=str2.replace("","").upper()
# if sorted(str1)==sorted(str2):
#     print("True")
# else:
#     print("False")

# str1="sachin"
# str2="ahcins"
# str1=str1.replace("","").upper()
# str2=str2.replace("","").upper()
# if sorted(str1) == sorted(str2) or len(str1) == len(str2):
#     print("True")
# else:
#     print("False")

##14 Checking For PALINDROME Using Extended Slicing Technique
# str1= "kayak".lower() #A palindrome is a word, number, or phrase that reads the same forward and backward.
# if str1 == str1[::-1]:
#     print("True")
# else:
#     print("False")

##15 Coutning white space in a Strig
# str1="P S S S S"
# print(str1.count(""))


##16. Counting Digitd,Letters, and Spaces in string
# import re
# name = 'Python is 1'
# digitcount  = re.sub("[0-9]","",name)
# lettercount = re.sub("[^a-zA-Z]","",name)
# spacecount  = re.findall("[\s]",name)

# print(len(digitcount))
# print(len(lettercount))
# print(len(spacecount))

# import re
# name = 'Sachin is Engineer 1'
# digitcount  =re.sub("[0-9]","",name)
# lettercount =re.sub("[^a-zA-Z]","",name)
# spacecount  =re.findall("[\s]",name) 

# print(len(digitcount))
# print(len(lettercount))
# print(len(spacecount))


##17. Counting special Characters in s string

# def count_sp_car(string):
#     sp_char= "!@#$%^&*()<>?/\[]:;~"
#     count=0
#     for i in string:
#         if i in sp_char:
#             count+=1
#     return count
# text='?'
# result=count_sp_car(text)
# print(result)

# def sp_car(string):
#     sp_char= "!@#$%^&*()<>?/\[]:;~"
#     count= 0
#     for i in string:
#         if i in sp_char:
#             count+=1
#     return count

# text="&"
# result=sp_car(text)
# print(result)

##18 Removing all whitespace in a string
# import re
# string= "C O D E"
# sp=re.compile(r"\s+")
# result=re.sub(sp,"",string)
# print(result)

# string = "C O D E"
# result = string.replace(" ", "")
# print(result)


# string = 'S F F E'
# ress = string.replace(" ", "")
# print(ress)


##19 Building a Pyramid in Python
# def Pyramid(n):
#     for i in range(n):
#         for j in range(i, n):
#             print(" ",end="")
#         for j in range(i+1):
#             print("*",end="")
#         for j in range(i):
#             print("*",end="")
#         print("")
# Pyramid(5)

# for i in range(10):
#     print("*",end="")
#     for j in range(i, 10):
#         print("*",end="!")


##20 Randomizing the items of a list in Python

# from random import shuffle
# lst=['python','is','easy']
# shuffle(lst)
# print(lst)
#it will gernrate randomly



##21 Create a generator to produce first n prime numbers

# def isprime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def prime_generator(n):
#     num = 2
#     while n:
#         if isprime(num):
#             yield num
#             n -= 1
#         num += 1

# x = int(input("Enter no. of prime numbers required: "))
# it = prime_generator(x)
# for e in it:
#     print(e, end=" ")


## write a program to check if a given number is prime or not
# def prime_no(n):
#     if n < 2:
#         return False  # 0 and 1 are not prime
#     for i in range(2, int(n**0.5) + 1):  # check up to sqrt(n)
#         if n % i == 0:
#             return False  # divisible by i → not prime
#     return True  # no divisors found → prime

# # Input and result
# num = int(input("Enter a number :- "))
# if prime_no(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


##22 Implementing varivle lengh arguments in Python
# def average(*t):
#     avg=sum(t)/len(t)
#     return avg
# result1 = average(32,5,4,4,35,6,63,5)
# print(result1)

# def avg(*k): #(*k) this collect all the argument into tuple
#      avg_all=sum(k)/len(k)
#     return avg_all
# new=avg(10,10,10)
# print(new)

## ** kwargs for dictionary if variable Lengh
# def avg_with_lengh(**kwargs):
#     values=list(kwargs.values())
#     avg = sum(values) /len(values)
#     return avg
# result1= avg_with_lengh(num1=10,num2=20,num3=30)
# #result2= avg_with_lengh(value=10,value=21,value=30)
# print(result1)
# #print(result2)

## 23 Creation instance menber variables in python

# class Test():
#     def __init__(self):
#         # 1st instance variable inside init function
#         self.a=5
#     def f1(self):
#         # 2nd insance variable inside function f1
#         self.b=10
# t1=Test()
# t2=Test()
# t1.f1()
# #3rd instance variable 
# t1.c=15
# print(t1.__dict__)
# print(t2.__dict__)


##24 Addition using Lambda functions 
# Lambda function to add two variables
# f = lambda a,b : a+b 
# r=f(3,7)
# print(r)
#single
# print((lambda a,b : a+b) (3,7))
#single line
# x=(lambda a,b,c : a+b+c)(3,1,6)
# print(x)

##25 Finding factorial using lambda funciton

# f=(lambda n :1 if n==0 else n*f(n-1))

# print(f(5))

# num=int(input("Enter a Number:-"))
# factorial = 1
# if num < 0:
#     print("Sorry factorial does not exits for negative numbers")
# elif num == 0:
#     print("Factorial is 0 to 1")
# else:
#     for i in range(1,num +1):
#         factorial = factorial * i
#     print(f"Factorial of {num} is ",factorial)
    
## 26 list compressoin (to create a list in single line)
#list of even numbers
# l1=[2*e for e in range(1,10)]
# print(l1)
'''
List comprehension is a concise and expressive way to create 
lists in pyhton it provides a more compact syntax for generation 
lists compared to using tradaitional loops.
'''

# to create a list of even numberrs from given list
# list1=[23,56,65,22,62,32,65,76,33,99]
# l3=[e for e in list1 if e%2==0]
# print(l3)

###27 
# what is the use of split and join function of str?
# s='what is right in your mind is right in your world'
# #split - to convert string into of string
# s1=s.split(" ") #split string into list of word
# print(s1)
# s1=s1[::-1] # reverse the list of words
# print(s1)
# print(" ".join(s1)) # join the reversed list back into a string


# str1='Hello Mr Sachin Naiknaware'
# s1=str1.split(" ")
# print(s1)

# s1=s1[::-1]
# print(s1)

# print(" ".join(s1))

##28 Global and Local variable

# x=10 # global variable
# def f1():
#     global x
#     x=15 #globale variable updated 
#     y= 10
#     print("x=%d y=%d"%(x,y))
# f1()
# print(x)




#tr1="Hello world"
# count=0
# for i in str1:
#     if i in 'o':
#         count+=1
#     else:
#         pass
    
# print(count)

#print(str1.count('o'))
# count=0
# i=0
# while i< len(str1):
#     if str1[i] == 'o':
#         count+=1
#     i+=1
# print(count)


#print(str1.count('o'))
# count=0
# for i in str1:
#     if i == 'o':
#         count+=1
# print(count)


## 29 Global function 
# global function returns dictionary
#you can use the globals() function to access or modify global variables
#within a function variable
# x=5
# def fun():
#     x=10
#     d=globals()
#     print("local x=%d global x=%d"%(x,d['x']))
# print(fun())


## 30 Types conversion basics

# x=int('123')
# a=float('1232.2')
# b=complex('3+9j')
# c=str(12)
# d=bool('True')
# e=bin(25)
# f=oct(25)
# g=hex(25)
# h=ord('A')
# i=chr(98)
# print(x,a,b,c,d,e,f,g,h,i,sep="\n")

## 31 Type conversion
# x=5
# print(type(x))
# s1='123'
# print(type(s1))
# print(str(x) + s1)
# print(x + int(s1))


## 32 What is Python decorator?
# Decorator is Powerfull tool that allow you to modify or
#enhance the behaiver of function or methods without changing their actual code

# Decoratoe is function that takes another function as input and return 
#new function with added functionallity

# def welcome(fx):
#     def mfx(*t,**d):
#         print("Before hello function")
#         fx(*t,**d) # *args to take arguments as tuple , **kwards to take argument
#         print("Thanks for using the function")
#     return mfx

# #decorator function arguments
# @welcome
# def add(a,b):
#     print(a+b)
# @welcome
# def hello():
#     print('Hello !')
# add(10,10)
# hello()



### decorators is function that takes another function as input and some extra behaiver to it 
### and returns a new fuction  - without changing the original function code .

#class  Decorator 

# class Calculator:
#     def __init__(self,func):
#         self.funciton = func
        
#     def __call__(self,*t,**d):
#         result=self.function(*t,**d)
#         return result**2
    
# @Calculator
# def add(a,b):
#     return a+b
    
# add(10,10)



#1) write a functions which does multiple numbers addition and retunn ans 

#1. Method one
# def addition(a,b,c,d,e):
#     print(a+b+c+d+e)
# print(addition(12,2,23,323,3))

#2. 2 Method
# def addition(*args):
#     return sum(args) 
# print(addition(32,333,3,33,3,33,3,3)) 



#write a program which finds area of rectange and circle  

# Area of Rectangle	Area = l × w	l =  length
# w  = width
# Area of Square	Area  = a2	a = sides of the square
# Area of a Triangle	Area = 1/2 b×h	b = base
# h = height
# Area of a Circle	Area = πr2	r = radius of the circle

# def area_reactangle(lenth,width):
#     return lenth*width
# print(area_reactangle(3,3))

# def area_cicle(redius):
#     PI=3.149
#     return PI * redius ** 2

# print(area_cicle(10))


# def area(shape, height=0, width=0, radius=0):
#     PI = 3.14159
#     if shape == 'rectangle':
#         area_rectangle = height * width
#         print(f"Area of rectangle is: {area_rectangle}")
#     elif shape == 'circle':
#         area_circle = PI * radius ** 2
#         print(f"Area of circle is: {area_circle:.2f}")
#     else:
#         print("Invalid shape. Please choose 'rectangle' or 'circle'.")

# area('rectangle', height=10, width=10)
# area('circle', radius=23)



# def area(shape):
#     pi=3.14159
#     if shape == 'rectangle':
#         height=eval(input("Enter hight"))
#         width=eval(input("Enter width"))
#         area_reactangle = height * width
#         return area_reactangle
#     elif shape == 'circle':
#         redius=eval(input("Enter a redius "))
#         area_circle = pi * redius ** 2
#         return area_circle
#     else:
#         return "Envalid shape"
# t1=area('circle')   
# print(t1)     



#Find all number divisible by 8 and 14 in under 

# def divisible_by_8_14(limit):
#     l1=[]
#     for i in range(1,limit):
#         if i % 8 == 0 and i % 14 == 0:
#             l1.append(i)
#     return l1
# print(divisible_by_8_14(100))            

# import statistics 

# l=[3,4,5,5,4,24,45]
# print(statistics.geometric_mean(l))


#ask user to enter an number and you write program find whether that number float or integer or positive or nigative or even or odd
# user=input("Enter a Input :-")

# for i in user:
#     print(type(i))
#     convert=int(i)
#     if convert % 2 == 0:
#         print('Number is even {i}')
#     else:
#         print("Number is odd {} ")



# def divisible_by_6_and_14(num):
#     output=[]
#     for i in range(1, num):
#         if i % 6 == 0 and i % 14 == 0:
#             output.append(i)

#     return output
# a = divisible_by_6_and_14(1212)
# print(a)

