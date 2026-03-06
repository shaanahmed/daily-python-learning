# %% GENERATORS

"""
The Magic Word: yield
The only thing that makes a function a Generator is the word yield.

return: Kills the function. It says, "I'm done, here's the result, goodbye!"

yield: Pauses the function. It says, "Here’s a value for now. 
I’ll wait right here until you need the next one."
"""

# The "Standard" Way (Slow/Heavy):

def get_n_list(n):
    result = []

    for i in range(n):
        result.append(i)
    return result
    
print(get_n_list(5))

# %% The "Generator" Way (Fast/Light):

def get_no_generator(n):
    for i in range(n):
        yield i

print(list(get_no_generator(6)))


# %%Advanced Level: Generator Expressions
"""You know how you can make a list in one line? [x for x in range(10)].
You can do the same with generators, but it's even more powerful. 
Just change the brackets [] to parentheses ().
"""
# This is a GENERATOR (Memory: Near Zero)

my_gen = (i**2 for i in range(5))
print(list(my_gen))

# This is the SAME . Just showing that I also know walrus GENERATOR (Memory: Near Zero)
# Just showing that I am learning python and trying to learn each and evert topic

my_gen = (sq for i in range(5) if (sq := (i**2)))
print(list(my_gen))
# It's giving 1 because it is False, the generator skips this iteration. 
# It never "yields" the 0.


# %% The "Boss Level" Concept: Chaining
"""
This is the secret of high-frequency trading and massive data pipelines. 
You can plug generators into each other like Lego bricks. 
The data "flows" through them without ever being stored.
"""

def get_lines(file_name):
    for line in open(file_name):
        yield line

def clean_lines(lines):
    for line in lines:
        yield line.strip().upper()

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

logs = get_lines(r"c:\Users\shaan\daily-python-learning\Generators\generator_file_search.txt")
clean = clean_lines(logs)
errors = filter_errors(clean)

for e in errors:
    print(e)



# %%

#BELOW ARE JUST THE OTHER STEPS FOR CREATING AND SEARCHING FILE LOCATION FOR THE ABOVE PROBLEM
# %%

with open("generator_file_search.txt", "w") as file:
    file.write("""INFO: Application started successfully
DEBUG: Loading configuration from config.yaml
INFO: Database connection established
ERROR: Failed to fetch user data from API endpoint /users/123
DEBUG: Retrying connection attempt 1 of 3
WARNING: Slow response time detected on server node-4
ERROR: Timeout occurred while connecting to cache server
INFO: Cache server reconnection attempted
DEBUG: Memory usage at 74% capacity
INFO: Scheduled job 'cleanup_temp_files' started
ERROR: Permission denied when accessing /var/logs/archive
WARNING: Disk space below 20% threshold on mount /data
INFO: User session started for user_id: 9021
DEBUG: Query executed in 340ms on table 'transactions'
ERROR: Null pointer exception in module payment_processor.py at line 88
INFO: Backup process initiated for database snapshot
DEBUG: Thread pool size adjusted to 12
WARNING: Deprecated API version called by client 10.0.0.55
ERROR: SSL certificate validation failed for host secure.payments.io
INFO: Email notification sent to admin@company.com
DEBUG: Cache hit ratio: 91.3%
INFO: New user registered with id: 4402
ERROR: Database deadlock detected on table 'orders' during transaction
WARNING: Rate limit threshold reached for API key ending in ...7f3a
DEBUG: Parsing XML response from third-party service
INFO: File upload completed: report_2024_q1.pdf
ERROR: Out of memory error in worker process PID 3812
DEBUG: Websocket connection opened from 192.168.1.45
INFO: Health check passed for all services
ERROR: Invalid credentials provided for admin login attempt from IP 203.45.67.89""")

# %%

from pathlib import Path

path = Path("generator_file_search.txt").resolve()
print(path)

# %%
import os

path = "generator_file_search.txt"
if os.path.exists(path):
    print(os.path.abspath(path))


# %%
