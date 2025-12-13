import sys

class Person:
    def __init__ (self, name = "John", age = 30, sex = 'M'):
        self.name = name
        self.age = age
        self.sex = sex
    
    def inputInfo (self):
        self.name = input("Enter name : ")
        self.age = int(input("Enter age : "))
        self.sex = input("Enter sex : ")

    def displayInfo(self):
        print("\n\nName : ", self.name)
        print("Age : ", self.age)
        print("Sex : ", self.sex)


person1 = Person()

person1.inputInfo()
person1.displayInfo()
