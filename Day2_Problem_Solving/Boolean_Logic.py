# %% 1. The "Empty Check" (Conversion to Boolean)
"""Goal: Understand which values Python considers "Empty" or False.
Task: Create a program that takes a string input. Use the bool() function to convert that input to a Boolean.
Challenge: Run the program twice. Once, type something (e.g., "Vietnam") and see the result. The second time, just press Enter without typing anything.
Logic: This helps you understand "Falsy" values in Python."""

user = input("Enter anything: ")
print(bool(user))


# %% 2. The Login Gatekeeper (Logical and)
"""Goal: Practice requiring multiple conditions to be True.
Task: Create two variables: stored_username = "admin" and stored_password = "password123".
Input: Ask the user to input a username and a password.
Boolean Check: Create a variable is_logged_in that is True only if both the username and password match.
Output: Print: "Access Granted: [True/False]". """

stored_username = "admin"
stored_password = "password123"

user_username = input("Enter your username: ")
user_password = input("Enter your password: ")

is_logged_in = (user_username == stored_username) and (user_password == stored_password)
print(f"access Granted: {is_logged_in}")


# %% 3. The "Free Shipping" Rule (Logical or)
"""Goal: Practice cases where only one condition needs to be True.
Task: Ask the user for their total order amount (float) and if they have a "Member Coupon" (Boolean conversion from input).
Logic: A user gets free shipping if their order is over $50 OR if they have a coupon.
Output: Print: "Free Shipping applied: [True/False]"."""

order_amount = float(input("Enter your total shoppping amount: "))
member_coupon = input("Do you have a membership[Yes/No]: ").lower()

free_shipping = order_amount >= 50 or member_coupon == "yes"
print("Free Shipping applied:", free_shipping)


# %% 4. The Number Range Filter (Comparisons & not)
"""Goal: Combine comparisons with negation.
Task: Take an integer input.
Logic: Check if the number is not between 10 and 20 (inclusive).
Requirement: Use the not operator in your solution (e.g., not (number >= 10 and number <= 20)).
Output: Print: "Is the number outside the range? [True/False]"."""

num = int(input("Enter a number: "))
out_range = not(num >= 10 and num <= 20)
print("Is the number outside the range?", out_range)

# %%
