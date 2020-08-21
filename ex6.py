# Creating a variable
types_of_people = 10
# formated string variable 
x = f"There are {types_of_people} types of people." # string in a string
# normal string variable
binary = "binary"
do_not = "don't"
# another string variable
y = f"Those who know {binary} and those who {do_not}." # string in a string

# printing formated string variables
print(x)
print(y)
# More printing with more formating
print(f"I said: {x}") # string in a string
print(f"I also said: {y}") # string in a string

# declaring boolean variable
hilarious = True
# alternate declaration of formated string variable
joke_evaluation = "Isn't that joke so funny?! {}"

# another format of using the format method
print(joke_evaluation.format(hilarious))

# regular string declaration
w = "This is the left side of ... "
e = "a string with a right side"

# string concatenation
print(w + e) 