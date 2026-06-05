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