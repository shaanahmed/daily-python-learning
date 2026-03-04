# %% Magic Methods 
"""
Magic methods(also called Dunder Methods, short for Double Underscore) are special methods 
that start and end with __.
They allow your custom objects to behave like built-in Python types.
"""

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
    


book1 = Book("1984", "George Orwell", 328)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book3 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 290)

# Testing

# __str__
print(book1)

# __eq__
print(book3 == book4)

# __lt__
print(book3 < book2)

# __gt__
print(book3 > book4)

# __add__
print(book2 + book3)

# __contains__
print("Hobbit" in book3)
print("Hobbit" in book2)

# __getitem__
print(book1["title"])
print(book2["title"])

print(book1["author"])

print(f"{book2["num_pages"]} pages")

# %%
