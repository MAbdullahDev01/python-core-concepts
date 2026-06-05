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