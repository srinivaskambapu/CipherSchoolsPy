"""Functions, Lambda Expressions, and Error Handling
    Functions
        Definition: A function is a block of reusable code that performs a specific task. Functions help to modularize code, making it more organized and maintainable.

Simple Function"""
def add_numbers(x, y):
    return x + y

print(add_numbers(5, 7))
# Output: 12
"""Function with Default Argument"""

def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Alice"))
# Output: Hello, Alice!

print(greet("Bob", "Hi"))
# Output: Hi, Bob!
"""Function with Variable Arguments"""

def sum_all(*args):
    return sum(args)

print(sum_all(2, 4, 6, 8))
# Output: 20
"""Function with Keyword Arguments"""

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Charlie", age=25, city="New York")
# Output:
# name: Charlie
# age: 25
# city: New York
"""Lambda Expressions
Lambda expressions, also known as anonymous functions, are small, unnamed functions defined using the lambda keyword. They are often used for short, throwaway functions.

Use Case: Lambda expressions are commonly used in sorting algorithms where a custom sorting key is needed.

Simple Lambda Function"""

square = lambda x: x * x
print(square(6))
# Output: 36
"""lambda Function in map"""

numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)
# Output: [1, 4, 9, 16, 25, 36]
"""Lambda Function in filter"""

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4, 6]
#Lambda Function in sorted

students = [("Alice", 25), ("Bob", 23)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)
# Output: [('Bob', 23), ('Alice', 25)]
"""Error Handling
Error handling in Python is done using try, except, else, and finally blocks. This allows you to handle exceptions gracefully and ensure that the program continues to run.

Basic Try-Except Block"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
# Output: Cannot divide by zero
#Try-Except-Else Block

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")
# Output: Division successful
#Try-Except-Finally Block

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed")
# Output: Execution completed

#Handling Multiple Exceptions

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero")

#Raising Exceptions

def check_positive(number):
    if number <= 0:
        raise ValueError("Number must be positive")

try:
    check_positive(-5)
except ValueError as e:
    print(e)
# Output: Number must be positive