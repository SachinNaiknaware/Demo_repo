##1. Converting an integer into Decimals

#import decimal   #this module, which provides decimal data type for precise decimal arithmetic. itcommonly 
#financial or scientific calculations where floating point precision issue are unacceptable.
#integer =10 # a integer is variable
#print(decimal.Decimal(integer))
#this convert the integer 10 into a decimal object
#internaly, it wraps the number in a Decimal class
#print(type(decimal.Decimal(integer)))
#this print the decimal representation of the number

# So decimals is used when accuracy matters especially in money calculations, rounding or scientific values.
#----------------------------------------------------------


##2. Converting an String of integers into Decimals

# import decimal

# string = '12345' # it is varible
# print(decimal.Decimal(string))  #converting string object to decimal 
# print(type(decimal.Decimal(string))) # it print ouput in decimal 


#-----------------------------------------------------------
##3. Reversing a String using an Extended Slicing Technique

# st= 'Python Programming' #it is string
# print(st[::-1])
# this is string slicing operation 
#the format is st[start:stop:step]
#[::-1] means start form end


#-----------------------------------------------------------
##4. Counting VOWELS in a Given World
# vowel =['a','e','i','o','u']# list of vowel
# word = 'programming' # input variable
# count= 0  #counter variable
# for  character in word: #loop thru check each letter in word
#     if character in vowel: #check the if letter is vowels
#         count+=1 # if yes icrease count by 1 
# print(count) #print total number of vowels
#-----------------------------------------------------------


##5.Counting Consonants in given word

# vowel =[ 'a','e','i','o','u'] # list of vowel
# word = 'programming' #input variable
# count = 0 # counter variable
# for i in word: # check each letter in word
#     if i not in vowel: #check the latter is not vovels 
#         count+=1 # if yes increse count by 1
# print(count) #print  total number of consonants
#----------------------------------------------------------

##6. Counting a number of occurances of a character in a String
# word ='programming'  #this is input string
# character ='g' # g is character target character
# # looking how many time g present in word
# count=0  #it will keep record how many times g appears
# for i in word: # check each character in word
#     if i == character: #check if equal to g
        
#         count+=1
# print(count)
#----------------------------------------------------------

#check even or odd
# for i in range(1,100):
#     if i % 2 ==0:
#         print(f'{i}:-EVEN')
#     else:
#         print(f'{i}:-ODD')
#----------------------------------------------------------

##7. Writing FIBONACCI Series
# fib=[0,1]

# n=10
# for i in range(n):
#     fib.append(fib[-1] +fib[-2])
# print('+'.join(str(e) for e in fib))





###8.# create a dictionary where the numbers from str1 are keys
# and if number is even the value of it should be square of it.
# if number is odd the value of it should be cube of it.
# use for loop

###str1 = "asdf23dfg98fgs6ks4   jd7"

# dict1={}
# for i in str1:
#     if i.isdigit():
#         if int(i) % 2 == 0:
#             dict1[int(i)] = int(i) ** 2
#         else:
#             dict1[int(i)]= int(i) ** 3
            
# print(dict1)
# Sample Output: {2:4, 3:27, 9:729, 8:64, 6:36, 4:16, 7:343}



###9. create a tuple of ascii's of given charecters arranged in a such a way
# that all the charecters whose ascii is even are at start
# and if the ascii is odd all are at end.
# L1 = ['a', 'k', 'P', 'A', 'I', 'o', 'Z']

# t1=[]
# for i in L1:
#     temp = ord(i)
#     if temp % 2 ==0:
#         t1.insert(0,temp)
#     else:
#         t1.append(temp)
        

# t1 = (90,80,97,107,65,73,11)# sample output
# print(t1)


## 10.  take two input from user as a numbers use first number as start second number as range and 
# get the numbers which are divisibale by 3 and 5

# first=int(input("First Number:-"))
# last=int(input("last Number:-"))

# L1=[]


# for i in range(first,last):
#     if  i % 3 == 0 and i % 5 == 0:
#         L1.append(i)
#     else:
#         pass

# print(f'This numbers are diviseble by 3 and 5 {L1}')
#This numbers are diviseble by 3 and 5 [15, 30, 45, 60, 75, 90]


##11 
# get the vowels from str2 and append them in list
# make sure the charecters in list will not be duplicated.
# str2 = 'sghcnqhjvdyuevegi783e1dbvg   3sus'
# vowels=['a','e','i','o','u']
# list1=[]
# for i in str2:
#     if  i  in vowels and i not in list1:
#         list1.append(i)
#     else:
#         pass

# print(list1)

##12 write a function which takes an argument as string and returns you asending order
# the same string in asending order

# def ascending_string(string:str):
#     l1 = sorted([x for x in string])
#     asc_str = ''
#     for i in l1:
#         asc_str += ''.join(i)
#     print(l1)
#     print(asc_str)
    
