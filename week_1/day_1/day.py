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
