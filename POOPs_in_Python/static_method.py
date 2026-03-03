# %% STATIC METHOD
"""A Static Method is a method that belongs to a class rather than a specific object (instance).

Usually, methods need self to access data inside an object. But sometimes, you want a 
function to live inside a class simply because it is logically related to that class, 
even if it doesn't need to change or read any object data.

----->>>> You should use a Static Method when:

Utility Functions: You have a function that performs a task related to the class 
(like a conversion or calculation) but doesn't need to know about the object's attributes.

Namespace Organization: You want to keep the function inside the class so it's easy to find, 
rather than having it float around your main code.

Memory Efficiency: Since it doesn't receive the self argument, it is slightly more lightweight.
"""
class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Clerk', 'Developer', 'System Designer']
        return position in valid_positions
    
print(Employee.is_valid_position("Star"))

emp1 = Employee("Alex","Developer")
emp2 = Employee("Krik","Manager")
emp3 = Employee("Trove","Clerk")

print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())


# %% The Problem: The "Temperature Converter"
# Let's combine a Nested Class with a Static Method.
"""The Requirements
Outer Class WeatherStation:
Constructor takes station_name.

Nested Class Converter:
This class should only contain Static Methods.
celsius_to_fahrenheit(c): Takes Celsius and returns Fahrenheit using the formula: 
F = (C * 9/5) + 32.
fahrenheit_to_celsius(f): Takes Fahrenheit and returns Celsius using: 
C = (F - 32) * 5/9.
"""

class WeatherStation:
    def __init__(self, station_name):
        self.station_name = station_name

    class Converter:
        @staticmethod
        def celsius_to_fahrenheit(c):
            return (c * 9/5) + 32
        
        @staticmethod
        def fahrenheit_to_celsius(f):
            return (f - 32) * 5/9

temp_f = WeatherStation.Converter.celsius_to_fahrenheit(25)
print(f"25°C in Fahrenheit is: {temp_f}°F")

my_station = WeatherStation("Jorhat Station")
temp_c = my_station.Converter.fahrenheit_to_celsius(77)
print(f"77°F in Celsius is: {temp_c}°C")


# %%
