# %% Problem 1: The High Scores (sort vs reverse)
"""
You are building an arcade game, and you need to display the top scores from highest to lowest.

scores = [450, 920, 110, 880, 340]

Your Task:
First, use .sort() to put the scores in order from lowest to highest.
Next, use .reverse() to flip that sorted list upside down so the highest score is first.

Print the final scores list.
(Note: You could do this in one step with reverse=True, but this proves you know how both 
methods work!)
"""
scores = [450, 920, 110, 880, 340]
scores.sort()
scores.reverse()
print(scores)


# %% Problem 2: The Original Playlist (sorted)
"""
You have a carefully curated playlist. You want to see what it looks like in alphabetical 
order, but you do not want to ruin your original custom order!

playlist = ["Wonderwall", "Bohemian Rhapsody", "Smells Like Teen Spirit", "Hotel California"]

Your Task:
Create a new variable called alphabetical_playlist and assign it the result of the sorted() function.
Print alphabetical_playlist to see the A-Z order.
Print the original playlist to prove that it remained completely untouched!
"""
playlist = ["Wonderwall", "Bohemian Rhapsody", "Smells Like Teen Spirit", "Hotel California"]
alphabetical_playlist = sorted(playlist)
print(playlist)
print(alphabetical_playlist is playlist)

# %% Problem 3: The Race Results (sort(reverse=True))
"""
You have a list of finishing times for a 5K race (in minutes). A glitch in the system 
means you need to sort them from slowest to fastest (highest number to lowest number) in a
single line of code.

race_times = [22.5, 19.8, 25.1, 18.2, 28.0]

Your Task:
Use the .sort() method with the reverse=True argument inside the parentheses to sort the 
list descending in-place.
Print the race_times list.
"""
race_times = [22.5, 19.8, 25.1, 18.2, 28.0]
race_times.sort(reverse=True)
print(race_times)

# %%
