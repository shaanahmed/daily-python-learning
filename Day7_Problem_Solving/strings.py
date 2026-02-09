# %% 1. The Data Cleanup Specialist
"""You are given a messy string from a user input: " ###Python_Programming_Is_Fun### "
A. Use a method to remove the leading and trailing whitespace.
B. From that result, remove the leading and trailing "#" characters.
C. Finally, replace the underscores "_" with single spaces.
D. Challenge: Can you do all of this in one line by "chaining" the methods?"""

user = " ###Python_Programming_Is_Fun### "
cleaned = user.strip().strip("#").replace("_", " ")
print(cleaned)

# %% 2. The Email Validator
"""Imagine you are checking a user's email address: user_name = " Contact@MyDomain.COM "
A. Standardize the email by converting it entirely to lower case and removing all surrounding whitespace.
B. Use a boolean method to check if the cleaned email ends with ".com".
C. Use a membership operator to check if the "@" symbol is present in the string."""

user_name = " Contact@MyDomain.COM "

email = user_name.strip().lower()
print(email.endswith(".com"))
print("@" in email )


# %% 3. The Substring Detective
"""Consider the sentence: "She sells sea shells by the sea shore."
A. Use a method to count how many times the word "sea" appears.
B. Use a method to find the index of the first occurrence of "shells".
C. What happens if you try to use .index("ocean") on this string? What happens if you use .find("ocean") instead?"""

sentence = "She sells sea shells by the sea shore."

print(sentence.count("sea"))
print(sentence.index("shells"))
print(sentence.find("ocean"))  # this will return -1
# print(sentence.index("ocean")) #this will return ValueError
# %%4. The Name Formatter
"""A database has names stored inconsistently: author = "cHaRlOtTe BrOnTë"
A. Use a method to format the name into Title Case (where only the first letter of each word is capitalized).
B. Using what you learned about normalization, replace "ë" with "e" to make it ASCII-friendly."""

author = "cHaRlOtTe BrOnTë".title()
print(author)
print(author.replace("ë","e"))
# %%5. Indexing and Slicing (Mental Check)
"""The string is word = "abracadabra"
A. What is returned by word.find("ra")?
B. What is returned by word.rfind("ra")?
C. What is the result of word.find("ra", 5)?"""

word = "abracadabra"
print(word.find("ra"))
print(word.rfind("ra"))  #it will return 9. Since rfind() method finds from the right side
print(word.find("ra", 5))
# %%
