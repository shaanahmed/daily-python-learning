# %%1. The CSV Data Formatter
"""In real-world data science, you often deal with Comma Separated Values (CSV).
The Task: Take a string of data (e.g., "John,30,Engineer") and turn it into a professional summary line (e.g., "Name: John | Age: 30 | Job: Engineer").
How to do it:
Use split(",") to turn the string into a list.
Use method chaining to clean up any accidental spaces using strip().
Use " | ".join() to create the final formatted string."""

data = "John,30,Engineer"
result = " | ".join([f"{label}: {value.strip()}" for label, value in zip(["Name", "Age", "Job"], data.split(","))])
print(result)

# %% Another way
data = "John,30,Engineer"

# Split, strip, and format
parts = data.split(",")
cleaned_parts = [part.strip() for part in parts]
formatted = f"Name: {cleaned_parts[0]} | Age: {cleaned_parts[1]} | Job: {cleaned_parts[2]}"
print(formatted)


# %% 2. The URL Slug Creator
"""Websites often turn article titles into "slugs" for URLs (e.g., "Python is Great" becomes "python-is-great").
The Task: Take a user-inputted title and convert it into a lowercase, hyphenated URL.
How to do it:
Use .lower() to standardize the case.
Use .split() to get a list of the words.
Use "-".join() to connect the words with hyphens."""

article = "Python is Great".lower()
article = article.split()
print("-".join(article))


# %%3. The Reverse Sentence Generator
"""The Task: Take a full sentence from the user and print the words in reverse order, but keep the characters in each word in their correct order.
Sample Input: Learning Python is fun
Sample Output: fun is Python Learning
Hint: Combine split(), the slicing trick [::-1], and join()."""

sentence = "Learning Python is fun".split()
sentence.reverse()
print(" ".join(sentence))

# OR
ant_sentc = "Hi my name is Shaan".split()
rev_sentc = ant_sentc[::-1]
print(" ".join(rev_sentc))

# %%4. Advanced: The Integer Line Summer
"""This combines split() with the map() function you recently learned.
The Task: Ask the user for a line of numbers (e.g., 10 20 30 40). Calculate the total sum of these numbers.
Step-by-Step Logic:
Use input().split() to get a list of strings.
Use map(int, list_of_strings) to convert those strings into actual integers.
Use the built-in sum() function on that map object to get the total."""

user = input("Enter some numbers: ").split()
print(sum(map(int, user)))


# %%5. Multi-line Text Cleaner
"""The Task: You have a string with several lines of text. Split it into a list, but only keep lines that are not empty.
The Tool: Use splitlines() instead of split() to handle different types of line breaks automatically."""

para =  """Hello World

This is a test

Python is awesome


End of text"""

lines = para.splitlines()
non_empty_lines = [line for line in lines if line.strip()]
print(non_empty_lines)

# %%
