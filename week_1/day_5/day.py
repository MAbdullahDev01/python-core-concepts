# Exercise 1: The Journal App
# Write a script that creates a simple text file and reads it back.

# Use the with open() context manager to create (or overwrite) a file named journal.txt in write mode ("w").

# Write three lines of text into the file (e.g., your goals for learning Python).

# Open the same file using a context manager in read mode ("r").

# Read the contents and print them out to the console.

journal_path = r"D:\projects\python-core-concepts\week_1\day_5\journal.txt"

with open(journal_path, "w") as file:
    file.write("Learn the basics \n")
    file.write("Get better \n")
    file.write("Be the best!! \n")

with open(journal_path, "r") as file:
    line = file.read()
    if line:
        print(line)
    else:
        print("Empty file.")