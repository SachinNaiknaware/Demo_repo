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


###Exception handling म्हणजे प्रोग्राममध्ये येणाऱ्या चुका (errors) नीट हाताळणे, जेणेकरून प्रोग्राम अचानक बंद होणार नाही.
# Common Exceptions (सामान्य चुका)
# Python मध्ये वारंवार येणाऱ्या काही exceptions:

# ZeroDivisionError → शून्याने भाग करताना

# ValueError → चुकीचा डेटा प्रकार दिला असताना

# IndexError → यादीतील चुकीचा index वापरला असताना

# KeyError → dictionary मधील key अस्तित्वात नसताना

# TypeError → चुकीचे प्रकार एकत्र वापरले असताना

# Exception Handling (चुका हाताळणे)
# Exception handling साठी try-except ब्लॉक वापरतो.

#if error come add in try 
# try:
#     x=10/0
# except ZeroDivisionError:
#     print("10 NOT divisible by 10")



# Try (प्रयत्न)
# try ब्लॉकमध्ये error येऊ शकतो असा कोड लिहिला जातो.

# # except except ब्लॉकमध्ये error आल्यास काय करायचं ते लिहिलं जातं.
# try:
#     x=int("abc")
# except ValueError:
#     print("X is string")



#Try-Except-Else
# जर try मध्ये error आला नाही, तर else ब्लॉक चालतो.
# try:
#     x=5/1
# except ZeroDivisionError:
#     print("Error come")
# else:
#     print("Error not come")



# Finally (नेहमी चालणारा ब्लॉक)
# Error आला किंवा नाही, finally ब्लॉक नेहमी चालतो.

# try:
#     x= open("fgdas.txt","r")
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("0 Error")

# Raising Exceptions (स्वतः Exception उचलणे) raise वापरून आपण manually exception तयार करू शकतो.
# we can creat a manually error also 
# def check_age(age):
#     if age < 18:
#         raise ValueError("Age 18 below")
#     else:
#         print("Valide age")
# age=int(input("Enter Enput :---"))
# print(check_age(age))


# Assertion (अट तपासणे)
# assert वापरून अट खरी आहे की नाही हे तपासतो.
# x = 10
# assert x > 0,"X Ia bigger than 0"

# import Modules_Packages
# print(Modules_Packages.greet("Sachin"))
