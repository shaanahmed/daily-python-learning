# %% simple file handling Task
"""
Create a file named test.txt manually.
Write a Python script using with open(...) and the a mode to add your name to it.
Run it three times.
Open the text file and see if your name appears three times.
"""

with open("test.txt","w") as f:
    f.write("Hi my name is Shaan Ahmed.\n")
    f.write("And I am learning python.\n")
    f.write("Today I am learning File Handling.     ")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)

# In this output we will get the end line spaces which is unefficient for large or big files

# %% Same but a bit different open style

with open("test2.txt","w") as f:
    f.write("Hi my name is Shaan Ahmed.\n")
    f.write("And I am learning python.\n")
    f.write("Today I am learning File Handling.                                 ")

with open("test2.txt", "r") as f:
    for lines in f:
        print(lines.strip())


# %% Pathlib
# To find the path of the file

from pathlib import Path

# This tells us the full "Home to File" address
path = Path("test2.txt").resolve()
print(f"The full path is: {path}")

# This tells us just the folder it sits in
print(f"The folder is: {path.parent}")


# %% Pathlib to find if the file exists

from pathlib import Path

my_file = Path(r"C:\Users\shaan\daily-python-learning\File_Handling\test2.txt")

if my_file.exists():
    content = my_file.read_text()  # Shortcut for opening, reading and closing
    print(content) 


# %% Advanced Tip: Dynamic Paths

from pathlib import Path

my_file = Path.home() / "daily-python-learning" / "File_Handling" / "test2.txt"
print(f"Looking at: {my_file}")

if my_file.is_file():
    print(my_file.read_text())  
else:
    print("File not found! Check the folder names.")


# %%
