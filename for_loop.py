# # # # # Python For Loops
# # # # ## # # # # A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# # # # # # # # # # This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# # # # # # # # # # With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# # # # # # # # # fruits=["Mango","banan","chery","water milo","chicku"]
# # # # # # # # # for i in fruits:
# # # # # # # # #     print(i)


# # # # # # # # Looping Through a String
# # # # # # # # Even strings are iterable objects, they contain a sequence of characters:

# # # # # # # for i in 'SACHIN':
# # # # # # #     print(i)
# fruits=["Mango","banan","chery","water milo","chicku"]
# # # # # # for i in fruits:
# # # # # #     print(i)
# # # # # #     if i =="chery":
# # # # # #         break

# # # # # The continue Statement
# # # # # With the continue statement we can stop the current iteration of the loop, and continue with the next:

# # # # frt=["Mango","banan","chery","water milo","chicku"]
# # # # for  i in frt:
# # # #     print(i)
# # # #     if i == "Mango":
# # # #         continue


# # # The range() Function
# # # To loop through a set of code a specified number of times, we can use the range() function,
# # # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# # for i in range(10):
# #     print(i)

# for i in range (2,10):
#     print(i)

for i in range (2,20000,5):
    print(i)

