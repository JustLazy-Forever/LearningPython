myList = list( ("Apple", 'Banana','Orange', 'Mango') )

print("The length of myList is ", len(myList))
print(myList)

if "Apple" in myList:
        print("'Apple' is in myList")
        
if "Kiwi" not in myList:
        print("'Kiwi' is not in myList")
        
myList.pop(0)
print("Popped", myList)

myList.insert(1, 'Mango')
print("Inserted", myList)

#del myList; print(myList)

myList.append('Apple')
print("Appended", myList)

yourList = list( ('Lamborgini', 'Pagani', 'Ferrari') )

myList.extend(yourList)
print("Extended", myList)

myList.remove('Lamborgini')
print("Removed Lamborgini", myList)

del myList[5:]
print("Deleted yourList", myList)

myList.remove('Mango')
print("Removed the first occurrence of 'Mango'",myList)

# myList.clear()
# print("Cleared List", myList)

# myList.sort(reverse = True)
# print(myList)

myList.reverse()
print("myList reversed ", myList )

x = 0
for x in myList:
        print(x)
        
someList = [x for x in myList if x != "Apple"]
print(someList)

someList = myList.copy()
print("someList(copied from myList)",someList)

anotherList = list (myList)
print("anotherList('list' from myList)",anotherList)

tooManyLists = myList[:]
print("tooManyLists(sliced from myList)", tooManyLists)















































































































































































































































































































