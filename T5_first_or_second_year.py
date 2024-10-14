# I commented out the code I wrote prior to following along with the lecture code example that you wrote

def first_or_second_year(class_code):
    if 1000<= class_code <= 1999:  # Defines range for first year class codes
        #print(f'{class_code} is a first year class code')  # This line will print if class code matches 1xxx format
        return 'First year'
    elif 2000 <= class_code <= 2999:  # Defines range for second year class codes
        #print(f'{class_code} is a second year class code')  # This line will print if class code matches 2xxx format
        return 'Second year'
    else:
        #print('This input is invalid, please try again.')  # This line will print if input doesn't match actual class codes
        return 'Invalid'


def main():
    class_code = int(input('What is your class code number: '))  # Class code input should be a four-digit number starting with 1 or 2
    result = first_or_second_year(class_code)
    print(result)


main()
