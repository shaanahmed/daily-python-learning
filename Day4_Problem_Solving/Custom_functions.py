# %% 1. The Welcome Message (Arguments & Parameters)
"""Goal: Create a function that accepts data and uses it.
Task: Define a function called greet_artist that takes one parameter: artist_name.
Logic: Inside, print a personalized message like: "Welcome to the studio, [artist_name]!".
Action: Call (invoke) the function three times with different names: your name, "Justin", and your artist name "urthirstybby".
Skill: Understanding that Parameters are the placeholders in the definition, and Arguments are the actual values you pass in. """

def greet_artist(artist_name):
    print(f"Welcome to the studio, {artist_name}!")
greet_artist("Shaan")
greet_artist("Justin")
greet_artist("urthirstybby")


# %% 2. The Royalty Calculator (Multiple Parameters)
"""Goal: Pass multiple pieces of data into one function.
Task: Define calculate_earnings with two parameters: streams and pay_per_stream.
Logic: Multiply the two numbers and print the result.
Action: Call the function for a song with 5,000 streams and a rate of 0.004.
Skill: Handling the order of multiple arguments."""

def calculate_earnings(streams, pay_per_stream):
    return streams * pay_per_stream
calculate_earnings(5000, 0.004)


# %% 3. The Temperature Converter (The return Keyword)
"""Goal: Get a value back from a function to use later.
Task: Define celsius_to_fahrenheit that takes one parameter: celsius.
Logic: Use the formula: F = (C * 9/5) + 32.
Requirement: Instead of printing, use the return keyword to send the result back.
Action: 1. Call the function with the current temperature in Nha Trang (e.g., 28).2. 
Store the result in a variable called fahrenheit_temp.3. 
Print: "The temperature in Fahrenheit is: [fahrenheit_temp]". """

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
fahrenheit_temp = celsius_to_fahrenheit(28)
print(f"The temperature in Fahrenheit is: {fahrenheit_temp}|")


# %%  4. The Default Value Challenge (Optional Parameters)
"""Goal: Make an argument optional by giving it a default value.
Task: Create a function describe_vacation(city, country="Vietnam").
Logic: Print "I am currently visiting [city] in [country].".
Action: 1. Call it with only one argument: "Dalat". 2. Call it with two arguments: "Tokyo" and "Japan".
Skill: Understanding how Python uses the default value if the second argument is missing."""

def describe_vacation(city, country="Vietnam"):
    print(f"I am currently visiting {city} in {country}.")
describe_vacation("Nha Trang")
describe_vacation("Tokyo", "Japan")


# %% 
