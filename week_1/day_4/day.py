# Exercise 1: The Script Shield
# Create a file named utility.py. Inside it, write a simple function:

# Python
# def greet_user(name):
#     return f"Hello, {name}!"
# Below the function, add an if __name__ == "__main__": block.

# Inside that block, call the function: print(greet_user("Developer")).

# The Test: * Run utility.py directly in your terminal. Does it print the greeting?

# Create a second file named main.py in the same folder. Write import utility and run main.py. Does it print the greeting? Explain why or why not based on how __name__ works.

from tkinter.filedialog import Directory

from utility import greet_user

greet_user("developer")

# the greeting wasn't printed when ran from day.py because __name__ only runs when the script is ran from the original file

# Exercise 2: The Automated Folder Cleaner
# Write a script that helps organize a messy computer directory.

# Import Path from pathlib.

# Define a path to a new directory called Project_Backup inside your current working directory.

# Check if Project_Backup already exists. If it doesn't, use your script to create the folder.

# Inside that new folder, create three empty text files programmatically named: notes.txt, todo.txt, and logs.txt.

from pathlib import Path 

directory = Path("D:/projects/python-core-concepts/week_1/day_4")
q = directory / "Project_Backup" 
if not q.exists(): q.mkdir()

file_paths = ["notes.txt", "todo.txt", "logs.txt"]
for file in file_paths:
    file_path = q / file
    file_path.touch()