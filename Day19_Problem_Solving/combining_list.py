# %% Problem 1: The Math Equation (+)
"""
You are organizing two different groups of students for a field trip, and you need a single, 
brand new master list without changing the original group lists.

group_1 = ["Alice", "Bob"]
group_2 = ["Charlie", "Diana"]

Your Task:
Create a new variable called all_students and use the + operator to combine group_1 and 
group_2.
Print all_students.
"""
group_1 = ["Alice", "Bob"]
group_2 = ["Charlie", "Diana"]
all_students = group_1 + group_2
print(all_students)


# %% Problem 2: The Bingo Card (*)
"""
You need to generate a default row for a Bingo card where every starting square is marked 
as "Empty". You could type out ["Empty", "Empty", "Empty", "Empty", "Empty"], but that takes 
too long.

square = ["Empty"]

Your Task:
- Create a new variable called bingo_row and use the * operator to multiply the square list 
by 5.
- Print bingo_row.
"""
square = ["Empty"]
bingo_row = square * 5
print(bingo_row)


# %% Problem 3: The Ultimate Merge ([*...])
"""
This one connects back to the unpacking skills you mastered earlier! You have three separate 
lists of data, and you want to merge them all into one new list using the * unpacking 
operator inside new brackets.

front_end = ["HTML", "CSS"]
back_end = ["Python", "SQL"]
dev_ops = ["Docker", "AWS"]

Your Task:
- Create a variable called tech_stack.
- Open a new pair of brackets [] and inside them, use the * operator on each of the three 
lists, separated by commas (e.g., [*list_1, *list_2]).
- Print your brand new tech_stack list!
"""
front_end = ["HTML", "CSS"]
back_end = ["Python", "SQL"]
dev_ops = ["Docker", "AWS"]

tech_stack = [*front_end, *back_end, *dev_ops]
print(tech_stack)

# %% Problem 4: The Report Card (zip)
"""
You are writing a program for a teacher who has two separate lists: one for student names, 
and one for their final grades. You need to match them up perfectly.

students = ["Alice", "Bob", "Charlie", "Diana"]
grades = [95, 87, 92, 88]

Your Task:
- Create a new variable called report_card.
- Use the zip() function to pair the students list with the grades list, and wrap the whole 
thing in list() so it generates a readable list.
- Print your report_card. (You should see a list of tuples like [('Alice', 95), ...]).
"""

students = ["Alice", "Bob", "Charlie", "Diana"]
grades = [95, 87, 92, 88]

report_card = list(zip(students, grades))
print(report_card)


# %%
