# _init_ method is  a speical method to initalize the objects when it's created. 
# self is a refrence to the current instance of a class and it is the fundamental part of OOP in python.
#  In "object" and "classes " , self is used within the _init_  method to refer to the instance.

# Creating an object
class Dog:
    def __init__(self , name):
        self.name = name

dog1 = Dog("Buddy")
print(dog1.name)


# classes in pyhton are like blueprints for creating objects.

class Car:
    def __init__(self, make , model ):
        self.make = make
        self.model = model

car1 = Car ("Rolls Royas", "Ghost")
car2 = Car("Buggati", "Chiron")

print(car1.make , car1.model)
print(car2.make , car2.model)


##### Encapsulation #####

class Bankaccount:
    def __init__(self, account_number , balance ):
        self._account_number = account_number     # protected me
        self.__balance = balance                # Private member

    def get_balance(self):
        return self.__balance
    
account1 = Bankaccount("12345" , 1000)
print(account1._account_number)           # Accessing a protected member
print(account1.get_balance())             # Accessing a private member



####### Inheritance #######

# Inheritance allows you to create new classes that inherit properties and methods from existing classes .

class Animal :
    def __init__(self , name):
        self.name = name 

    def speak(self):
        pass


class Dog(Animal):
    def speak (self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    

dog = Dog("Buddy")
cat = Cat("Wishkers")

print(dog.name , dog.speak())
print(cat.name , cat.speak())