# Exercise 1: The Bouncer
# Write a script that checks a person's age and determines if they can enter a venue.

# Create a variable age.

# Use if, elif, and else blocks:

# If age is under 18, print "Access Denied."

# If age is between 18 and 20 (inclusive), print "Enter, but no drinking."

# If age is 21 or older, print "Access Granted. Enjoy!"
age = int(input("Enter your age: "))
if age < 18:
    print("Access Denied.")
elif age > 21:
    print("Access Granted. Enjoy!")
else:
    print("Enter, but no drinking.")

# Exercise 2: The Custom Countdown
# Write a while loop that starts at 5 and counts down to 1, printing each number.

# After the loop finishes, print "Blast off!".

# Rewatch your logic: ensure the loop doesn't run infinitely!

count = 5
while count >= 1:
    print(count)
    count -=1

# Exercise 3: The Filter & Square
# You have a list of raw numbers:

# Python
# numbers = [2, 5, 8, 11, 14, 17, 20]
# Write a standard for loop that iterates through numbers.

# Inside the loop, check if a number is greater than 10.

# If it is, square it (multiply it by itself) and append it to a new list called squared_above_ten.

# Print the final list. (Expected: [121, 196, 289, 400])

numbers = [2, 5, 8, 11, 14, 17, 20]

squared_above_ten : list[int] = [num**2 for num in numbers if num > 10]
# for num in numbers:
#     if num > 10:
#         squared_above_ten.append(num**2)
#         count += 1

print(squared_above_ten)

# Exercise 4: Grade Book Classifier
# You have a dictionary of student names and their numeric scores:

# Python
# scores = {"Alice": 88, "Bob": 55, "Charlie": 92, "Diana": 68}
# Use a Dictionary Comprehension to create a new dictionary called grade_book.

# The keys should remain the students' names.

# The values should be "Pass" if the score is 70 or above, and "Fail" if the score is below 70.

# Print grade_book. (Expected: {'Alice': 'Pass', 'Bob': 'Fail', 'Charlie': 'Pass', 'Diana': 'Fail'})

scores = {"Alice": 88, "Bob": 55, "Charlie": 92, "Diana": 68}

grade_book : dict = {name : "Pass" if scores[name] >= 70 else "Fail" for name in scores }
print(grade_book)