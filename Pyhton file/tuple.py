# what is tuple ?
#tuple is data structure which is also call as collection of items in which we can store anlything like list
#we write item of the tuple in () paranthes in which store by coma
#duplicates are allowed
#immutable

# t1=(5500,4035)
# type(t1)

#t2=(10,10.5,'sachin',True)
# print(type(t2))
# print(t2)

#len
# p=len(t2)
# print(p)

#copy

# t3=t2
# print(t3)

# tuple is immutable once created we can not change, used for data security
# tuple allow to store duplicate value in tuple 
# allow to diff type data
# t1= (1,2,3,3,4,5,6)
# print(t1)

#####tuple  comprehensions/ slicing
# square = tuple( x**2 for x in range(1,10))
# print(square) 

## slicing

# num=(10,20,30,40,50,60)
# # print(num[1:3]) #tuple slicing
# print(num[:-1])

# tuple fucntion

# Function	वापर	उदाहरण
# len()	लांबी मिळवतो	len(nums) → 5
# max()	सर्वात मोठा घटक	max(nums) → 50
# min()	सर्वात लहान घटक	min(nums) → 10
# sum()	सर्व घटकांची बेरीज	sum(nums) → 150

# tup=(1,2,3,4,5,67,8,9)
# print(len(tup))
# print(max(tup))
# print(min(tup))
# print(sum(tup))

# Tuple Methods (ट्युपलचे अंगभूत मेथड्स)
# Method	वापर	उदाहरण
# count()	दिलेला घटक किती वेळा आहे	(1,2,2,3).count(2) → 2
# index()	घटक कुठल्या index वर आहे	(10,20,30).index(20) → 1


# t = (1,2,3,4,5,6,7,8,9,10)
# print(t.count(5)) # check value how many time present in tuple
# print(t.index(10)) # chcekc index number in tuple
