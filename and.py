# Program to determine whether user meets requirements to donate blood
weight = float(input('Please enter your weight, in pounds: '))
age = int(input('Please enter your age, in years: '))

if weight >= 110 and age >= 16:
    print('Great! You are eligible to be a blood donor.')
else:
    print('Sorry, you are not eligible to be a blood donor')