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
#

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


#while loop := while loop एखादी अट खरी असेपर्यंत कोड पुन्हा पुन्हा चालवतो.

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# उद्दिष्ट: अटींवर आधारित निर्णय घेऊन लूप चालवणे.
# उदाहरण: एखाद्या संख्येचा गुणाकार, सरासरी, किंवा विशिष्ट पॅटर्न तयार करणे.

# n=5
# fact=1
# while n>0:
#     fact*=n 
#     n-=1
# print(fact)


##series based q
# i=1
# while i <=10:
#     print(i,end= "")
#     i+=1

# i=1
# while i <=10:
#     print(i)
#     i+=1


#break statment  वापर: लूप मधून बाहेर पडण्यासाठी.
# i=1
# while i <=10:
#      if i == 5:
#          break
#      print(i)
#      i+=1

#continue statment वापर: काही अटींवर iteration skip करणे.
# i=0
# while i <= 5:
#     i+=1    
#     if i == 3:
#         continue
#     print(i)


#nested while loop वापर: लूपच्या आत दुसरा लूप.

# i = 1
# while i<=4:
#     j=1
#     while j<=2:
#         print(f"i={i},j={j}")
#         j+=1
#     i+=1


#pattern based questions
# i=1
# while i<=5:
#     print("**" * i)
#     i+=1

# k=10
# for i in range(k):
#     print("*"* i)

# pass statement वापर: काहीही न करायचं असेल तरी syntax पूर्ण ठेवण्यासाठी.

# i=0
# while 1 <=10:
#     pass

# loop else block  वापर: लूप पूर्ण झाल्यावर else चालतो (break न झाल्यास).

# i=1
# while i <=10:
#     print(i)
#     i+=1
# else:
#     print('End the loop')


# Merge two lists without duplicates
# a = [1,2,3]
# b = [3,4,5]
# print(list(set(a+b)))


# Count frequency of characters
# a='sachinnaiknaware'
# freq={}
# for ch in a:
#     freq[ch] = freq.get(ch, 0) +1
# print(freq)

#Reverse words in a string

# test = 'python test engineer'
# print("".join(test.split()[::-1]))

#find largest number in list
# largest= [2,3,4,34,2,45,243,5,24,4]
# print(max(largest))
# print(min(largest))

#  Lambda to square numbers
# sq = lambda x : x ** x   
# print(sq(10))  

def polindrome(s):
    return s == s[::-1]
print(polindrome('madam'))
        