"""
Python: Overview and Uses
  Introduction
    Python was invented by Guido van Rossum in 1991.

  Uses of Python
    Web development
    Software development
    Mathematics
    System scripting
    Data science
  Why Python?
    Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc.).
    Python automatically identifies the types of variables.
  Variables & Data Types
    Variables: A variable is the name given to a memory location in a program.
Data Types
1. Integer
Holds numerical values, e.g., 1, 2, -1.
Inbuilt Functions and Operations for Integer:"""
num = 10
print(abs(num))     # Absolute value
# Output: 10

print(bin(num))     # Binary representation
# Output: 0b1010

print(hex(num))     # Hexadecimal representation
# Output: 0xa

print(pow(num, 2))  # Power function
# Output: 100

print(divmod(num, 3)) # Quotient and Remainder
# Output: (3, 1)
"""2. Floating Point Number
Holds decimal numbers, e.g., 1.1, 24.5.
Inbuilt Functions and Operations for Float:"""

price = 99.99
print(round(price))  # Round to nearest integer
# Output: 100
"""Typecasting:"""

print(int(price))        # Convert to integer
# Output: 99

print(float("1234"))     # Convert string to float
# Output: 1234.0
"""3. String
Holds sequences of characters, e.g., greeting = "hello world!".
Inbuilt Functions and Operations for String:"""

greeting = "hello world!"
print(greeting.lower())          # Convert to lower case
print(greeting.upper())          # Convert to upper case
print(greeting.replace("world", "python"))  # Replace substring
print(greeting.split())          # Split string into a list
print(greeting.find("world"))    # Find the substring
print(len(greeting))             # Length of string
"""4. List
Mutable collection that can store values of any data type, e.g., fruit = ["apples", "banana", "cherry"].
Inbuilt Functions and Operations for List:"""

fruit = ["apples", "banana", "cherry"]
fruit.append("orange")          # Add at end of the list
fruit.extend(["grape", "kiwi"]) # Add multiple elements at end
fruit.remove("banana")          # Remove an element
fruit.pop()                     # Remove the last element
fruit.sort()                    # Sort the list
print(len(fruit))               # Length of the list
print(fruit.index("cherry"))    # Find the index of a value
"""5. Tuple
Immutable collection, e.g., coordinates = (10.0, 20.0).
Inbuilt Functions and Operations for Tuple:"""

coordinates = (10.0, 20.0)
coordinates.count(10.0)   # Count occurrences
coordinates.index(10.0)   # Find index of value
print(len(coordinates))   # Length of the tuple

# Convert tuple to list to modify
li = list(coordinates)
print(li)
# Output: [10.0, 20.0]
"""6. Dictionary
Collection of key-value pairs, e.g., person = {"name": "Aizen"}.
Inbuilt Functions and Operations for Dictionary:"""

person = {"name": "Aizen"}
print(person.keys())    # Get all keys
print(person.values())  # Get all values
print(person.items())   # Get all key-value pairs
person.update({"age": 22}) # Update dictionary
person.pop("name")      # Remove value
print(len(person))      # Length of the dictionary
"""7. Set
Collection of non-repetitive elements, e.g., sem = {1, 2, 3, 4}.
Inbuilt Functions and Operations for Set:"""

sem = {1, 2, 3, 4}
print(len(sem))          # Length of the set
sem.add(5)               # Add value to the set

"""Conditional Statements
Example"""

a = 98
b = 99

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
"""In this example, the third condition is met, so it will print "a is greater than b"."""