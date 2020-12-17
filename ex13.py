
# importing from the sys module
# importing modules
from sys import argv

# read the WYSS section for now to run this

# parsing the variables listed below as arguments to the python command.
# all the arguments on the lhs are unpacked and placed into argv
# all this arguments are checked at run time

# syntax: python3 ex13.py first second third
script, first, second, third = argv

# Printing the argument names passed
print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# combining input() with argv
yob = int(input("Enter your year of birth: "))
cy = int(input("Enter the current year: "))
age =  cy - yob
print(f"So, you're {age} years old.")
