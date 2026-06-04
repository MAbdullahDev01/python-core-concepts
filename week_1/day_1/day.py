# Exercise 1: The Receipt Generator
# You are building a primitive checkout system.

# Create a variable item_name with the value "iced latte".

# Create a variable price with the string value "4.99".

# Create a variable quantity with the integer value 3.

# Calculate the total cost. Hint: You will need to coerce (convert) the price string into a float first.

# Print the result using an f-string so it matches this exact format:
# "3 x iced latte = $14.97"

import queue


item_name : str = "iced latte"
price : str = "4.99"
quantity : int = 3
total_cost : float = quantity * float(price)

print(f"{quantity} x {item_name} = ${total_cost}")

# Exercise 2: Type Detective
# Look at the following collection:

# Python
# mystery_bag = {10, "10", (10,), 10.0}
# What Python data type is mystery_bag?

# Print the length of mystery_bag. Is it 4, or something else? Why?

mystery_bag : set = {10, "10", (10,), 10.0}
# mystery_bag is a set

print(mystery_bag)
# length is 3 because set do not contain duplicates so 10.0 is dropped as 10 = 10.0

# Exercise 3: The Secret Agent Slicer
# You received an encrypted coordinates string from headquarters:

# Python
# secret_msg = "X99A-40.7128,-74.0060-OMEGA"
# Extract just the latitude and longitude ("40.7128,-74.0060") by slicing the string.

# Use a string method to split that slice into a list containing two strings: ['40.7128', '-74.0060'].

# Convert those string values into a tuple of two floats: (40.7128, -74.0060).

secret_msg = "X99A-40.7128,-74.0060-OMEGA"
latitude = float(secret_msg[5:12])
longitude = float(secret_msg[13:21])
coordinates = (latitude, longitude)
print(coordinates)

# Exercise 4: The Locked Vault
# Consider the following data structures:

# Python
# combo_list = [1, 2, 3]
# combo_tuple = (1, 2, 3)
# Try to change the second element (index 1) of combo_list to 99. Print the list.

# Try to change the second element of combo_tuple to 99.

# Write down a brief explanation of the error message you receive and what it teaches you about lists vs. tuples.

combo_list : list = [1, 2, 3]
combo_tuple : tuple = (1, 2, 3)
combo_list[1] = 99
print(combo_list)
#combo_tuple[1] = 99 TypeError: 'tuple' object does not support item assignment
print(combo_tuple)
# Lists can be edited but tuples cannot

# Exercise 5: The Inventory Merger
# You manage a bookstore. You have a dictionary of current stock and a list of newly arrived books.

# Python
# stock = {"The Hobbit": 5, "1984": 2, "Gatsby": 0}
# new_arrivals = ["1984", "Dune", "1984", "The Hobbit", "Dune", "Dune"]
# Filter the new_arrivals list using a set to get a collection of unique new book titles.

# Update the stock dictionary using the new_arrivals list:

# If a book is already in stock, increment its count by how many times it appears in new_arrivals.

# If a book is not in stock, add it with its correct count.

# Print the final stock dictionary. (Expected output: {'The Hobbit': 6, '1984': 4, 'Gatsby': 0, 'Dune': 3})

stock = {"The Hobbit": 5, "1984": 2, "Gatsby": 0}
new_arrivals = ["1984", "Dune", "1984", "The Hobbit", "Dune", "Dune"]

new_arrivals_set : set = set(new_arrivals)
print(new_arrivals_set)

for book in new_arrivals:
    for title in stock:
        if title == book:
            stock[title] += 1
    if book not in stock:
        stock[book] = 1
print(stock)

# Exercise 6: The Data Normalizer
# You are handed raw, messy data from an old database API. It looks like this:

# Python
# raw_data = [
#     ("user1", "  active  ", "105"),
#     ("user2", "INACTIVE", "0"),
#     ("user1", "active", "15"), # Duplicate user!
#     ("user3", "  Active ", "42")
# ]
# Write a script that processes raw_data into a clean, searchable dictionary called clean_users.

# Rules for processing:

# No Duplicates: If a username has already been processed, add the new points to their existing points.

# Clean Strings: User statuses must be completely lowercase and stripped of all whitespace (e.g., "  active  " becomes "active").

# Correct Types: Points must be stored as integers, not strings.

# The final output should look exactly like this:

# Python
# {
#     "user1": {"status": "active", "points": 120},
#     "user2": {"status": "inactive", "points": 0},
#     "user3": {"status": "active", "points": 42}
# }

raw_data = [
    ("user1", "  active  ", "105"),
    ("user2", "INACTIVE", "0"),
    ("user1", "active", "15"), # Duplicate user!
    ("user3", "  Active ", "42")
]

processed_data = {}

for user, status, points in raw_data:
    cleaned_status = status.lower().strip()
    int_points = int(points)
    
    if user not in processed_data:
        processed_data[user] = {"status" : cleaned_status, "points" : int_points}
    else:
        processed_data[user]["points"] += int_points
        
print(processed_data)