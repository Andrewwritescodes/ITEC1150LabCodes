star_id = input('Please enter your StarID: ')

if len(star_id) >= 9:
    print('Your StarID is too long.')
elif len(star_id) == 8:
    print('Your StarID is the correct length.')
else:
    print('Your StarID is too short.')