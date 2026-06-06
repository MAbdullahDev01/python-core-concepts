# Exercise 1: The Script Shield
# Create a file named utility.py. Inside it, write a simple function:

# Python
# def greet_user(name):
#     return f"Hello, {name}!"
# Below the function, add an if __name__ == "__main__": block.

# Inside that block, call the function: print(greet_user("Developer")).

# The Test: * Run utility.py directly in your terminal. Does it print the greeting?

# Create a second file named main.py in the same folder. Write import utility and run main.py. Does it print the greeting? Explain why or why not based on how __name__ works.

from utility import greet_user

greet_user("developer")

# the greeting wasn't printed when ran from day.py because __name__ only runs when the script is ran from the original file