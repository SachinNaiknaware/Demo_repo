a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}






# Intersection: elements common to both sets
print("Intersection:", a.intersection(b))     # OR a & b   #Intersection means common elements that exist in both sets.

# Union: all unique elements from both sets
print("Union:", a.union(b))                   # OR a | b    All unique elements from both sets combined.

# Difference: elements in 'a' but not in 'b'
print("Difference (a - b):", a.difference(b)) # OR a - b

# Symmetric Difference: elements in a or b but not both
print("Symmetric Difference:", a.symmetric_difference(b))  # OR a ^ b

# Subset: checks if all elements of 'a' are in 'b'
print("Is 'a' subset of 'b'? :", a.issubset(b))            # OR a <= b

# Superset: checks if 'a' contains all elements of 'b'
print("Is 'a' superset of 'b'? :", a.issuperset(b))        # OR a >= b
