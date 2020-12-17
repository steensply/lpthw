# define function that takes two arguments and prints out stuff

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man that's enough for a party")
    print("Get a blanket. \n")
#script execution starts here where the function is called the first time with it's two arguments
print("We can just give the function numbers directly")
cheese_and_crackers(20, 30)

# two new variables are created and assigned values
print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

# the variables are then passed as arguments to the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# addition is performed on the arguments of the function and the result is passed to the function
print("We can even do math inside too:")
cheese_and_crackers(20 + 10, 5 + 6)

# addition is performed on the variables and the results are passed as arguments to the function
print("And we can combine the two variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def people(girls, boys):
    print(f"We have {girls} girls")
    print(f"We have {boys} boys")
    print("That is enough people to have a house party")
    print('''Get the weed and alcohol. 
We are about to turn up.
Let's get this party started.
''')

print("Start the party")
people(20, 15)

print("Not enough girls for the party!")
people(20 - 18, 10)

print("Not enough guys at this party")
people(59, 12)

number_of_girls = int(input("How many girls are there? > "))
number_of_boys = int(input("How many guys are coming? > "))

print("This is a sausage fest")
people(number_of_girls, number_of_boys ** 2)

print("It's a numbers game")
people(number_of_girls * 2, number_of_boys + 3)


