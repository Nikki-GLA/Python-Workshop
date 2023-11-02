# A set of an unordered collection of unique elements in python.
# defined by enclosing elements in curly brackets or in set()


# Operating a set
my_set = {1,2,3,4}

# Adding an element
my_set.add(5)
print(my_set)

# Adding more than one element
myset = {8,9,10}
Resultant_set = my_set.union(myset)
print(Resultant_set)

# Removing an element 
my_set.remove(3)  # Raise an error if the element does not exist
my_set.discard(7) # Remove the element, even if it doesn't exist
print(my_set)



# Methods and Opeations 
# union 



# intersection
set1 = {"a","b","c","d"}
set2 = {"c","d","e"}
 
c = set1.intersection(set2)
print(c)

# difference
set1 = {"a","b","c","d"}
set2 = {"c","d","e"}

d = set1.difference(set2)
print(d)

# symmetric difference
set1 = {"a","b","c","d"}
set2 = {"c","d","e"}
 
e = set1.symmetric_difference(set2)
print(e)



# ---------------------------------------- DICE GAME ----------------------------------

