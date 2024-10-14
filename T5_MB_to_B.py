def main():
    Megabytes = float(input('Please enter number of Megabytes: '))  # First line that will print. This will ask user for input in MB
    Bytes = Megabytes_to_Bytes(Megabytes)   # Defines the variable "Bytes" with the next function
    print(f'{Megabytes} Megabyte(s) is equal to {Bytes} Bytes') # Final printed line of the program's output

def Megabytes_to_Bytes(Megabytes):  # Function needed to define the Bytes variable in the main() function
    Bytes = Megabytes * 1000000 # Calculates MB to B conversion
    return Bytes

main()