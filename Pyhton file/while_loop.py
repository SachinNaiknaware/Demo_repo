# # # # # # # # Python Loops
# # # # # # # # Python has two primitive loop commands:

# # # # # # # # while loops
# # # # # # # # for loops

# # # # # # # The while Loop
# # # # # # # With the while loop we can execute a set of statements as long as a condition is true.

# # # # # # i=2
# # # # # # while i<6:
# # # # # #     print(i)
# # # # # #     i+=1

# # # # # The break Statement
# # # # # With the break statement we can stop the loop even if the while condition is true:

# # # # i=1
# # # # while i<10:
# # # #     print(i)
# # # #     if i ==5:
# # # #         break
# # # #     i+=1

# # # The continue Statement
# # # With the continue statement we can stop the current iteration, and continue with the next:

# # i=0
# # while i<6:
# #     i+=1
# #     if i==3:
# #         continue

# #     print(i)

# #he else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# i=1
# while i<10:
#     print(i)
#     i=i+1
# else:
#     print("i is no longer than 10")


# from scipy import stats
# import numpy as np

# data = np.random.normal(loc=50, scale=10, size=1000)
# print("Mean:", np.mean(data), "Skewness:", stats.skew(data))

# # Hypothesis Testing
# t_stat, p_val = stats.ttest_1samp(data, 50)
# print("T-Statistic:", t_stat, "P-Value:", p_val)


### while 

# while is loop will cause loop statement to the executed unil the loop condition is fasley
# i=0
# while i <10:
#     i = i+2
    
# print(i)



# if the condition is alway true  the loop will run forewer 

# while True:
#     print("Infinitr loop")


## while loop are fundamentatls for control flow ,and logic building
# a while loop runs as long conndition is true

# count=0
# while count  < 12:
#     print("Count is :-", count)
#     count +=1 

#series based question
