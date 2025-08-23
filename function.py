

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


# def sum_vallue(a,b,c):
#     d=a+b+c
#     print(f"Total Sum :-{d}")
# a=sum_vallue(10,10,10)


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


##fibonacci series
# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(2,n):    
#         c=a+b
#         a=b
#         b=c
#         print(c)
        
# print(fibonacci(10))

# for i in range(1,10):
#     if i % 2 == 0:
#         print('Even :-',i)
#         if 2 == i in 6:
#             print('6')
    
#     else:
#         print('Odd :-',i)

