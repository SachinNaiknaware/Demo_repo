##1 Converting an integer into Decimals
# import decimal

# integer = 10
# print(decimal.Decimal(integer))              # Output: 10
# print(type(decimal.Decimal(integer)))        # Output: <class 'decimal.Decimal'>


##2 Convertin an string of ingegers into Decimals

# import decimal
# string='12345'
# print(decimal.Decimal(string))
# print(type(decimal.Decimal(string)))

##3. reverting a string using an extended slicing technnique

# string= "Python Programming"
# print(string[::-1])

# ##4 Counting vowels in given list
# vowel=['a','e','i','o','u']
# word='wilwkoiurznbvcxzqwqertyuiolmnbvcxzasyubvjml'
# count=0
# for charecter in word:
#     if charecter in vowel:
#         count+=1
# print(count) 

# ii=input('enter :: --')
# vowel=['a','e','i','o','u']
# c=0
# for i in ii:
#     if i in vowel:
#         c+=1
# print(c)


##5.  Counting CONSONANTS
# vowel=['a','e','i','o','u']
# count=0
# wk=input("Enter input--")
# for i in wk:
#     if i not in vowel:
#         count+=1
#     else:
#         pass
# print(count)


# vowel=['a','e','i','o','u']
# input_1='lsdofiuhb'
# c=0
# for i in input_1:
#     if i in vowel:
#         c+=1
#     else:
#         pass
# print(c)

##6 Counting the number of occuranced of a character in a string

# word=['p']
# name=input("Enter:-")
# count=0
# for i in name.lower():
#     if i in word:
#         count += 1
#     else:
#         pass
# print(count)

##7. Writing FIBONACCI Series
# fib=[0,1]
# n=10
# for i in range(n):
#     fib.append(fib[-1] + fib[-2])
    
# print(fib)
# print(','.join(str(e) for e in fib))

# fib=[0,1]
# n=20
# for i in range(n):
#     fib.append(fib[-1] + fib[-2])
# print(fib)

# fib=[0,1]
# fib_num=15
# for i in range(fib_num):
#     fib.append(fib[-1]+ fib[-2])
# print(fib)


##8 Finding the Maxomum Numnber in a lis
# num1=[32,43,34,3,32,45,5,2,23,32,453]
# ma=num1[0]
# for i in num1:
#     if i > ma:
#         ma=i
# print(ma)        
# import statistics
# nn=statistics.
# print(nn)


##9 Finding the minimam Number in a List

# number_list=[22,2,4,32,67,144,15,15]
# min=number_list[0]
# for i in number_list:
#     if i > min:
#         min=i
# print(min)

#print(max(22,2,4,32,67,144,15,15))


##10 Finding the middle Elemrnt in a list
# numlist=[22,2,4,32,67,144,15,15]
# middle_list=int((len(numlist)/2))
# print(numlist[middle_list])

# num=[12,23,3,34,5,25,6]
# mid=int((len(num)/2))
# print(num[mid])

##11 Converting a list into a string

# ls=['P','y','t','h','o','n',20]
# string="".join(map(str,ls))
# print(string)

# name=['S','A','C','H','I','N',10]
# new_name="".join(map(str, name))
# print(new_name)


##12 Adding Two vallue List Element Together
# l1=[12,4,4,2]
# l2=[34,4,34,23]
# new_list=[]
# for i in range(0, len(l1)):
#     new_list.append(l1[i] + l2[i])
# print(new_list)


# l3=[122,3,4,4,5]
# l4=[24,5,5,5,5    ,9]
# emplist=[]
# for i in range(0,len(l3)):
#     emplist.append(l3[i]+ l4[i])
# print(emplist)



##