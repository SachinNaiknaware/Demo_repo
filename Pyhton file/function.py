

###### function 
# function is block of code when we call that time only run

# We can write a function by using the keyword def followed by a function name.
# • The function name is user defined and it is suggested to take a meaningful name while de ning a function
# • The rules for de ning a function is same as giving variable names
# • Within the ( ) you can pass parameters to a function these Parameter are called “Formal parameter”
# Parameters are called input to a function , a function can take multiple Parameter.
# Parameters can be of any datatype Returning values of the statements is Calle “output”
# You can call a function by using the function name and pass parameter in ( ) , these Parameter
# are called “Actual parameter”
# The actual parameter values are copied into formal parameter which acts as input to a
# function they are copied in the same position / order
# When you call a functioning a result is returned you should place that result into another
# variable (or) print it directly
# If you don’t write return in function it'll return NONE
# So, every function returns whether you write it or not.

# def sachin(b):
#     print("sachin")
#     return b
# s=sachin('sa')
# print(s)

# Syntax :
# def fun_name ( par1 , par2, par3 ) : #Formal parameter
# Stat2
# #Statements of function

# return result #Returning result
# fun_name ( par1, par2, par3 )
# return_value = fun_name ( apar1, apar2, apar3 ) #Calling a function

# def sk(a,b,c):
#     if a == b and b==c and a==c:
#         print('Equal')
#     else:
#         print('Value are equal')

# a=sk(2,2,1)



# def vallue(a,b,c):
#     if a==b and b==c and a==c:
#         print(f"Vallue ara equal {a,b,c}")
#     else:
#         print(f"Valle are not equlas{a,b,c}")
#     return 'ok'

# a=vallue(10,1,10)
# print(a)


# def sum(a,b,c):
#     k=a+b+c
#     return f"Sum of vallue is :- {k}"
# print(sum(10,10,10))



# def sum_vallue(a,b,c):
#     d=a+b+c
#     print(f"Total Sum :-{d}")
# a=sum_vallue(10,10,10)


# def v(a=10,b=10):
#     return a+b
# print(v())    

# def s(a,b,c):
#     return a+b+cu
# a=s(10,10,10)
# print(a)

# def add(a=10,b=5,c=5):
#     print(a+b+c)
# a=add(10,5,20)

# def add(a=10,b=5):
#     return a+b
# print(add(10,5))

# def check_even_or_odd(number):
#     if number % 2 == 0:
#         return f"Even:-{number}"
#     else:
#         'odd'
# print(check_even_or_odd(10))        


# for i in range(1,12):
#     def jls_extract_def():
#         return 2


#     if i % jls_extract_def() == 0:
#         print("ev ")
#     else:
#         print("Dfgjk")

# def check_even_or_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(check_even_or_odd(2))  # Output: Even
# print(check_even_or_odd(7))  # Output: Odd


# def check_even_or_odd(number):
#     if number % 2 == 0:
#         return 'even'
#     else:
#         return 'Odd'        
# print(check_even_or_odd(4))
# print(check_even_or_odd(1))


#fibonacci series
# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(2,n):    
#         c=a+b
#         a=b
#         b=c
#         print(c)    
# print(fibonacci(10))

# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(1,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# print(fibonacci(10))    
        
# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
#         #return 'ok'
# print(fibonacci(10))


# for i in range(1,10):
#     if i % 2 == 0:
#         print('Even :-',i)
#         if 2 == i in 6:
#             print('6')
    
#     else:
#         print('Odd :-',i)

# def process(n):
#     y1 = n-8
#     y2 = n+8
#     y3 = n*8
#     y4 = n/8
#     y5 = n%8
#     y6 = n//8
#     print(f'If you make the above operations with {n}, the results will be {y1}, {y2}, {y3}, {y4}, {y5}, {y6}.')
#     return y1, y2, y3, y4, y5, y6
# print(process(5))

# def hell():
#     return 'Hi Sachin Naiknaware'

# print(hell())


## parameter            details
# arg1 .... argn        regular argument
# *args                 unnamed positional argument
# kw1 ......kwn         keyword only arguments
# kwards                the rest of keywords

#function in python provide orgnized, reusable and modular code to perform set of specific actions 

# def sachin():
#     print('My name is sachin')
# print(sachin())

#give defoult value to that  funciton argument
# def greet(greeting='Welcome to out home'):
#     return greeting
# print(greet())



#defining a function  with an arbitrary number of arguments

# def func(*args):
#     # args will be a tuple containing all value that are passed in
#     for i in args:
#         print(i)
    
# print(func(1,2,3,4,5))     

## arbitrary number of keyword arguments 

