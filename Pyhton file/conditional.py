#1. find a difference between 2 numbers
# no1=int(input("Enter your number:-"))
# no2=int(input("Enter your number:-"))

# if no1-no2 >=0:
#     print(no1-no2)
# else:
#     print(no2-no1)
    
#2. check if a number is odd or even
# x=10
# for i in range(x):
#     if i%2==0:
#         print('Number is even',i)
#     else:
#         print("Numebe is odd",i)     
        
        
#3. check the aligibilty for castin a vote
# std=int(input("Enter your age:-"))
# if std >=18:
#     print("Eligible for voting!......")
# else:
#     print("Student not eligible for vote!...")

#4. check if marks of a subject are within  range 0-100
# std=int(input("Enter std Mark:-"))
# if std>=0 and std<=100:
#     print("Student marks between 0 to 100")
# else:
#     print("Invalid Number") 

#5. check if person is female or male
# gender=input("Enter your status:-")
# if gender =='M' or gender == 'male':
#     print("True")
# else:
#     print('female')


#6. check if the person eligile to work
# age=int(input("Enter your ege:-"))
# if age>=18 and age<=100:
#     print("Eligible for work !!!!!!!")
# else:
#     print("Not eligible for work !!!!!!!")


#7. . check if a statement has passed or failed , by taking marks in 3 subjects .
# lets take marks of subjects ( maths , physics , chemistry ) marks are between 0 - 100
#and passing marks should be above 45
# math=int(input("Enter your Marks"))
# physics=int(input("Enter your Marks"))
# chemistry=int(input("Enter your Marks"))

# if math>=45 and physics>=45 and chemistry>=45:
#     print("Passed.....")
# else:
#     print("Fail")


#8. check the  person athorise for admin access
    #only admin can access the data by taking the user input  admin name sachin and balaji
    
# admin=str(input("Enter Your Name"))
# if admin=='sachin' or admin =='balaji':
#     print("Athorized")
# else:
#     print("Not Athorized")


#9 check if a given lowercase charector is vowels and consonant
#vowels= a,e,i,o,u
#remnaing are consonant
# ch =input("Enter your carector:- ")
# if ch=='a' or ch=='e'or ch=='i' or ch=='o' or ch=='u':
#     print("Vowels",ch )
# else:
#     print("consonant")
#if year % 100 ==0:
#     if year % 400 ==0:
#         print("leap year") 
#     else:
#         print("NOt leap year")
# elif    year % 4 ==0:
#     print("Leap Year")
# else:
#     print("Not Leap year")
#10. calculate discounted amount

# amount=int(input("Enter Your Amount:-"))
# if amount>=0 and amount<=1000:#10 percent
#     discount= amount * 10 / 100
# elif amount>=1000 and amount<=5000:#20 percent
#     discount= amount * 20 / 100
# elif amount>=5000 and amount<=10000:#30 perceent
#     discount= amount * 30 / 100
# else:
#     print("No Discount")
# discamount = amount - discount
# print("Pay after Discount",discamount)

#11. check the whether year is leap year or not

# year=int(input("Enter a year "))

# 


#12 take a day number and display day name
# day =input("Enter a day :-")
# if day == 1:
#     print("Sunday")
# elif day ==2:
#     print("Monady")
# elif day==3:
#     print("Tuesday")
# else:
#     print("Invalid day !!!!")



### Nestes if and elif

# age = int(input("Enter Your age :-"))
# citizenship = ['US','UK']

# if age >= 18:
#     if citizenship == 'US':
#         print("You are an adult US citizen.")
#     else:
#         print("You are an adult, but not a US citizen.")
# else:
#     print("You are not an adult.")


# age=int(input("Enter your age :-"))
# if age>=18:
#     if age <=30:
#         print("Young adult")
#     else:
#         print("adult")
# else:
#     print("not a adult")

# age=int(input("Enter your age :-"))

# if age>=0:
#     if age<13:
#         print("child")
#     elif age <= 19:
#         print("teenager")
#     else:
#         print("adult")
# else:
#     print("invalid age")
    
# temp=int(input("enter tempaature:-")) 
# if temp >=30:
#     if temp >= 40:
#         print("Extreme heat warning! stay indors.")
#     elif temp >=35:
#         print("Heat warning drink plenty of water")
#     else:
#         print("warm weather enjoy your day")
# elif temp >=20:
#     print("mild wheather")
    
# else:
#     print("cold weather")


#age wise educatuin leval 
# age=int(input("Enter your age:-"))

# if age>=18:
#     if age >= 45 :
#         print('Well educated')
#     elif age>=35:
#         print('Educated')
#     elif age >=26:
#         print('College complate')
#     else:
#         print("Under gradvation")
# elif age>=12:
#     print("child")
# else:
#     print('Not eligeble for study')
    
        


#1. Conditional Statements (if, elif, else)

# Syntax:
# python

# if condition:
#     # code to execute if condition is true
# elif another_condition:
#     # code to execute if another_condition is true
# else:
#     # code to execute if none of the above conditions are true


##### conditionals

#conditionals expressions involing keyword such as if,elif and else 

### the ternary operators 
n=5
"Greter than 2" if n > 2 else "smaller then or equal 2" 