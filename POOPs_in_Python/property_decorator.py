# %% Property Decorator
"""
The @property decorator is the final piece of the OOP puzzle. 
It is used for Encapsulation—the art of protecting your data.

In most languages, you have to write "Getter" and "Setter" methods (like get_balance() and 
set_balance()). 
In Python, @property allows you to use a method as if it were a simple variable, 
while still keeping a "security guard" at the door to check the data.
"""

class Product:
    def __init__(self, price):
        self.price = price

    #1. GETTER: allows usto read the value
    @property
    def price(self):
        print("Checking price...")
        return f"${self._price:.2f}"
    
    #2. SETTTER : allows us to chnage the logic with value
    @price.setter
    def price(self, value):
        if value < 0:
            print("Error Price cannot be negative.")
        else: # Store data in the "hidden" variable _price
            self._price = value

p = Product(1000)

p.price = -500 

p.price = 800

print(p.price) 



# %% Email
"""
1. The "Secure Account" Example
In this example, we’ll use a User class. We want to protect the email.

Getter: Formats the email (e.g., lowercase).
Setter: Validates that it contains an @ symbol.
Deleter: Instead of removing the attribute, it "clears" it to a default value.
"""
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    @property
    def email(self):
        print(f"Accessing email for {self.username}")
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            print("Invalid email missing @ value.")
        else:
            self._email = value.lower()

    @email.deleter
    def email(self):
        print(f"Warning: Deletinng email for {self.username}. resetting the value to None.")
        self._email =  None

#getter
user1 = User("shaan_ahmed", "SHAAN536@gmail.com")
print(user1.email)

#setter
user1.email = "new_email@test.com"
print(user1.email)

#Deleter
del user1.email
print(user1.email)
# %%
