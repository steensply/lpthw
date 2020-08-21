# print a regular string
print('Mary had a little lamb.')
# print the format string with the new string snow
snow = "snow"
print("Its fleece was white as {}.".format(snow))
# print the normal string
print("And everywhere that Mary went.")
# print the . 10 times
print("." * 10) # what does that do?

# declaring 12 variables with names end1 - end 12 and assigning each variable a character
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# string concatenation using the * operator
print(end1 + end2 + end3 + end4 + end5 + end6, end= ' ') # end=' ' us used to get rid of the \n character. The next print continues on the same line.
print(end7 + end8 + end9 + end10 + end11 + end12)