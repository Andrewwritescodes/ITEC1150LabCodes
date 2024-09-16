# This program will assess whether the user has an amount of pennies that is less than, equal to, or more than 1 dollar

# We need the user to input the amount of pennies they have
pennies = float(input('How many pennies do you have? ')) # This will save the user's input as a variable

if pennies <= 99:       # If user inputs any number less than 100, they have less than 1 dollar
    print('You have less than one dollar.')


elif pennies == 100:    # This line will only run if the user has exactly one dollar's worth of pennies
    print('You have one dollar.')

else:                   # This line will only run if user inputs amount greater than 1 dollar
    print('You have more than 1 dollar!')