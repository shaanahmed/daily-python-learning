# %% Problem 1: The Profile Builder
"""Create a function called user_info that takes a user's name (required) and then any 
number of additional details (like age, city, or job) using **kwargs.

The function should print:
"User: [name]"
" - [key]: [value]" for every extra detail.

Example:
user_info("Sarah", age=25, city="London")

User: Sarah
- age: 25
- city: London"""

def user_info(name, **kwargs):
    print(f"User : {name}")
    for key, value in kwargs.items():
        print(f" - {key} : {value}")

user_info("Shaan", age = 21, city = "Jorhat")
print()
# %% Problem 2: The Default Updater
"""Imagine you have a dictionary of default settings for a game:
defaults = {"theme": "Light", "volume": 50, "difficulty": "Easy"}

Create a function get_settings(**custom_updates) that:

Starts with the defaults dictionary.

Updates it with whatever the user passes in through **kwargs.

Returns the final dictionary.

Goal: Use the unpacking operator (**) inside the function to merge the dictionaries easily."""

def get_settings(**custom_updates):
    defaults = {"theme": "Light", "volume": 50, "difficulty": "Easy"}
    final_settings = {**defaults, **custom_updates}
    
    return final_settings

print("Test1 - No changes:")
print(get_settings())

print("_" * 60)

print("Test2 - Changing the theme and adding new settings:")
print(get_settings(theme = "Dark", language = "English UK", game_mode = "Hybrid"))

# %% Problem 3: The Argument Mixer (Order Challenge)
"""Look at the function definition below. One of these calls will cause a SyntaxError. 
Can you spot which one and explain why?
##python

def total_score(player_name, *points, **metadata):
    print(f"Player: {player_name}")
    print(f"Total Points: {sum(points)}")
    print(f"Extra Info: {metadata}")

# Call A
total_score("Kobe", 10, 20, 30, team="Lakers", status="Retired")

# Call B
total_score("Lebron", team="Lakers", 20, 30)"""

def total_score(player_name, *points, **metadata):
    print(f"Player: {player_name}")
    print(f"Total Points: {sum(points)}")
    print(f"Extra Info: {metadata}")

# Call A
total_score("Kobe", 10, 20, 30, team="Lakers", status="Retired")
print()
# Call B
total_score("Lebron", 20, 30, team="Lakers")
print()

# %% Problem 4: The HTML Tag Generator
"""Write a function make_tag(tag_name, content, **attributes) that creates an HTML string.

tag_name is the type of tag (e.g., "a" or "div").

content is the text inside.

**attributes are the properties like id or style.

Example:
make_tag("a", "Click Here", href="google.com", target="_blank")

Result: <a href="google.com" target="_blank">Click Here</a>"""

def make_tag(tag_name, content, **attributes):
    attr_string = ""
    for key, value in attributes.items():
        attr_string += f' {key}="{value}"'

    html_tag = f"<{tag_name}{attr_string}>{content}</{tag_name}>"
    return html_tag

# Test examples
print("Example 1 - Anchor tag with link:")
print(make_tag("a", "Click Here", href="google.com", target="_blank"))

print("Example 2 - Button with multiple attributes:")
print(make_tag("button", "Submit", type="submit", id="submit-btn", class_="btn-primary"))

print("Example 3 - Simple tag without attributes:")
print(make_tag("h1", "Welcome"))


# %%
