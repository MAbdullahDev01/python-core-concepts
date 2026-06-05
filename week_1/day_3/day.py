# Exercise 1: The Coffee Order
# Write a function called make_coffee that simulates a barista order.

# It should take two parameters: size and milk_type.

# Give milk_type a default value of "whole milk".

# The function should return a string like: "Ordered a Large coffee with oat milk."

# Call the function twice and print the results:

# Once specifying both arguments ("Large", "oat milk").

# Once specifying only the size ("Medium"), letting the default milk take over.

def make_coffee(size : str, milk_type : str ="whole milk"):
    print(f"Ordered a {size} coffee with {milk_type}.")

make_coffee("Large", "oat milk")
make_coffee("Medium")

# Exercise 2: The Multi-Calculator (*args)
# Write a function called multiply_all that can take any number of numeric arguments and multiply them all together.

# Use *args to accept a flexible amount of numbers.

# If no arguments are passed, the function should return 0.

# Otherwise, return the product of all numbers.
# Example usage: multiply_all(2, 3, 4) should return 24.

def multiply_all(*args):
    if not args:
        return 0
    
    total = 1
    for num in args: total *= num
    return total

print(multiply_all(2,3,4))

# Exercise 3: The Profile Builder (kwargs)
# Write a function called build_user_profile that accepts a user's first_name and last_name as required arguments, but accepts any other details as keyword arguments.

# Use kwargs to capture the extra details.

# The function should return a dictionary containing all the information combined.
# Example input: build_user_profile("Jane", "Doe", role="Engineer", location="NYC")
# Expected output: {'first_name': 'Jane', 'last_name': 'Doe', 'role': 'Engineer', 'location': 'NYC'}

def build_user_profile(first_name, last_name, **kwargs):
    data = {"first_name" : first_name, "last_name" : last_name}
    for key, value in kwargs.items():
        data[key] = value 
    print(data)

build_user_profile("Jane", "Doe", role="Engineer", location="NYC")

# Exercise 4: The Scope Trap
# Look at this code snippet. Predict what it will print before running it, and explain why. Then, modify the function so it successfully increases the global counter by 1.

# Python
# counter = 0

# def increment_counter():
#     counter = counter + 1
#     print(f"Inside function: {counter}")

# increment_counter()
# print(f"Outside function: {counter}")

# the second print statement will show 0 as the global counter value doesn't change

counter = 0

def increment_counter():
    global counter
    counter = counter + 1
    print(f"Inside function: {counter}")

increment_counter()
print(f"Outside function: {counter}")