
#1.Function as a Parameter

# def greet(name):
#     return f"Hello, {name}!"

# def call_func(func, value):
#     return func(value)

# print(call_func(greet, "Sachin"))

#2.Function as a Return Value
# def outer():
#     def inner():
#         return "Inner Function"
#     return inner

# f = outer()
# print(f())  # Output: Inner Function

#3. Closures
# A closure is a function that remembers variables from its enclosing scope even if the outer function has finished executing.

# def make_multiplier(x):
#     def multiplier(n):
#         return x * n
#     return multiplier

# double = make_multiplier(2)
# print(double(5))  # Output: 1

#4. Decorators
# Decorators are functions that modify the behavior of other functions.

# def decorator(func):
#     def wrapper():
#         print("Before Function Call")
#         func()
#         print("After Function Call")
#     return wrapper
# @decorator
# def say_hello():
#     print("Hello!")
    
# say_hello()

# 5. map(), filter(), reduce()
# These are built-in higher-order functions for transforming data.

#map() → applies a function to every item in an iterable
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)  # [1, 4, 9, 16]

#filter() → filters items based on a condition

# nums=[1,2,3,4,5,6,7]
# even=list(filter(lambda x: x % 2 == 0, nums))
# print(even)

#reduce() → reduces iterable to a single value

# from functools import reduce

# nums = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, nums)
# print(product)  # 24
