def main():
    miles = float(input('Please enter a number of miles: '))    # First line of the program that will print. This will require user to input number of miles
    kilometers = miles_to_kilometers(miles) # Assigns value to the kilometers variable based on input from the "kilometers_to_miles(miles)" function
    print(f'{miles} miles is equal to {kilometers} kilometers') # Final line that will print in the program that will print

def miles_to_kilometers(miles):
    km = miles * 1.60934    # Equation for converting miles to kilometers
    return km

main()