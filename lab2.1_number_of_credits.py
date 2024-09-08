# Program to as student's name and credits they're taking this semester

print() # Blank line

# Ask for their name
name = input('Please enter your name: ')

print() # Blank line

# Greet and ask about amount of credits taken this semester
print('Hello ' + name + '! How many credits are you taking this semester?')
credits_taken = int(input('Enter amount of credits: '))

print() # Blank line

# Print result that includes name and credits taken variables
print(name + ' is taking ' + str(credits_taken) + ' credits this semester.')
