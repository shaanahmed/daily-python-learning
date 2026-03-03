# %% super()

class Shape:
    def __init__(self, color, is_filled):
        self.color = color 
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and is {"filled" if self.is_filled else "not filled"}.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"This is a circle with area: {3.14159 * self.radius ** 2:.2f}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

    def describe(self):
        print(f"This is a square with area: {self.side ** 2:.2f}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"This is a circle with area: {self.width * self.height /2 :.2f}cm^2")
        super().describe()

circle = Circle("Blue", True, radius = 5)
square = Square("Silver", False, side = 8)
triangle = Triangle("Red", True, width = 4, height = 6)

#Testing
circle.describe()

print(50*"_")

square.describe()

print(50*"_")

triangle.describe()


# %% Using super() with Regular Methods
# You can also use it to "extend" a behavior. Imagine a Manager who does everything an Employee does, plus a little extra:

class Employee:
    def work(self):
        return "I am performing my tasks"

class Manager(Employee):
    def work(self):
        original_work = super().work()
        return f"{original_work} and I am also attending meetings."
    
manager = Manager()

print(manager.work())

    
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
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
    
    def area(self):
        return self.side ** 2
    
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
shapes = [Square("My Square", 4), Circle("My Circle", 5)]

for s in shapes:
    print(f"The area of {s.name} is {s.area():.2f} cm^2")
    

# %%
