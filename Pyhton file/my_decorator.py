## decorates

## decorater is function that takes another funciton as inpunt and return as a new function with added functionallity

## decorators used for 

# logging 
# acces control
# timing execution
# memoization (catching)
#valiadation

#steg 1
# def greet_decorator(func):
#     def wrapper():
#         print("Hellor From the decorators !")
#         func() # calling original function
#         print("Good by from the decorators!")
#     return wrapper
# #steg 2 apply decortor using @ synatax
# @greet_decorator
# def say_name():
#     print("My name is Sachin")
    
say_name()