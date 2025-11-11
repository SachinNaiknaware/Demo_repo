
# squred=lambda  num : num  ** 2
# # print (squred(5))



# s= lambda  string : string [::-1]
# print(s('apple'))


# owels = lambda string : [x for x in string if x.lower()]
# print(owels('apple'))

# write a lambda which creates tuple takes list as argumen/parmaetr and creat a dictionary where list element are used as keys and the datatype value
# tu = lambda list :
    
# tu = lambda lst: {x: type(x).__name__ for x in lst}
# data = [1, "hello", 3.14, True, None]
# result = tu(data)
# print(result)


#create a lambda function which take tuple numric string and retuns list of number from string 

#basic lambda function 
# greet_me = lambda : "Hello"
# print(greet_me())


# lambda can take argument 

# strip_and_uper_case = lambda a : a.strip().upper()
# print(strip_and_uper_case("Hellolgkfhjkj"))


# lambda are use for short function that are convenient to define at the point where they are called
# sorted_list = sorted(['foo', 'bar', 'baz'], key=lambda a: a.strip().upper())
# print(sorted_list)

# def greet(msg):
#     return msg

# print(greet("Hello Modi"))
# greet_lm = lambda x: greet(x)
# print(greet_lm("Hello Modi"))


## lambda  in python simple way to define a small ,anonymous function in single line without using def

# square = lambda x:  x ** x 
# print(square(4))

## map सर्व घटकांवर फंक्शन लावतो
#in python map used to apply a funciton to each item in an interable (like= list and tuple) and return map object iterrator

#Syntax
# map(function, iterable)
# function → the function you want to apply
# iterable → list, tuple, or any sequence of values


#using normal function
# def square(x):
#     return x * x
# number=[1,2,3,4,5]
# result=map(square,number)
# print(list(result))

# num=[2,4,6]
# square= list(map(lambda x : x ** 2, num ))
# print(square)

# num=[1,2,34,5]
# square=list(map(lambda x: x ** 2, num))
# print(square)

# Filter (फक्त अट पूर्ण करणारे घटक ठेवतो)
# num=[1,2,3,4,5,56,4,4,4,3,5,6]
# even = list(filter(lambda x: x % 2 ==0,num))
# print(even)

