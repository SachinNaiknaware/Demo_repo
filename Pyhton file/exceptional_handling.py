# Common Exceptions
# Exception Type	    Description
# ZeroDivisionError	Division by zero
# ValueError	        Wrong value type
# TypeError	        Invalid operation on types
# IndexError	        Index out of range
# KeyError	        Missing dictionary key
# FileNotFoundError	File does not exist
# AttributeError	    Calling undefined attribute
# ImportError	        Module not found

#basic exception 
# try:
#     c= 10/0
# except ZeroDivisionError:
#     print("10 can not devide 0")

#Try-Except-Else

# try:
#     s=int(input("Enter a Number:-"))
# except ValueError:
#     print("Enter Only Numric valle")
# else:
#     print("Your Number",s)

# Finally Block
# finally runs no matter what (used for cleanup).

# try:
#     f =open("sachin.txt","r")
#     print(f.read())
# except FileNotFoundError:
#     print('File not found')
# finally:
#     print("Always runs")

# Raising Exceptions
# You can raise exceptions manually using raise.

# def check_age(age):
#     if age<0:
#         raise ValueError("Age cannot be negative")
#     else:
#         print("Age is Valid")

# check_age(10)
# check_age(-1)

# Assertions
# Use assert to debug by checking conditions.

# x = 10
# assert x > 0, "x must be positive"
# assert x < 5, "x must be less than 5"