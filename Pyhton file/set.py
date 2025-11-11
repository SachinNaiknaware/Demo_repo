# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8



# Intersection: elements common to both sets
# print("Intersection:", a.intersection(b))     # OR a & b   #Intersection means common elements that exist in both sets.

# # Union: all unique elements from both sets
# print("Union:", a.union(b))                   # OR a | b    All unique elements from both sets combined.

# # Difference: elements in 'a' but not in 'b'
# print("Difference (a - b):", a.difference(b)) # OR a - b

# # Symmetric Difference: elements in a or b but not both
# print("Symmetric Difference:", a.symmetric_difference(b))  # OR a ^ b

# # Subset: checks if all elements of 'a' are in 'b'
# print("Is 'a' subset of 'b'? :", a.issubset(b))            # OR a <= b

# # Superset: checks if 'a' contains all elements of 'b'
# print("Is 'a' superset of 'b'? :", a.issuperset(b))        # OR a >= b





###### set is used store uniqe values 

#s={1,2,2,3,4,55,55}
#print(s) # dosent allow duplicate value


# Sets Operations (सेटवरील क्रिया)
# ऑपरेशन	         उदाहरण	अर्थ
# Membership	     2 in s   True	घटक अस्तित्व तपासणे
# Add	            s.add(5)	 नवीन घटक घालणे
# Remove	        s.remove(2)	 घटक काढणे
# Pop	            s.pop()	     random घटक काढतो
# Clear	            s.clear()	 सेट रिकामा करतो

s={1,2,3,4,5,5,5,6,7,8}
# print( 2 in s) #check 2 present in set or mot
# s.add(11) #new value added
# print(s)
# s.remove(1) #remove element
# print(s)

# print(s.pop()) # it remove random value
# print(s)

# i=1
# if i %2 ==0 :
#     print("Even")
# else:
#     print("odd")
# s.clear()
# print(s) #Clear the set


#union 
# a={1,2,3,3}
# b={4,5,6,3}
# print(a | b) # give us unique vallue in both set

# print(a & b) # it will give from two set comman value

# print(a - b)
# print(b - a)


# Symmetric Difference (सममित फरक)
# दोन सेट्स मधील unique पण common नसलेले values.
# print(a ^ b)
