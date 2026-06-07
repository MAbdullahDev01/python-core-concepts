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

# Exercise 3: The Session Logger
# You need to save a user's login session configuration data to a file, including the exact time they logged in.

# Python
# import json
# from datetime import datetime

# session_data = {
#     "username": "coder_42",
#     "access_level": "Admin",
#     "login_time": datetime.now() # This will cause an issue!
# }
# If you try to run json.dumps(session_data), Python will throw a TypeError. Why?

# Fix the login_time value by converting the datetime object into a standardized string format using .strftime() (e.g., "2026-06-06 21:30:00").

# Save the updated dictionary into a file named session.json using json.dump().

import json
from datetime import datetime

session_data = {
    "username": "coder_42",
    "access_level": "Admin",
    "login_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

json_string = json.dumps(session_data)
json_file_path = Path(r"D:\projects\python-core-concepts\week_1\day_4\session.json")
if not json_file_path.exists(): json_file_path.touch()
with open(json_file_path, "w") as file: file.write(json_string)

# Exercise 4: The Environment Reporter
# Write a script named sys_report.py that gathers information about the environment it is running in and saves it as a clean report.

# Your Task:

# Use sys to capture:

# The version of Python currently running (sys.version).

# The operating system platform (sys.platform).

# Any command-line arguments passed to the script (sys.argv).

# Use pathlib to find the absolute path of the directory where your script is living.

# Bundle all of this information into a dictionary:

# Python
# report = {
#     "python_version": ...,
#     "os_platform": ...,
#     "script_directory": ..., # Must be a string, not a Path object!
#     "arguments_passed": ...
# }
# Save this dictionary as env_report.json.

# To test the master level: Run your script from the terminal while passing extra arguments, like this:

# Bash
# python sys_report.py --verbose --debug
# Open your generated JSON file to ensure --verbose and --debug were successfully captured inside the data!

import sys

report = {
    "python_version" : sys.version,
    "os_platform" : sys.platform,
    "script_directory" : str(Path(__file__).resolve()),
    "arguments_passed" : sys.argv
}

report_file_path = Path(r"D:\projects\python-core-concepts\week_1\day_4\env_report.json")
report_json = json.dumps(report)
if not report_file_path.exists(): report_file_path.touch()
with open(report_file_path, "w") as file: file.write(report_json)