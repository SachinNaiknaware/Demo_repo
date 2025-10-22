# There are a number of collection types in Python. While types such as int and str hold a single value, collection types hold multiple values.

####### 1. Lists
# The list type is probably the most commonly used collection type in Python. Despite its name, a list is more like anarray in other languages, 
# mostly JavaScript. In Python, a list is merely an ordered collection of valid Python values. A
# list can be created by enclosing values, separated by commas, in square brackets:


# how to crate a list

int_list=[1,2,3,4,5]
string_list=['ab','xyz']


empty_list=[]
#print(empty_list)  # []


#The elements of list are not ristricted to a single datatype, which makes sense given that Python is Dynamic type language.

list1=[1,'sachin',1.2,True,None]
#print(list1)


#the list can contain another list as its elemnet.
nested_list=[[1,2,4,3],[1,34,54,2]]
# print(nested_list[1])

#the element of list can be accessed vie an index or numric represention of their position 
# list are in zero_index postion 
names=['sachin','balaji','jivan','ram','sham']
# print(names[4]) #sham


#indices can also be nigative which means counting form the end 
# print(names[-3])  #jivan


#lise are mutable so you can change values in a list
names[0]='krishna'
#print(names) #it remove old value and add new value of that index position 


#append object to the end of list
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
#names.append('Sia')
# print(names)

#add new element to the list of spescfic index
#names.insert(1,'Srisha')
#print(names)

#remove the first accurence of a value 
# names.remove('Bob')
# print(names)

#get the index of the first item 
#print(names)
# names.index('Eric')
# print(names)

#count lenth of list
# print(len(names))


# count occurrence of any item in list
a=[2,4,5,8,1,2,3,4,7,2]
# print(a.count(2))

#Reverse the list
# a.reverse()
# print(a)
# print(a.reverse())

# remove and return item at index (defaults remove the lst item)
# print(a)
# a.pop()
# print(a)




### tuple 
# A tuple is similar to a list except that it is ﬁxed-length and immutable. So the values in the tuple cannot be changed
# nor the values be added to or removed from the tuple. Tuples are commonly used for small collections of values
# that will not need to change, such as an IP address and port. Tuples are represented with parentheses instead of
# square brackets:
# ip_address = ('10.20.30.40', 8080)



### Dictionaries
# a dictionary in python is a collection of key vallue pais. the dictionary is supported curly braces,
# each pair is sepreated by comma and the key and  value are separated by colon.
dict1={'id':1,'name':'sachin'}
# print(dict1)




###  set 
# A set is a collection of elements with no repeats and without insertion order but sorted order. They are used insituations where it is 
# only important that some things are grouped together, and not what order they were  included. For large groups of data, 
# it is much faster to check whether or not an element is in a set than it is to do the same for a list.

first_name={'sachin','ram','sham'}

# you can bulid set using an exsting list
# my_list=[13,4,45,45,24,53]
# my_set=set(my_list)
# print(type(my_set))
