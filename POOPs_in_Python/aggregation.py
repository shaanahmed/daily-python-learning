# %% Aggregation
"""
It is a specialized form of Association where one object contains other objects, 
but those objects can exist independently. If the "parent" object is destroyed, the "child" objects still survive.
"""

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("Jorhat Public Library")

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("Machine Learning Yearning", "Andrew Ng")

library.add_book(book1)
library.add_book(book2)

print(library.name)

for books in library.list_books():
    print(books)


# %% The Problem: The "Department of Science"
"""
You are building a system to manage a university department. 
A Department aggregates several Professors.

The Requirements
Class Professor:
Constructor should take name and specialty.

Class Department:
Constructor should take dept_name.

It should have an empty list called faculty.

Methods for Department:
add_professor(prof): Adds a Professor object to the list.
get_faculty_details(): Returns a list of strings formatted as "Name (Specialty)".

Constraint:
Ensure that if the Department object is deleted, the Professor objects still exist (this is the core of Aggregation).
"""

class Professor:
    def __init__(self, name, speciality):
        self.name = name
        self.speciality = speciality

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.faculties = []

    def add_professor(self, faculty):
        self.faculties.append(faculty)

    def get_faculty_details(self):
        return [f"{faculty.name} is specialized in {faculty.speciality}" for faculty in self.faculties]
        
p1 = Professor("Dr. Ahmed", "Physics")
p2 = Professor("Dr. Sharma", "Mathematics")

science_dept = Department("Science")

science_dept.add_professor(p1)
science_dept.add_professor(p2)

for details_dept_science in science_dept.get_faculty_details():
    print(details_dept_science)



# %%
