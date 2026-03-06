# %% ITERATOR
"""
An Iterable is like a bag of candy (a List, Tuple, or String). 
An Iterator is the hand that reaches into the bag and pulls one out at a time.

Iterable: Any object you can loop over.
Iterator: The object that actually remembers where it is in the sequence.

The "Manual" Way (What for loops hide from you)
When you write for x in [1, 2, 3], Python secretly does this:
    Calls iter() on the list to get an iterator.
    Calls next() repeatedly to get each value.
"""

my_list = [10,20,30]
hand = iter(my_list)

print(next(hand))
print(next(hand))
print(next(hand))

# %% The "Illegal" Advantage: Lazy Evaluation
"""
Why do professionals use iterators? Memory efficiency.

If you have a list of 1 billion numbers, your computer's RAM will explode. 
An iterator, however, only "exists" one item at a time. 
It doesn't store the whole list; it just knows how to calculate the next number.

"""

# %% The "Infinite Counter"
"""
This class can count to a trillion, but it uses almost zero RAM.

To turn a class into an iterator, you just need two "Magic Methods":
__iter__: Returns the iterator object itself.
__next__: Returns the next value.
"""

class TopOnePercentCounter:
    def __init__(self, high):
        self.current = 0
        self.high = high

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

counter = TopOnePercentCounter(3)
for n in counter:
    print(n)

# %%The "Log File Detective" Challenge
"""
The Scenario:
You are a Lead Engineer at a massive tech company. 
You have a 100GB log file (too big for your RAM). 
You need to find the first 5 "CRITICAL" error messages in that file, 
but you want to do it using zero extra memory.

Your Task:
Create a class called LogReader that acts as an Iterator.

__init__: It should take a list of log lines (to simulate a file).
__iter__: Standard setup.
__next__: It should search through the lines one by one.

If it finds a line containing the word "CRITICAL", it returns that line.
If it reaches the end of the logs without finding more, it raises StopIteration.
"""

class LogReader:
    def __init__(self, logs):
        self.logs = logs
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.logs):
            lines = self.logs[self.index]
            self.index += 1
            if "CRITICAL" in lines:
                print(lines)
        raise StopIteration


raw_logs = [
    "INFO: System start",
    "CRITICAL: CPU Overheating!",
    "DEBUG: Loading modules",
    "INFO: User logged in",
    "CRITICAL: Database connection lost!",
    "INFO: Routine backup complete"
]

scanner = LogReader(raw_logs)

print('Searching for the Critical Error!')

for error in scanner:
    print(f"Found: {error}")

# %%
