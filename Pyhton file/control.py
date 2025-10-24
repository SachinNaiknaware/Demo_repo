##control 
#while loop
#1, print number from 1 to 10 using while loop
# a=1
# while a<=10:
#     print(a)
#     a+=1
    
#2. Sum of Even Numbers: Write a code using a while loop to calculate the sum of all even numbers between 1 and 50.
    
# s=2
# even_sum=0
# while s<=50:
#     even_sum+=s
#     s+=2
# print("Sum of Even Numbers:-",even_sum)

#3. Count Down: Write a code using a while loop that counts down from 10 to 1 and prints each number.

# c=10
# while c>=1:
#     print(c)
#     c-=1

#4. Factorial: Write a code using a while loop to find the factorial of a given number.

# number=int(input("Enter your number:-"))
# factorial=1
# while number >0:
#     factorial *=number
#     number-=1
# print("factorial is :-",factorial)

#5. Password Check: Write a code using a while loop that keeps asking for a password until the correct password ("secret") is entered.

# correct_password='mechdm@600'
# password=''
# while password != correct_password:
#     password=input("Enter your password:--")

#     if password != correct_password:
#         print("Please enter valide password !...")


# print("password ! correct")



# s=10
# while s>=1:
#     print(s)
#     s-=1
    
    
## for loop

#1.		Print Squares: Write a code using a for loop to print the squares of numbers from 1 to 10.

# for i in range(1,11):
#     squre=i ** 2
#     print(f"Square of {i} is {squre}")

#2. find even odd number 1 to 50
# a=50
# for i in range(a):
#     if i %2 ==0 :
#         print(f"even number:-{i}")
#     else:
#         print(f"odd number:-{i}")


#3. Sum of Odd Numbers: Write a code using a for loop to calculate the sum of all odd numbers between 1 and 50.

# sum_of_odds = 0

# for i in range(1, 51):  
#     if i % 2 != 0:
#         sum_of_odds += i  

# print(f"Sum of odd numbers between 1 and 50  {sum_of_odds}")


#3. Multiplication Table: Write a code using a for loop to print the multiplication table of a given number up to 10.
# number=2
# for i in range(1,11):
#     print(f"{number} * {i} = {number * i} ")
    

#4. Reverse String: Write a code using a for loop to reverse a given string. For example, "hello" becomes "olleh".

# s='Sachin'
# t=[]
# for i in s:
#     for j in i:
#         t.append(j)
# t.reverse()
# temp_var=t
# print(temp_var)
       
#5. Generate List: Use a for loop to generate and print a list of the first 10 positive integers.
# s=[]

# for i in range(1,11):
#         s.append(i)
        
# print(s)

###infinite loop -break -continue -loop
#In nite loop is a loop that goes on , which never stops such type of loop is called in nite loop

# while True:

#     n=int(input("Enter a number:-"))
#     if n >0:
#         print('positive')
#     else:
#         print('Nigative')


##break

#  To stop such in nite loop we can use break statement
# • A break statement will stop the loop then and there
# • A break statement can be used in other loop situations as well apart from in nite loop
# • The below example shows the use of break statement

# while True:
#     n=int(input('Enter a Number:-'))
#     if n >0:
#         print('Positive')
#     elif n<0:
#         print('nigative')
#     else:
#         break

##Continue means it’ll not execute the rest of the loop it’ll simply go to beginning
#of the loop and continue its execution lets understand this with an example

# count=0
# while count <10:
#     n=int(input("enter a numnber:-"))
#     if n% 3==0:
#         continue
#     print(n)
#     count+=1



##Pass - In some cases when you don’t have to do anything use them just pass the it
# • Pass means nothing to do
# • In python when you write a block of code you must write something if there’s nothing to write , then simply write pass statement.

# count=0
# while True:
#     n=int(input("Enter a Number:-"))
#     if n %2 ==0:
#         pass
#     else:
#         print(n)  
#     count+=1
# 


# Not clear
# n=int(input("enter a numnber:-"))
# while n>0:
#     r= n%10
#     n=n//10
#     print(r)


# day=int(input("Enter a Day :-"))

# if day ==1:
#     print('Sunday')
# elif day ==2:
#     print("Monday")
# elif day ==3:
#     print("Tuesday")
# elif day ==4:
#     print("Wednesday")
# elif day ==5:
#     print("Thursday")
# elif day ==6:
#     print("Friday")
# elif day ==7:
#     print("Saturday")
# else:
#     print('Holiday')


##Nested loops
#loop instide loop is said as nested loop
#not clear
# for i in range(0,5):
#     for j in range(0,5):
#         print(i,j, end='')
#     print('')



# for loop: Iterates over a sequence (e.g., list, range).
# while loop: Repeats code as long as a condition is true.
# break: Exits the loop early.
# continue: Skips the current iteration and continues with the next.
# pass: Does nothing (used as a placeholder).

###break statement 
#break  statement used to exite the current (for or while) prematurely, even if the loop’s condition hasn’t been met yet.


# for i in range(1,10):
#     if i ==5:
#         break #break statement will stop the loop when i equal 5
#     print(i)


# for i in range(1,10):
#     if i == 6:
#         break
#     print(i)

# count=1
# while count<10:
#     print(count)
#     count+=1 #increment by 1


# count=0
# while count<10:
#     print(count)
#     count+=1
    
###coninue use ti skip curent iteration of a loop and move to next iteration

# for i in range(1,10):
#     if i==3:
#         continue #here compared to 3 and skiped 3 and runed complate code
#     print(i)

# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)


### Pass Statement
#The pass statement does nothing. It's used as a placeholder where a statement is syntactically required, but you don't want to execute any code.

# for i in range(1,10):
#     if i ==2:
#         pass #do nothing when i equal 2
#     print(i)


# for i in range(1,10):
#     if i == 2:
#         continue
#     print(i)

# Summary of Control Statements:
# if: Executes code if the condition is true.
# elif: Checks another condition if the previous one is false.
# else: Executes code if all preceding conditions are false.
# for loop: Iterates over a sequence (e.g., list, range).
# while loop: Repeats code as long as a condition is true.
# break: Exits the loop early.
# continue: Skips the current iteration and continues with the next.
# pass: Does nothing (used as a placeholder).

# numbers = [2, 3, 4, 5, 10, 11, 13, 17, 20]  # Example list


# for number in numbers:
#   # Check if the number is prime.
#   is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#         is_prime = False
#         break
#   # If the number is prime, print it.
#   if is_prime:
#     print(number)

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# # Example
# num1 = 48
# num2 = 18
# print("GCD:", gcd(num1, num2))


