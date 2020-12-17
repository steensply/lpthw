print(""" You enter a room with two doors.
Do you go through door #1, door #2 or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("\t 1. Take the cake.")
    print("\t 2. Scream at the bear.")

    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("The bear eats your legs off. Good Job!")
    else:
        print(f"Well doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("\t 1. Blueberries.")
    print("\t 2. Yellow jacket clothespins.")
    print("\t 3. Understaning revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
elif door == "3":
    print("Proceed to the next room.")
    print("""You see a map on the floor.
    What do you do?""")
    print("\t 1. Pick up the map")
    print("\t 2. Ignore the map")

    map = input("> ")

    if map == "1":
        print("Find the treasure location on the map.")
        print("""There are two routes to be taken.
        one on the left and the other on the right """)
        print("which one do you take?")

        route = input("> ")

        if route == "left":
            print("You encounter a giant smelling pig.")
            print("The pig eats off your face and you die.")
        
        elif route == "right":
            print("You see two rooms ahead.")
            print("""The treasure is in one of the rooms.
            Do you choose room #1 or room #2?""")

            room = input("> ")
            if room == "1":
                print("""You run into a trap and an arrow goes through your head.
                You bleed out and die.""")
                print("\t Game over")
            elif room == "2":
                print("Congratulations you have found the treasure and saved the village.")
                print("You win a Gold star and proceed to the next level. Good Job!")
            else:
                print("You missed a turn and forfeited the game. You lose!")
        else:
            print("You took the wrong route, fell into a hole and died. Game over!")
    
    elif map == "2":
        print("You ignored the map and got lost in the abyss. No where to go.")
        print("The game is stuck and you lose!")
    
    else:
        print("You have no clue what you are doing and should quit the game immediately. Bye!")

else:
    print("You stumble around and fall on a knife and die.")
    print("Game Over!")