# ascending_string("fghgfdxdcgytrt")

# a=50
# b=30
# print(a*b)


##13. squares of range from 1 to 6 using list confrention
# squares = [x*x for x in range(6)]
# print(squares)

#even or odd number
#for i in range(1,20):
    # if i % 2 == 0:
    #     print(f'This is Even No :{i}')
    # else:
    #     print(f'This is Odd No :{i}')

#  #if Statements   
# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')
     
     
## 14. write a functin which takes a  two parameter as number the first parameter will be as
# start of range and second number is end of range you have to find armstrong number between range
# def armstrong_number(first, last):
#     print(f"Armstrong numbers between {first} and {last} are:")
#     for num in range(first, last + 1):
#         digits = str(num)
#         power = len(digits)
#         total = sum(int(digit) ** power for digit in digits)
#         if num == total:
#             print(num)
# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
# armstrong_number(start, end)


## 15. write a function which takes argument as list it transferm this list in such order all the even numbers will be at start
# all the odd number at the end
# even=[]
# def sachin(n):
#     for i in range(1,51):
#         if i % 2 ==0:
#             even.insert(0,i)
#         else:
#             even.append(i)
    
# results=sachin(1)
# print(even)

##16. create a calculator

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         return self.num1 + self.num2

#     def subtract(self):
#         return self.num1 - self.num2

#     def multiply(self):
#         return self.num1 * self.num2

#     def divide(self):
#         if self.num2 != 0:
#             return self.num1 / self.num2
#         else:
#             return "Cannot divide by zero"

#     def modulus(self):
#         return self.num1 % self.num2

#     def power(self):
#         return self.num1 ** self.num2

# # --- Usage ---
# # Taking input from user
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# calc = Calculator(a, b)

# print("Choose operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
# print("5. Modulus")
# print("6. Power")

# choice = input("Enter your choice (1-6): ")

# if choice == '1':
#     print("Result:", calc.add())
# elif choice == '2':
#     print("Result:", calc.subtract())
# elif choice == '3':
#     print("Result:", calc.multiply())
# elif choice == '4':
#     print("Result:", calc.divide())
# elif choice == '5':
#     print("Result:", calc.modulus())
# elif choice == '6':
#     print("Result:", calc.power())
# else:
#     print("Invalid choice")


# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w,':-' ,len(w))


# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
#  Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)

# print(list(range(1,10)))
# print(list(range(0,10,3)))
# print(list(range(-10,-100,-30)))

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i,a[i])

#print(sum(range(10)) )

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n//x}")
#             break

# for num in range(2, 10):
#     if num % 2 == 0:
#         print(f"Found an even number {num}")
#         continue
#     print(f"Found an odd number {num}")


##17. 
# def fib(n):    # write Fibonacci series less than n   #Each number is the sum of the two previous numbers

#     """Print a Fibonacci series less than n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# # Now call the function we just defined:
# fib(2000)


# def fib(n):
#     a,b= 0,1
#     while a <n:
#         print(a, end=' ')
#         a,b = b, a+b
#     print()

# fib(100)

# x = "awesome"
# def myfunc():
#   print("Python is " + x)
# myfunc()



## Data Types
# x = "Hello World"	#str	
# x = 20	#int	
# x = 20.5	#float	
# x = 1j	#complex	
# x = ["apple", "banana", "cherry"]	#list	
# x = ("apple", "banana", "cherry")	#tuple	
# x = range(6)	#range	
# x = {"name" : "John", "age" : 36}	#dict	
# x = {"apple", "banana", "cherry"}	#set	
# x = frozenset({"apple", "banana", "cherry"})	#frozenset	
# x = True	#bool	
# x = b"Hello"	#bytes	
# x = bytearray(5)	#bytearray	
# x = memoryview(bytes(5))	#memoryview	
# x = None


# import numpy as np
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# print(np.mean((speed)))
# print(np.median(speed))

#friends=10
#addtion 
#friends=friends+1
#friends +=1
#friends=friends-1
# friends -=1
# friends=friends*1
# friends *=1
# friends=friends/1
# friends /=1
# friends=friends**1
# friends **=1
# friends=friends%1
#print(friends)


##.16 write a function which will ask to enter number and return even or odd again it gives prompt back a number again so when 
#we are say to stop 

# def get_even_odd():
#     while True:
#         num = input("Enter a number: ")
#         if num == "stop":
#             break
#         else:
#             if int(num) % 2 == 0:
#                 print("Even")
#             else:
#                 print("Odd")
                
# get_even_odd()

## 17 write function which will take an argument as word tringle or sqr or rectangle  print a vallue

