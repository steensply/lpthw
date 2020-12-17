# import module argv and creating argument variables

from sys import argv
script, filename = argv

# Initial display text
print(f"we are going to erase {filename}.")
print("If you don't want to erase the file then type CTRL + C (^C).")
input("If you want that, hit RETURN (ENTER) ?")

# input("?")
# Opening the file in write mode
print("Opening the file...")
target = open(filename, 'w')

# Deleting the content of the file 
print("Truncating the file, Goodbye")
target.truncate()

print("Now I am going to ask you for three lines:")

# Collecting input from the user to be written into the file
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write this to a file.")

# Writing the collected input to the file
# target.write(line1)
# target.write("\n") # place a new line at the end of each line written to file
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# target.write(line1 + "\n" + line2 + "\n" + line3)
target.write(f"{line1}. \n{line2}. \n{line3}.")

# Closing the file after write operation is done
print("And finally we close it.")
target.close()

# Re-opening the file in read mode to display it's content, then closing it again
new_target = open(filename)
print("\nDisplaying the contents of the file: ")
print(new_target.read())
new_target.close()