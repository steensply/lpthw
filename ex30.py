people = 30
cars = 20 
trucks = 25

# compare the number of cars to the number of people ie 20 > 30
if cars > people : 
    print("We should take the cars.") # print this if the above comparism executes to true
elif cars < people and trucks < people: # boolean operations
    print("We shouldn't take the cars.")
else:
    print("We can't decide.") # if all the above comparisms are false then execute this line

if trucks > cars:
    print("That's too many trucks.") # only displayed if there are more trucks than cars
elif trucks < cars:
    print("Maybe we could take the trucks.") # only displayed if there are more cars than trucks
else:
    print("We still can't decide.") # displayed if the number of cars == number of trucks

if people > trucks or people < cars:
    print("Alright, let's just take the trucks.") #displayed if the people are more than the trucks or the cars are more than the people
else:
    print("Fine, let's stay home then.") # displayed if the number of trucks are more than the people or the number of cars are less than the people7