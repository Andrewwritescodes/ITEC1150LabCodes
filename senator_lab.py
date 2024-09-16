# This program will determine whether the user meets the criteria to be a senator
print('Do you meet the requirements to be a US senator? Find out by entering your information')
print() # Blank line for aesthetic

# First we'll need to define the requirements which are age, length of citizenship, and state of residence
age = int(input('Please enter your age: '))  # Requirement is 30 and up

citizenship_in_years = int(input('How many years have you been a US citizen? ')) # Requirement is 9 and up

state_of_residence = (input('In which state do you currently reside? ')) # Must match state_of_senator

state_of_senator = (input('In which state do you want to be the senator: '))  # Must match state_of_residence

if age >= 30 and citizenship_in_years >=9 and state_of_residence == state_of_senator: # If all criteria is met this will run
    print('You are eligible to run for senate in ' + state_of_senator)

if age <=29 or citizenship_in_years <= 8 or state_of_residence != state_of_senator:  # If they are ineligible for any reason this line will run instead
    print('You are ineligible to run for senate since do not meet one or more of the necessary criteria')