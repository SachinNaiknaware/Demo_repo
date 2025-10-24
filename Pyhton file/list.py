# #List are used multiple items in single variable
# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# #Since lists are indexed, lists can have items with the same value:

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

#List items can be of any data type:
# list1 = ["apple", "banana", "cherry"]
# # list2 = [1, 5, 7, 9, 3]
# # list3 = [True, False, False]
# # print(list1)
# # # print(list2)
# # # print(list3)
# # # print(type(list1))

# # # The list() Constructor
# # thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# # print(thislist)# possible to use the list() constructor when creating a new list.

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#Access Items
#List items are indexed and you can access them by referring to the index number:
# thislist = ["apple", "banana", "cherry"]
# print(thislist[0])


#list1=[]

# print(type[list1])
#l2=[10,'ankit',True,10.6,'ankush',10]

#slice methods

# print(l2[2]) #True
# print(l2[1:3]) #['ankit', True]

#count
# print(l2.count(10))

#index
#print(l2.index(10.6)) #3 check index postion 

#insert 
# l2.insert(2,'Sachin')
# print(l2)

#pop # delete element 

# l2.pop(4)
# print(l2) #pop delete a  vallue by using index ,defoult delete last element

#extend
# l4=['sachin',10]
# l2.extend(l4) #add new list another list
# print(l2) 

#copy
# l3=l2.copy()
# print(l3)

# fruits = ['apple', 'banana']
# fruits.append('mango')
# print(fruits)

#sort
#l3=[12,23,43,45,56,78976,2,31]
# l3.sort()#defult ascending
# l3.sort(reverse=True) #descending manual
# print(l3)

#reverse 
# l3.reverse()
# print(l3)#it will reverse not sort


# nested list
# l3=[12,23,43,45,56,78976,2,31,['Sachin',['balaji']]]
# print(l3)

#list compherantion 

# l4=['Sachin','balaji','avi','ajit']
# a=[word for word in l4 if word.startswith("a")]
# print(a)

#list unpacking

# l5=['ankush','amkit']
# l6,l7=l5 #unpack means broken 
# print(l6)
# print(l7)


# Starting list
fruits = ['apple', 'banana', 'cherry']

# 1. append()
fruits.append('orange')  # ['apple', 'banana', 'cherry', 'orange']

# 2. clear()
fruits.clear()  # []

# Reset list
fruits = ['apple', 'banana', 'cherry']

# 3. copy()
copy_fruits = fruits.copy()  # ['apple', 'banana', 'cherry']

# 4. count()
fruits.count('banana')  # 1

# 5. extend()
fruits.extend(['date', 'fig'])  # ['apple', 'banana', 'cherry', 'date', 'fig']

# 6. index()
fruits.index('cherry')  # 2

# 7. insert()
fruits.insert(1, 'blueberry')  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'fig']

# 8. pop()
fruits.pop()  # removes 'fig'

# 9. remove()
fruits.remove('banana')  # removes first occurrence of 'banana'

# 10. reverse()
fruits.reverse()  # reverses the list

# 11. sort()
fruits.sort()  # sorts alphabetically
