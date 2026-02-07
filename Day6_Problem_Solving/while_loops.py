# %% Problem 1: Countdown Timer
"""Difficulty: Easy
Write a program that takes a positive integer N as input and counts down from N to 1, 
printing each number on a separate line. After reaching 1, print "Blast off!".  """

n = int(input("Enter a positive integer: "))

while n > 0 :
    print(n)
    n -= 1
print("Blast Off!")

# %% Problem 2: Sum Until Negative
"""Difficulty: Easy
Write a program that continuously reads integers from the user until a negative number is entered. 
Print the sum of all positive numbers entered (excluding the negative number that stops the input)."""

total = 0

while True:
    n = int(input())
    if n < 0:
        break
    total += n
print(total)

# %% Problem 1: Print Numbers 1 to N
"""Difficulty: Very Easy
Write a program that takes a positive integer N as input and prints all numbers from 1 to N (inclusive), 
each on a separate line."""

n = int(input())
num = 1
while num <= n:
    print(num)
    num += 1

# %% Problem 2: Print Even Numbers
"""Difficulty: Very Easy
Write a program that takes a positive integer N as input and prints all even numbers from 2 to N (inclusive)."""

num = int(input())
n = 2
while n <= num:
    if n % 2 == 0:
        print(n)
    n += 1

# %% Problem 3: Multiplication Table
"""Difficulty: Easy
Write a program that takes a number N as input and prints its multiplication table from 1 to 10."""

n = int(input("Enter the multiplication table you want: "))
i = 1
while i <= 10 :
    print (f"{n} * {i} = {n * i}")
    i += 1


# %% Problem 4: Sum of N Numbers
"""Difficulty: Easy
Write a program that takes a positive integer N as input and prints the sum of all numbers from 1 to N."""

n = int(input("Enter a positive number: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print(total)

# %% Problem 5: Count Digits
"""Difficulty: Easy
Write a program that takes a positive integer as input and counts how many digits it has."""

n = int(input('Enter positive integer: '))
count = 0

while n > 0:
    n //= 10 
    count += 1
print(count)

# %% Problem 6: Print Odd Numbers in Reverse
"""Difficulty: Easy
Write a program that takes a positive integer N as input and prints all odd numbers from N down to 1."""

n = int(input())

while n >= 1:
    if n % 2 != 0:
        print(n)
    n -= 1

# %% Problem 7: Factorial Calculator
"""Difficulty: Easy
Write a program that takes a non-negative integer N as input and calculates its factorial (N!)."""

n = int(input())
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1
print("Factorial: ", fact)


# %% Problem 8: Guess the Number (Simple)
"""Difficulty: Easy
Write a program where the "secret number" is 7. Keep asking the user to guess until they get it right. 
When they guess correctly, print "Correct!" and stop."""

sec_num = 7

while True:
    n = int(input("Enter the secret number: "))
    if n == sec_num:
        print("CORRECT!")
        break
    else:
        print("Try again")


# %% Problem 9: Sum of Digits
"""Difficulty: Easy
Write a program that takes a positive integer as input and calculates the sum of its digits."""

n = int(input("Enter an int: "))
sum = 0

while n > 0:
    dig = n % 10
    sum += dig
    n //= 10
print(sum)


# %% Problem 10: Power Calculator
"""Difficulty: Easy
Write a program that takes two integers base and exponent as input and calculates base raised to the power of 
exponent using a while loop (don't use ** operator). """

# Power Calculator using while loop

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1
i = 0

while i < exponent:
    result *= base
    i += 1

print(f"{base} raised to the power of {exponent} is {result}")

# %%
