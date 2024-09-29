temperature = float(input('Enter the temperature in farenheit: '))

if temperature <= 32:
    print('It is below freezing. Watch out for ice.')

    snowing = input('Enter "Y" if it is snowing today: ')

    if snowing == 'Y' + 'y' :
        print('Snow boots are recommended today')

else:
    print('It is above freezing today')