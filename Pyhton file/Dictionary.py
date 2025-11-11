### Dictionary
## A Dictionary is an examaple of key value store also known as Mapping in Pyhton

# 
# d={}
# print(type(d))

# d = {'key': 'value'}
# print(d['key'])



# iterating over the dictionary
# a={'a':1,'b':2}
# for i in a:
#     print(i, a[i])


### dictionary is collection of key vallue pairs
#dictionary is mutable  kew is uniqe
# my_dict={1:"Sachin",2:"Balaji"}
# print(my_dict)
# print(my_dict[1])
#Operations (डिक्शनरीवरील क्रिया)
# ऑपरेशन	उदाहरण	अर्थ
# Access	    my_dict["age"]	                value      मिळवणे
# Add	      my_dict["country"] = "India"	    नवीन key-value घालणे
# Update	my_dict["age"] = 26               	value बदलणे
# Delete	del my_dict["city"]	                key-value काढणे
# Membership	"name" in my_dict → True	    key अस्तित्व तपासणे

# my_dict ={"name":"sachin","age":24,"location":"Dharashiv","Education":"BCA","Job":"Engineer"}


# print(my_dict["name"]) #access  

# my_dict["Contry"] ="India" 
# print(my_dict)  # adding new kew value

# my_dict["name"] = "Balaji"
# print(my_dict) # updating value in existing dict key

# del my_dict["Contry"] #delating key and value by deleting key
# print(my_dict)
# my_dic={1:2}
# my= 1 in my_dic
# print(my)



## comprehensions means creat dictionary in single line

# squres = {x: x**2 for x in range(1,10)}
# print(squres)

# Dictionary Methods (डिक्शनरीचे अंगभूत फंक्शन्स)
# Method	      वापर	                  उदाहरण
# keys()	      सर्व keys मिळवतो	        my_dict.keys()
# values()	      सर्व values मिळवतो	    my_dict.values()
# items()	      key-value pairs मिळवतो  my_dict.items()
# get()	value     मिळवतो (error न देता)	    my_dict.get("age")
# update()	      दुसरी dictionary merge करतो	my_dict.update({"age": 30})
# pop()	          दिलेला key काढतो delete  	my_dict.pop("name")
# clear()	      dictionary रिकामी करतो    my_dict.clear()

my_dict ={"name":"sachin","age":24,"location":"Dharashiv","Education":"BCA","Job":"Engineer"}
#my_dict.keys()
#my_dict.values()
#my_dict.items()
#my_dict.get("age")
# my_dict.update({"State":"Maharashtra"})
#my_dict.pop("name")
# clr=my_dict.clear()
# print(clr)
