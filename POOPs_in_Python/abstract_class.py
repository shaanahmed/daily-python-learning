# %% Abstract Class 
"""An Abstract Class is like a "blueprint for a blueprint. 
You use it when you want to define a common set of rules for a group of objects, 
but you don't want anyone to create an instance of that base class directly."""

# ABC = Abstract Base Classes

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod 
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("You drive the car.")

    def stop(self):
        print("You stopped the car.")

class Bike(Vehicle):
    def start(self):
        print("You ride the bike.")

    def stop(self):
        print("You stopped the bike.")

class Boat(Vehicle):
    def start(self):
        print("You sailed the Boat")

    def stop(self):
        print("You anchored the boat.")

car = Car()
bike = Bike()
boat = Boat()

car.start()
car.stop()

bike.start()
bike.stop()


boat.start()
boat.stop()


# %% The "Shape Calculator"
"""
You are building a geometry tool. You need to handle different shapes (Circles, Squares, etc.), 
and every shape must be able to calculate its own area. 
If a developer creates a new shape but forgets to include an area method, 
the code should crash immediately to prevent errors later.

The RequirementsAbstract Base Class: Create a class named Shape.
Abstract Method: Define a method area() that has no implementation in the base class.
Subclasses: * Square: Takes a side in its constructor.
Circle: Takes a radius in its constructor.
Special Rules:If someone tries to write my_shape = Shape(), Python should raise an error.

The Circle class should use $3.14159$ for its calculation.
"""
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

# 2. Implementing the Square subclass

class Square(Shape):
    def __init__(self, name, side):
        self.name = name
        self.side = side
    
    def area(self):
        return self.side ** 2

# 3. Implement the Circle subclass

class Circle(Shape):
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

#Testing   
shapes = [Square("Square", 4), Circle("Circle", 3)]

for shape in shapes:
    print(f"The area of {shape.name} is : {shape.area():.2f}")
        


# %%
