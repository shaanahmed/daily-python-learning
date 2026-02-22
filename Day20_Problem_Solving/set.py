# %% Problem 1: The Data Cleaner (Deduplication)
"""
You scraped some product IDs, but your scraper glitched and grabbed duplicates.

scraped_ids = [101, 102, 101, 103, 104, 102, 105]

Your Task:
In one line of code, convert scraped_ids into a set to destroy the duplicates, wrap it 
back in list(), and print the clean list.
"""
scraped_ids = [101, 102, 101, 103, 104, 102, 105]
print(list(set(scraped_ids)))

# %% Problem 2: The Skill Matcher (& and -)
"""
You are writing a recruiting app. You have a job that requires specific skills, and a 
candidate who has their own set of skills.

job_requirements = {"Python", "SQL", "Git", "AWS"}
candidate_skills = {"Python", "Java", "Git", "Docker"}

Your Task:

Create a variable called matched_skills using the intersection operator (&) to find out 
which required skills the candidate actually has. Print it!

Create a variable called missing_skills using the difference operator (-) to find out which 
required skills the candidate is lacking. Print it!
"""

job_requirements = {"Python", "SQL", "Git", "AWS"}
candidate_skills = {"Python", "Java", "Git", "Docker"}

matched_skills = job_requirements & candidate_skills  # we can also use .intersection()
print(matched_skills)

missing_skills = job_requirements - candidate_skills # we can also use .difference()
print(missing_skills)

# %% Problem 3: The Safe Unsubscribe (discard vs remove)
"""
A user wants to unsubscribe from your mailing list, but they double-clicked the button.

active_subs = {"alice@email.com", "bob@email.com", "charlie@email.com"}

Your Task:
Write code to remove "bob@email.com" from active_subs twice using the method that won't 
crash your program on the second attempt. Print the final set to confirm he is gone.
"""
active_subs = {"alice@email.com", "bob@email.com", "charlie@email.com"}
print(active_subs.discard("bob@email.com"), active_subs, sep = '\n')

# %% Problem 4: The Pangram Hacker (Strings + Sets)
"""
A "pangram" is a sentence that uses every single letter of the alphabet. You are writing a 
script that checks what letters a user is missing.

alphabet = set("abcdefghijklmnopqrstuvwxyz")
user_sentence = "the quick brown fox jumps over the lazy cat"

# Hint: You can convert a string directly into a set of its characters!
# user_chars = set(user_sentence)
Your Task:
Use set math to find out exactly which letters are missing from user_sentence. Create a 
variable called missing_letters, calculate the difference, and print it. 
(Hint: Make sure you subtract the user's characters FROM the alphabet, not the other way around!)
"""

alphabet = set("abcdefghijklmnopqrstuvwxyz")
user_sentence = "the quick brown fox jumps over the lazy cat"

user_sent = set(user_sentence)
missing_letters = alphabet - user_sent
print((missing_letters))


# %% Problem 5: The Strict Bouncer (Subsets and Supersets)
"""
You are building an authorization system. A user has certain permissions, but to access 
the admin panel, they must have all the required permissions.

required_perms = {"read", "write", "delete"}
user_perms = {"read", "write", "edit_profile", "delete", "comment"}

Your Task:
Write a single line of code that prints True if user_perms contains everything inside 
required_perms (meaning the user is a superset of the requirements). 
You can use the .issuperset() method or the >= operator.
"""

required_perms = {"read", "write", "delete"}
user_perms = {"read", "write", "edit_profile", "delete", "comment"}

print(required_perms.issubset(user_perms))
# or
print(user_perms.issuperset(required_perms))

# %% Problem 6: The Triple Overlap (Advanced Intersection)
"""
You are analyzing three different social media platforms, and you want to find the 
"super-influencers" who are trending on all three platforms at the exact same time.

tiktok_trending = {"Alice", "Bob", "Charlie", "David"}
insta_trending = {"Charlie", "Eve", "Alice", "Frank"}
twitter_trending = {"Grace", "Alice", "Charlie", "Heidi"}

Your Task:
You can chain set operators together! Create a variable called super_influencers and use 
the & operator to find the names that exist in all three sets simultaneously. 
Print the final set.
"""

tiktok_trending = {"Alice", "Bob", "Charlie", "David"}
insta_trending = {"Charlie", "Eve", "Alice", "Frank"}
twitter_trending = {"Grace", "Alice", "Charlie", "Heidi"}

super_influencers = tiktok_trending & insta_trending & twitter_trending
print(super_influencers)


# %%
