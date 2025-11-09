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



### it will print group of elment one by one
# for u in range(1,10):
#     print(u)

#range function 
#it crat a serij
#range(start, stop ,step)
# for i in range(1,10,2):
#     print(i)


#nested for loop  inside loop another loop  वापर: pattern printing, matrix traversal, आणि complex logic साठी.


# for i in range(1,2):
#     for j in range(1,3):
#         print(f"i={i},j={j}")


# Pattern-Based Questions (पॅटर्न आधारित प्रश्न)

#star pattern
# for i in range(1,10):
#     print("*" * i)

#reverse pattern
# for i in range(10,0,-1):
#     print("*" * i)


#break statement # used for out the loop वापर: लूप मधून बाहेर पडण्यासाठी.

# for i in range(1,20):
#     if i == 10:
#         break
#     print(i)

#continue statement  वापर: एखादी iteration skip करण्यासाठी.

# for i in range(1,10):
#     if i == 1:
#         continue
#     print(i)