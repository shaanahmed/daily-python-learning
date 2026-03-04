# %% Class Method
"""
A Class Method is a method that belongs to the class itself rather than an individual object.

While a regular method uses self to talk to an object (like a specific car), 
a Class Method uses cls to talk to the blueprint (the Car class).

The Key Characteristics
The Decorator: It must be preceded by @classmethod.
The First Argument: It always takes cls (short for Class) as its first argument instead of self.
The Access: It can change things that affect the entire class, not just one instance.
"""

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"total number of students {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The average gpa of students is : {cls.total_gpa / cls.count}"

student1 = Student("Shaan", 8.5) 
student2 = Student("Anie", 9.0)
student3 = Student("Alex", 7.7) 

print(student1.get_info())

print(Student.get_count())

print(Student.get_average_gpa())


# %% The Problem: The "Employee Onboarding" System
"""
Imagine you are building a system for a company. Usually, you create an employee with a 
name and a salary. However, sometimes the HR department sends you the data as a single 
string (from a spreadsheet) or as a dictionary (from a website form).

The Requirements
Class Employee:
Class Variable: company_name = "TechCorp".
Constructor: Takes name and salary.
Class Method 1: from_string(cls, employee_str):

This should accept a string like "Rahul-50000".
It should split the string and return a new Employee object.

Class Method 2: from_dict(cls, data_dict):
This should accept a dictionary like {"n": "Sita", "s": 60000}.
It should extract the values and return a new Employee object.
"""
class Employee:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, employee_str):
        name, salary = employee_str.split("-")
        return cls(name, int(salary))

    @classmethod
    def from_dict(cls, data_dict):
        name = data_dict.get("n")
        salary = data_dict.get("s")
        return cls(name, salary)

emp1 = Employee("Shaan", 40000)

# from string
emp2 = Employee.from_string("Anie-55000")

# From Dictionary
emp3 = Employee.from_dict({"n": "Alex", "s": 70000})

print(f"{emp1.name} works at {Employee.company_name} with a salary of {emp1.salary}")
print(f"{emp2.name} works at {Employee.company_name} with a salary of {emp2.salary}")
print(f"{emp3.name} works at {Employee.company_name} with a salary of {emp3.salary}")


# %%
