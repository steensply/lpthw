# i = 0
numbers = []

def loop(i, c):
    while i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += c
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

# print("The numbers: ")
# for num in numbers:
#     print(num)
loop(0, 1)
print("------------------")

def listgen():
    cons = 0
    for cons in range(0, 6):
        print(f"At the top i is {cons}")
        numbers.append(cons)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {cons}")
    return numbers

listgen()