# %% Simple Inheritance
# Inheritance allows a new class (the "Child") to automatically get all the features and behaviors of an existing class (the "Parent")
"""
The Key Benefits
Reusability: 
You don't have to rewrite the same code (like eat() or sleep()) for every single animal.

Organization: 
It keeps your code hierarchical and easy to read.

Efficiency: 
If you need to change how eat() works, you only change it in one place (the Parent), and all children are updated instantly."""


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is saying Bhaw Bhaw")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is saying Meow")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} is saying Squeek Squeek")

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

dog.eat()
cat.eat()
mouse.sleep()

mouse.speak()

dog.speak()


# %% Multiple Inheritance
# Multiple Inheritance is when a single child class inherits attributes and methods from more than one parent class.

class Prey:
    def flee(self):
        print("This is fleeing.")

class Predator:
    def hunt(self):
        print("This is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


rabbit.flee()

hawk.hunt()

fish.flee()
fish.hunt()

rabbit.hunt()  # This will give an error because rabbit has only instance of Prey not Predator 


# %% Multilevel Inheritance
# Multi-level Inheritance is like a family lineage (Grandparent -> Parent -> Child).

# Parent 1
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

# Parent 2
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

# Child

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Jojo")
hawk = Hawk("Henery Hawk")
fish = Fish("Nemo")


fish.hunt()
fish.eat()
print(Fish.mro())  # Method Resolution Order (MRO) ensures that Animal is only visited once.

print(80*"_")
rabbit.sleep()
rabbit.flee()
print(Rabbit.mro()) #Method Resolution Order (MRO) ensures that Animal is only visited once.

print(80*"_")
hawk.hunt()
hawk.eat()
print(Hawk.mro())



# %%
