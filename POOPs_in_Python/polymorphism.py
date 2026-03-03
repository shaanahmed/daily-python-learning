#%% Polymorphism
"""
Polymorphism is a Greek word meaning "many forms." In programming, 
it’s the ability of different objects to respond to the same method call in their own specific way.
"""
# In python polymorphism is usually achieved through Inheritance (sharing a base class) or Duck Typing (sharing method names without needing a common parent).

# INHERITANCE

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name 

    @abstractmethod
    def area(self):
        pass

    

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
    
    def area(self):
        return self.side ** 2

class Pizza(Circle):    # This is also Polymorphism because it has many forms a pizza, a circle then a shape.
    def __init__(self, name, toppings, radius):
        super().__init__(name, radius)
        self.toppings = toppings

shapes = [Circle("Circle", 4), Square("Square", 5), Pizza("Cheese Pizza", "Mushroom", 7)]

for items in shapes:
    if not isinstance(items, Pizza):
        print(f"Area of the {items.name} is {items.area():.2f}cm^2")
    else:
       print(f"Giant Offer the {items.name} with {items.toppings} is {items.area():.2f}cm^2") 



# %% POLYMORPHISM using DUCK TYPING

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print('WOOF!')

class Cat(Animal):
    def speak(self):
        print('Meow')

class Car:
    def speak(self):
        print('Honk Honk!')

    alive = False

animal = [Dog(), Cat(), Car()]

for i in animal:
    i.speak()
    print(i.alive)
    

# %% Polymorphism using Method Overriding

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Generic Sound')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self): # Overriding the parent method
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self): # Overriding the parent method
        print("Meow")

dog = Dog("Scooby")
cat = Cat("Garfield")


print(dog.name)
dog.speak()

print(cat.name)
cat.speak()

# %%
