

#########   string
  
# str.casefold
# str.upper
# str.lower
# str.capitalize
# str.title
# str.swapcase

# case fold creata lowercase string that is sutaible for case insentive comparisons
# print("SHIVkumar".lower()) lower text
# print("SHIVkumar".upper())  upper text
# print("SHIVkumar".casefold())  all noramal text lower
# print("SHIVkumar".capitalize()) only first latter capitali
# print("SHIVkumar".title())       title
# print("SHIVkumar".swapcase())   first part lower last part upper


#### string is used to store text data

#single line comment
# p= "sss" #single line
# b= ''' this is multiple line comment    ''' #this is multiple line comment
# print(p)
# print(b)

## string opreation 


# ऑपरेशन	          उदाहरण	              अर्थ
# Concatenation 	"Hello" + "World"	    जोडणे
# Repetition	    "Hi" * 3 → "HiHiHi"	    पुनरावृत्ती
# Indexing	        "Sachin"[0] → 'S'	    पहिला अक्षर
# Slicing	        "Sachin"[1:4] → 'ach'	भाग कापणे
# Length	        len("Sachin") → 6	    लांबी

# str1="SACHIN  NAIKNAWARE"
# print("Hellow" + "Sachin") # Concatention
# print("HEllOW"*3) # Repeatition
# print(str1[0]) #Indexing
# print(str1[1:4]) #slicing
# print(len(str1)) # len           it takes space len also


#string methods


# Method	        वापर	          उदाहरण
# upper()	       मोठ्या अक्षरात	     "sachin".upper() → 'SACHIN'
# lower()	       लहान अक्षरात	        "HELLO".lower() → 'hello'
# strip()	       रिकामी जागा काढतो	" hi ".strip() → 'hi'
# replace()	       अक्षर बदलतो	       "abc".replace("a", "x") → 'xbc'
# split()	       शब्द वेगळे करतो	     "a,b,c".split(",") → ['a', 'b', 'c']
# find()	       अक्षर कुठे आहे ते शोधतो	"hello".find("e") → 1
# startswith()	   सुरुवात तपासतो	     "hello".startswith("he") → True
# endswith()	   शेवट तपासतो	       "hello".endswith("lo") → True

# print("Skdnbknv knkcddkjlncd".upper()) #uper 
# print("SkdFKDJBHDJDNMlncd".lower()) #lower
# print("    sachin JD,,      ".strip()) #strip  Is used to remove extra spaces from the string
# print("Hello ".replace('H','G')) #replace it replace the word or charectors
# print("Sachin naike".split()) # split  it will seprate the word  by coma
# print("Sachin naike".find('S')) #Find it will find the s is where is located
# print("Sachin naike".startswith("Hello")) # startwith it will check start with hellow or not output is False
# print("Sachin naike".startswith("Sachin")) # startwith it will check start with Sachin or not output is True

# print("Sachin naike".endswith("naike")) # endswith it will check ends with naike or not output will br True





