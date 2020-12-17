# define addition 
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# define subtraction
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

# define multiplication
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

# define division
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")
# Calling the functions and assigning their outputs to variables
age = add (30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# displaying the newly computed variables
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.

print("Here is a puzzle.")

# Performing nested computation using the functions and variables just calculated
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# what_now = multiply(age, divide(height, subtract(weight, add(iq, 2))))
# try out this formula 
formula = add(24, divide(34, subtract(100, 1023)))

print("That becomes: ", what, "Can you do  it by hand?")

print("That becomes: ", formula, "Can you do  it by hand?")


