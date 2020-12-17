# import the argv method from the sys libraries / modules
# from sys import argv
# number of arguments to pass when running the program. one in this case
# script, input_file = argv

# function that prints the whole content of the file opened
def print_all(f):
    print(f.read())
    print("\n")

# function to rewind the print operation.
def rewind(f):
    f.seek(0) # the seek method moves to a specific position within the file based on
              # the offset (0 means the start of the file)

# Reads the file one line at a time and is used with the rewind function
def print_a_line(line_count, f):
    print(line_count, f.readline()) # prints the line number and it's contents

# Open the file 
# current_file = open(input_file)
current_file = open(input("Enter the file name: "))

# Start the program display and print the entire file contents 
print("First let's print the whole file:\n")
print_all(current_file)

# start the rewind process
print("Now let's rewind, Kind of like a tape.")

rewind(current_file) # the value of current line becomes the line_count

print("Let's print four lines: ")
# Printing the lines of the file 
current_line = 1
print_a_line(current_line, current_file) # current_line = 1

current_line+= 1 # same as current_line = current_line + 1 [counter to increment the line count by 1]
print_a_line(current_line, current_file) # current_line = 2

current_line+= 1
print_a_line(current_line, current_file) # current_line = 3

current_line+= 1
print_a_line(current_line, current_file) # current_line = 4