# def get_area_by_shape():
#     list_of_shapes = ['triangle', 'square', 'rectangle']
#     area = 0
#     my_shape = input(f"Enter a shape name [0 for {list_of_shapes[0]}, 1 for {list_of_shapes[1]}, 2 for {list_of_shapes[2]}]:")
#     if my_shape == '0':
#         base = float(input('enter a base value: '))
#         height = float(input('enter a height value: '))
#         area = 0.5 * base * height
        
#     elif my_shape == '1':
#         breadth = float(input('enter a breadth value: '))
#         area = breadth ** 2
        
#     elif my_shape == '2':
#         width = float(input('enter a width value: '))
#         height = float(input('enter a height value: '))
#         area = height * width
#     print(f"The area of {list_of_shapes[int(my_shape)]} is {area}")
    
    
# get_area_by_shape()
        
##.18 write a function for banking application withdrow cash,add user, exit,
# banking_app.py
# users = {}

# def welcome():
#     print("\n🏦 Welcome to the Shivkrupa Banking Application\n")
# def add_user():
#     user_id = input("Enter New User ID: ")
#     if user_id in users:
#         print("❌ User already exists.")
#     else:
#         name = input("Enter User Name: ")
#         balance = float(input("Enter Initial Balance: "))
#         users[user_id] = {"name": name, "balance": balance}
#         print(f"✅ User '{name}' added with balance ₹{balance:.2f}")

# def withdraw_cash():
#     user_id = input("Enter User ID: ")
#     if user_id not in users:
#         print("❌ User not found.")
#         return

#     amount = float(input("Enter Amount to Withdraw: "))
#     if amount > users[user_id]['balance']:
#         print("❌ Insufficient Balance.")
#     else:
#         users[user_id]['balance'] -= amount
#         print(f"✅ Withdrawal of ₹{amount:.2f} successful.")
#         print(f"💰 Remaining Balance: ₹{users[user_id]['balance']:.2f}")

# def show_menu():
#     while True:
#         print("\n--- MENU ---")
#         print("1. Add User")
#         print("2. Withdraw Cash")
#         print("3. Exit")
#         choice = input("Enter your choice (1-3): ")

#         if choice == '1':
#             add_user()
#         elif choice == '2':
#             withdraw_cash()
#         elif choice == '3':
#             print("👋 Thank you for using the Banking Application.")
#             break
#         else:
#             print("❌ Invalid choice. Please try again.")

# if __name__ == "__main__":
#     welcome()
#     show_menu()


##19 write a code for one restorant billigs and everything

# The Maratha House - Restaurant Order System

# menu = {
#     'Kaju Kari': 250,
#     'Paneer Butter Masala': 220,
#     'Veg Kolhapuri': 200,
#     'Dal Tadka': 150,
#     'Butter Naan': 40,
#     'Jeera Rice': 120,
#     'Chicken Handi': 280,
#     'Mutton Rassa': 320,
#     'Solkadhi': 50,
#     'Gulab Jamun': 60
# }

# order = []  # Store user order

# def welcome():
#     print("\n🍽️ !!! Welcome To The Maratha House !!! 🍽️\n")

# def show_menu():
#     print("Here is our menu:\n")
#     for item, price in menu.items():
#         print(f"{item} - ₹{price}")

#     while True:
#         choice = input("\nHi Sir, what would you like to order? (type 'done' to finish): ").strip().title()

#         if choice.lower() == 'done':
#             break
#         elif choice in menu:
#             order.append(choice)
            
#             print(f"✅ '{choice}' added to your order.")
#         else:
#             print(f"❌ '{choice}' is not available in our menu!")

#     # Final bill
#     if order:
#         print("\n🧾 Your Final Order:")
#         total = 0
#         for item in order:
#             print(f"{item} - ₹{menu[item]}")
#             total += menu[item]
#         print(f"\n💰 Total Bill: ₹{total}")
#     else:
#         print("You didn't order anything. Hope to see you again!")

# if __name__ == "__main__":
#     welcome()
#     show_menu()

#bytes data type
# b9=b"asivfhbjsjvhjbfhnm"
# print(b9.find(b'a'))
# print(b9.rfind(b'i'))

#bytesarray
#mutable
# ba=bytearray(b'akfbkvefsdvbkednvk')
# ba[0]=72
# print(ba)

#openpyxel Library
# from openpyxl import Workbook

# file = Workbook()
# ws = file.active

# ws.title = 'Food'  # ✅ Fixed title assignment
# ws['A1'] = 'Name'
# ws['B1'] = 'Roll Number'
# ws.append(['Sachin', 1])        # ✅ append with list
# ws.append(['Shivkumar', 2])     # ✅ append with list
# file.save('student.xlsx')

import sys
# print(sys.version)
# print(sys.gettrace) # get the global debug tracing function
# print(sys.argv)

