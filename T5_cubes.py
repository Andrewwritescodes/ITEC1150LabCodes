def main():
    for number in range(10):
        c = cube(number)
        print(c)

def cube(value):
    cubed_value = value ** 3
    return cubed_value

main()