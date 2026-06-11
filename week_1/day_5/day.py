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

# Exercise 2: The Log Accumulator
# Imagine you are building a logging system. If you use "w" mode, you overwrite the old logs. We need to use append mode ("a").

# Create a loop that asks the user to input a log message. If they type "exit", the loop should stop.

# For any other input, open a file named app.log in append mode and write the user's input on a new line.

# Run the script, type a few lines, exit, and run it again. Check app.log to confirm the older lines were preserved!

log_path = r"D:\projects\python-core-concepts\week_1\day_5\app.log"
message = input("Enter a message: ")
while message != "exit":
    with open(log_path, "a") as file:
        file.write(message + "\n")
    message = input("Enter a message: ")

# Exercise 3: The High Score Tracker
# You are building a game and need to save player scores.

# Python
# import json

# # Your starting data
# leaderboard = {
#     "Player1": 2500,
#     "Player2": 1800,
#     "Player3": 1200
# }
# Save the leaderboard dictionary into a file named scores.json using json.dump(). Ensure you use the indent=4 argument to make the file human-readable.

# Now, write a separate block of code that opens scores.json in read mode, loads the data back into a Python dictionary using json.load(), updates "Player2"'s score to 2100, and adds a new player ("Player4": 950).

# Save this updated dictionary back into scores.json.

import json
from pathlib import Path

# Your starting data
leaderboard = {
    "Player1": 2500,
    "Player2": 1800,
    "Player3": 1200
}

scores_file_path = Path(r"D:\projects\python-core-concepts\week_1\day_5\scores.json")
if not scores_file_path.exists(): scores_file_path.touch()
with open(scores_file_path, "w") as file:
    json.dump(leaderboard, file, indent=4)

with open(scores_file_path, "r") as file:
    data = json.load(file)
data["Player2"] = 2100
data["Player4"] = 950
with open(scores_file_path, "w") as file:
    json.dump(data, file, indent=4)