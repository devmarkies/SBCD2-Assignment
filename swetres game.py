import random

print("Welcome to the Swetres Game!")
winning_combination = [random.randint(0, 9) for _ in range(3)]
print("The winning combination has been generated!")
user_combination = []
print("Enter your 3-digit combination (0-9):")
for i in range(3):
    while True:
        try:
            digit = int(input(f"Digit {i + 1}: "))
            if 0 <= digit <= 9:
                user_combination.append(digit)
                break
            else:
                print("Please enter a number between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
if user_combination == winning_combination:
    print("Congratulations! daog ka!")
else:
    print(f"Sorry, patad nasab sunod. The winning combination was: {winning_combination}")
