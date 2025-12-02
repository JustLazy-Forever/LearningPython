"""
Created on Nov 24, 2025

@author: Hitech
"""

myDictionary = {
    "first_name": "Darshan",
    "second_name": "Shrestha",
    "roll_no": "KCE081BCT010",
}

# Displaying the key-value pairs of a dictionary using for loop
print("myDictionary: ")
for string in myDictionary.items():
    print(string)
# print("myDictionary: " , myDictionary)

# Adding dictionaries
also_anotherDictionary = {"Programme": "BCT"}
anotherDictionary = {"age": 18}
myDictionary.update(anotherDictionary)
print("\nmyDictionary: ", myDictionary)
for string in myDictionary.items():
    print(string)

    # Changing value of a key
myDictionary["age"] = 19
print("myDictionary-age: ", myDictionary["age"])
