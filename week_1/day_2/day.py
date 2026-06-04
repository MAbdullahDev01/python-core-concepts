# Exercise 1: The Bouncer
# Write a script that checks a person's age and determines if they can enter a venue.

# Create a variable age.

# Use if, elif, and else blocks:

# If age is under 18, print "Access Denied."

# If age is between 18 and 20 (inclusive), print "Enter, but no drinking."

# If age is 21 or older, print "Access Granted. Enjoy!"

if age := int(input("Enter your age: ")) < 18:
    print("Access Denied.")
elif age > 21:
    print("Access Granted. Enjoy!")
else:
    print("Enter, but no drinking.")