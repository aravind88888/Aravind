# Get user input for a number
user_input = input("Enter a number: ")

# Convert the input to a float (assuming the user may enter a decimal number)
try:
    number = float(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Calculate the square of the number
result = number ** 2

# Display the result and a saying
print(f"The square of {number} is: {result}")
print("Here's a saying: 'In the middle of difficulty lies opportunity.' - Albert Einstein")

