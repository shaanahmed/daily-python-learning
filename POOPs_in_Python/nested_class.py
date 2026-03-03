# %% Nested Class
"""
A Nested Class (also called an Inner Class) is a class defined entirely inside another class.

While Composition usually involves two separate classes where one "owns" the other, 
a Nested Class is used when a class is so specialized that it shouldn't really exist on its own outside the "Outer" class.

-----> Why use Nested Classes?

Logical Grouping: If a class is only used by one other class, keep them together. 
It makes the code easier to read and maintain.

Encapsulation: It hides the internal details. A user of your code only sees the Computer 
class and doesn't need to worry about the Processor class directly.

Namespace Control: It prevents "polluting" your main code with tiny classes that aren't 
useful elsewhere.
"""

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name =name
            self.position = position

        def get_details(self):
            return f"{self.name} is a {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name 
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)   #here is the ested class usage
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company = Company("Palantir")

print(company.company_name)

company.add_employee("Shaan","AI & Blockchain Developer")
company.add_employee("Jake","Software Engineer")
company.add_employee("Luke","System Designer")


for emp in company.list_employees():
    print(emp)

# %%