# def func(**kwards):
#     #kwargs will be a dictionary containing a names as key  and value as value
#     for name, value in kwards.items():
#         print(name,value)
# print(func(value1=1,value2=2,values3=3))


    

##funtion used for reapitative work means म्हणजे कोडचा पुन्हा वापर करता येणारा ब्लॉक.

# def my_fun():
#     print("Hello Sachin ")
    
# print(my_fun())

# def greet(name):
#     print("Hellow",name)
#     return
# print(greet("Sachin"))


#function need to call  like above example greet("SACHIN")


## there is three type of argument 

#functional argument
#positional argument
#keyword arguments 

# def add(a,b):
#     return a+b
# print(add(5,6)) # this is positional argument
# print(add(a=5,b=6)) # this is keyword 


#default if you didnt mentioned argument means
# default argument used

# def greet(name="Sachin"):
#     return name
    
# print(greet())


#Docstrings 
# def s():
#     return '''  Hii i am sachin naiknaware'''
# print(s())


# Scope (व्हेरिएबलची मर्यादा)
# Local Scope: फक्त फंक्शनमध्येच उपलब्ध
# Global Scope: संपूर्ण प्रोग्राममध्ये उपलब्ध

# in side fucntrion or outside function we created on scope when we call inside fucntion only inside local scope only run
# x=10 #Global
# def show():
#     x=5 #local
#     return x
# print(show())

# Functional Programming & Reference Functions
# Functional programming म्हणजे functions वर आधारित कोडिंग.
# Reference functions म्हणजे फंक्शनला दुसऱ्या फंक्शनमध्ये इनपुट म्हणून वापरणे.

# def short(text):
#     return text.upper()
# def greet(func):
#     massage = func("hello")
#     return massage
# print(greet(short))

# Function as a parameter (फंक्शन इनपुट म्हणून)
# एखाद्या फंक्शनला दुसऱ्या फंक्शनमध्ये argument म्हणून देता येते.

# def square(x):
#     return x*x  
# def apply_func(func,value):
#     return func(value)
# print(apply_func(square, 5))


# Function as a return value (फंक्शन आउटपुट म्हणून)
# फंक्शन दुसरे फंक्शन परत करू शकतो.

# def outer():
#     def inner():
#         return "Hello Sachin"
#     return inner
# f=outer()
# print(f())


# Closures (क्लोजर्स)
# Inner function बाहेरच्या फंक्शनचे variables लक्षात ठेवतो, जरी outer function संपला तरी.
# def make_multiplier(n):
#     def multiplier(x):
#         return x * n
#     return multiplier

# double = make_multiplier(2)
# print(double(5))


# Decorators म्हणजे काय?

# 👉 Decorator म्हणजे दुसऱ्या function ला modify (सुधारणे) करणारा function.

# म्हणजेच, तो एखाद्या function मध्ये extra functionality add करतो
# तेही मूळ function चा कोड न बदलता!

# def my_decorator(func):
#     def wrapper():
#         print("Before the function runs 👇")
#         func()
#         print("After the function runs 👆")
#     return wrapper

# @my_decorator   # 👈 हा आहे डेकोरेटर
# def say_hello():
#     print("Hello, World!")

# say_hello()




#1.  map() चा वापर एखाद्या फंक्शनला लिस्ट (किंवा इतर iterable) मधल्या प्रत्येक घटकावर लागू करण्यासाठी केला जातो.
# map function is used to apply function to each element in an iterable (like list, tuple)

# number =[1,2,3,4,5,6]
# def square(x):
#     return x * x
# result=map(square,number)
# print(list(result))


# 2. filter() फंक्शन
# filter() चा वापर एखाद्या अट पूर्ण करणाऱ्या घटकांना ठेवण्यासाठी केला जातो.
# (जे True परत करतात तेच ठेवले जातात.)

# num=[1,2,3,5,6]

# def even(x):
#     return x % 2 == 0
# result=filter(even,num)    
# print(list(result))
#filter() ने is_even() फंक्शन प्रत्येक संख्येवर चालवलं आणि ज्यांचं उत्तर True आलं त्या संख्याच ठेवून नवीन लिस्ट तयार केली.



# 3. reduce() फंक्शन
# reduce() चा वापर लिस्टमधल्या सर्व घटकांना एकाच मूल्यात एकत्र करण्यासाठी होतो.
# (हे functools मॉड्यूलमध्ये उपलब्ध आहे.)

# from functools import reduce
# num=[1,2,3,4,5,6]
# def square(x,y):
#     return x * x
# result = reduce(square,num)
# print(result)



# def sachin(*t):
#     return sum(t)

# print(sachin(10,5,5))

