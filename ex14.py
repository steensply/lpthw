# import modules
from sys import argv

# setting up the arguments to be passed.
script, user_name, address = argv

# creating a command like prompt
prompt = 'user@response:# '

# Begin conversation and question asking
print(f"Hi, {user_name}, I am the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
# calling the prompt and asking for user input
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

# summarising information from conversation
print(f'''
Alright, so you said {likes} about liking me.
You live at {lives} in {address}. Not sure where that is.
And you have a {computer} Computer. Nice.
''')