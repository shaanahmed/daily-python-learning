# %% Logging Module

import logging

# 1. Basic configuration
logging.basicConfig(
    filename='app.log',         # The file name
    level=logging.INFO,         # Minimum level to capture (skips DEBUG)
    format='%(asctime)s - %(levelname)s - %(message)s' # Time - Level - Msg
)

logging.info("The program has started.")
logging.warning("User input looks suspicious.")


# %% Simple Example of logging Exception Handling

import logging

logging.basicConfig(
    filename = "app.log",
    level = logging.ERROR,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

try:
    x = 10 / 0
except ZeroDivisionError:
    logging.exception("A math error occured!")

# %%

import logging

logging.basicConfig(
    filename = "app.log",
    level = logging.ERROR,
    # Added force=True so it actually updates your settings!
    force = True,
    format = '%(asctime)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s'
)

try:
    x = 10 / 0
except ZeroDivisionError:
    logging.error("A math error occured!")

# %%
