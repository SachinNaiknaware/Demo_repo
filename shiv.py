# it will take string as input from user it will print only owels

s = str(input("User Input: "))

for i in s:
    if i.upper() in ['A', 'E', 'I', 'O', 'U']:
        print(f"{i} is a vowel")
    else:
        print(f"{i} is not a vowel")


#write a program which will print only squre of odd number from 10 to 20

# for i in range(10, 21):  
#     if i % 2 != 0: 
#         print(i ** 2)  


#write a function which will print the reverese string


# def sachin(s):
#     print(s[::-1])
    
    
# print(sachin('SHIVKUMAR'))


# S ='SACHIN'
# rev_string = S[::-1]

# print(rev_string)
    