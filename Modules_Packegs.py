# What is a Module?
# A module is a single Python .py file that contains functions, classes, or variables 
# that you can reuse in other programs.

# def hello(name):
#     return f"Hello,{name}!"

# import greetings
# print(greetings.hello("Sachin"))

# Types of Modules
# Type	       Example
# Inbuilt	       math, os, sys, random
# External	   pandas, numpy, matplotlib
# User-defined   Your own .py files

#os
# import os
# print(os.getcwd()) #current directory
# print(os.listdir()) #lsit of directory

#sys

#import sys  #(System-specific parameters)
# print(sys.path)
# print(sys.version)

#math   
# import math
# print(math.sqrt(16))  # 4.0
# print(math.pi)  #3.141592653589793

#string
    # import string

    # print(string.ascii_letters)
    # print(string.digits)
    
    
#Create Your Own Module
# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b


# What is a Package?
# A package is a directory that contains a collection of modules and a special file __init__.py.


#practical pending
# ------------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Closures
#A closure is a function that remembers variables from its enclosing scope even if the outer function has finished executing.

# def make_multiplier(x):
#     def multiplier(n):
#         return x * n
#     return multiplier

# double = make_multiplier(2)
# print(double(5))  # Output: 10



# Create environment
# python -m venv myenv

# # Activate
# source myenv/bin/activate  # macOS/Linux
# myenv\Scripts\activate     # Windows

# # Install packages
# pip install flask

# # Save dependencies
# pip freeze > requirements.txt

# # Deactivate
# deactivate
