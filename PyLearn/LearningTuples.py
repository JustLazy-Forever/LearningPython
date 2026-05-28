aTuple = tuple(("Python", "C", "C++", "Java"))
print("Creating a tuple ", aTuple)

aList = list(aTuple)
print("above tuple into a list", aList)

aList.remove("C++")
print("removing from the list", aList)

aTuple = tuple(aList)
print("Above list back into tuple", aTuple)

print("Length of the tuple", len(aTuple))

print("Number of Python in the tuple", aTuple.count("Python"))

print("Working with the list", aList)

aList.insert(2, "Python")

print("Inserted", aList)

aTuple = tuple(aList)
print("modified tuple", aTuple)

print("First occurence of 'Python' at index = ", aTuple.index("Python"))
