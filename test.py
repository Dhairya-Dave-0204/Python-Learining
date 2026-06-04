# print("Hello")
# .\venv\Scripts\Activate.ps1
#str = "Programming"
#print(str[-2:-7])

# User input
# userInput = input("Enter your name here: ")
# print(userInput)

# Conditional statements
score = 80
if score >= 90 :
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# Switch case (match)
command = "start"
match command:
    case "start":
        print("System is starting...")
    case "stop":
        print("System is stopping...")
    case "restart":
        print("System is restarting...")
    case _:  # The underscore acts as the 'default' or 'else' case
        print("Unknown command.")

# Ternary operator like
age = 20
# Syntax: [value_if_true] if [condition] else [value_if_false]
status = "Adult" if age >= 18 else "Minor"
print(status)

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loops 5 times (0, 1, 2, 3, 4)
for i in range(5):
    print(f"Loop count: {i}")

# while loop
count = 1
while count <= 3:
    print(f"Number: {count}")
    count += 1

# Special else paired with for or while loop
# The else block executes only if the loop finished naturally 
# (it went through the entire sequence or the condition became false, without being interrupted by break)
for item in ["item1", "item2", "item3"]:
    print(item)
else:
    print("Loop finished successfully without hitting a break!")

# General function
def greet_user(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet_user("Alice", "Smith")

# Handle unknown number of arguments
# Using *args to accept any number of numbers. Receives arguments as a tuple.
def sum_all(*numbers):
    return sum(numbers)
print(sum_all(1, 2, 3, 4, 5))
# Using **kwargs to accept any number of named details. Receives arguments as a dictionary.
def user_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
user_profile(username="coder123", email="abc@eg.com", status="Active")

# Lambda Functions (The Anonymous One-Liners)
# Standard way
def square(x):
    return x * x
# Lambda way
# Syntax: lambda arguments: expression
square_lambda = lambda x: x * x
print(square_lambda(4))