###compehensions

 
# Key Benefits of Comprehensions
# Conciseness: Reduce multiple lines of code into one line.
# Readability: Clear and intuitive when used properly.
# Performance: Faster than equivalent loops for small to medium-sized data sets.
# Flexibility: Support mapping, filtering, and complex nested structures.


# expression: The value that gets added to the list.
# item: The current element from the iterable.
# iterable: The iterable you're looping over (e.g., list, tuple).
# condition (optional): A filter to include only items that satisfy the condition.



#1. List Comprehensions



#table of two
# s=[i *2 for i in range(1,11)]
# print(s)



# ev=[x for x in range(10) if x % 2== 0]
# print(ev)



# words=['sachin','ram','Laxaman']
# upper_l=[i.upper() for i in words]
# print(upper_l)




# nasted_list=[[1,2],[3,4],[5,6]]# nasted_list is a list containing other lists (a nested list):

# s=[j for i in nasted_list for j in i]
# print(s)



# list1=[1,2,3]
# list2=['A','B','C']

# L=[(x,y)for x in list1 for y in list2]
# print(L)


#2. tuple comperhensions
#Similar to list comprehension, but it creates a generator object instead of a list. Useful for large data sets as it computes items lazily (on demand).

#not clear generator object <genexpr> at 0x766e63a42570>  why this error is coming
# t1 = (1, 2, 3, 4, 5)
# f = (i * 2 for i in t1)

# print(f)



#3. Dictionary comprehensions

#not clear 
# squares_dict = {x: x**2 for x in range(5)}
# filtered_dict = {x: x**2 for x in range(10) if x % 2 == 0}

# print(squares_dict)
# print(filtered_dict)

# origin={'a':1,'b':2,'c':3,'d':4}
# fil={ key:value for key,value in origin.items() if value % 2 ==0 }
# print(fil)



# original = {'a': 1, 'b': 2, 'c': 3,'d':4,'e':5}
# f={key:value for key,value in original.items()}
# print(f)



# key=['sachin','balaji','laxamn']
# value=[1,2,3,4]
# a={key:value for key,vlaue in zip(key,value)}
# print(a)



# numbers = range(1, 6)
# result = {x: ('even' if x % 2 == 0 else 'odd') for x in numbers}
# print(result)



# Set Comprehensions:-
# unique_squares = {x**2 for x in range(1,6)}
# print(unique_squares)

# list1=[0,1,2,3,4,5,6,7,8,9]

# f=[i for i in list1 if i !=2]
# print(f)



#code for even or odd

# for i in range(1,10):
#     if i % 2 == 0:
#         print(f'{i}is even')
#     else:
#         print(f'{i}odd')
        
        
