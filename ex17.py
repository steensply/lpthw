# import modules to be used.

from sys import argv
# imports the exists module which returns True / False depending
# on if a file exist or not
# based on it's name
from os.path import exists
import os

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# we could do this two in one line how?
in_file = open(from_file).read()
# indata = in_file.read()


# print the size of the input file
print(f"The input file is {len(in_file)} bytes long")

# check if the output file exists or nor
print(f"Does the output file exist? {exists(to_file)}.")
# The program creates the output file if it does not exist
input("Ready, hit RETURN to continue or CTRL-C to abort.")

# open the output file and write the content of the in_file to it
out_file = open(to_file, 'w').write(in_file)
# out_file.write(in_file)

# print completed message and close both files
print("Alright, all done")
# out_file.close()
# in_file.close()
