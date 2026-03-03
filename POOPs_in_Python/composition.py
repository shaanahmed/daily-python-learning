# %% Composition 
"""
While Aggregation is a loose "has-a" relationship, Composition is a strong "part-of" relationship.

In Composition, the child object cannot exist without the parent. If the parent object is destroyed, 
the child objects are automatically destroyed too. The parent "owns" the life cycle of the child.
"""

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}hp {self.wheels[0].size}inch "
    

car1 = Car("Ford", "Everest", horse_power = 296, wheel_size = 18)
car2 = Car("Land Rover", "Range Rover Evoque", horse_power = 600, wheel_size = 18)

print(car1.display_car())
print(car2.display_car())

# %% The Problem: The "Smart Home System"
"""
You are designing a system for a smart home. A House is composed of several Rooms, and each Room is composed of a Light.

The Requirements
Class Light:
__init__ takes brightness (integer).
Method glow() returns "Glowing at [brightness]% brightness".

Class Room:
__init__ takes room_name and light_level.
Inside __init__, create a Light object (Composition).

Class House:
__init__ takes address.
It should have a list called self.rooms.

Method add_room(name, lux): This should create a new Room object and append it to the list (Composition).
Method show_status(): Prints the address and loops through the rooms to show their names and how their lights are glowing.
"""

class Light:
    def __init__(self, brightness):
        self.brightness = brightness

    def glow(self):
        return f"Light Glowing at {self.brightness}% brightness"

class Room:
    def __init__(self, room_name, light_level):
        self.room_name = room_name
        self.my_light = Light(light_level)

class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []

    def add_room(self, name, lux):
        new_room = Room(name, lux)
        self.rooms.append(new_room)

    def show_status(self):
        print(f"House Status at: {self.address}")

        print("-" * 30)
        
        for r in self.rooms:
            print(f"In the {r.room_name}: {r.my_light.glow()}")

# Testing
my_home = House("Naginijan, Jorhat")
my_home.add_room("Kitchen", 90)
my_home.add_room("Bedroom", 20)
my_home.add_room("Bathroom", 30)

my_home.show_status()
# %%
