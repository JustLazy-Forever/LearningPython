"""Sets- unorderd, elements unreplaceable, duplication of elements not allowed"""

mySet = {"banana", "apple", "cherry"}
print("My first set", mySet)

mySet.add("mango")
print("Added mango to mySet", mySet)

mySet.remove("apple")
print("removed 'apple'", mySet)

print("Length of mySet", len(mySet))

yourSet = set(("mango", "kiwi", "pineapple"))
print("yourSet", yourSet)

mySet.update(yourSet)
print("mySet", mySet)

mySet.symmetric_difference_update(yourSet)
print("mySet", mySet)

del yourSet

inputSet = {"keyboard", "mouse", "trackpad"}
print("Input set", inputSet)

outputSet = {"monitor", "printer", "speaker", "headphones"}
print("Ouptut set", outputSet)

inputSet.add("joystick")
print("added to inputSet", inputSet)

hardwareSet = inputSet | outputSet  # only for sets
print("Hardware Set", hardwareSet)

# hardwareSet = inputSet.union(outputSet) (for any iterable)
# print("Hardware Set", hardwareSet)

"""Frozensets = sets but unchangeable like tuple(un-removable, un-update-able, un-replaceable) """
