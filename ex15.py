# import modules
from sys import argv

# declaring the argv variables for the script and the filename at runtime
script, filename = argv

# opening the file to access it's content
txt = open(filename)

# Displaying the filename and reading/displaying it's content using the read method 
print(f"Here is your file {filename}:")
print(txt.read().strip())
txt.close()
print("\n")
# asking user to input the filename from keyboard and opening it for read
print("Type the filename again: ")
file_again = input("> ")

# reading the opened file and printing it's contents on the stdout
txt_again = open(file_again)
print(txt_again.read())
txt.close()