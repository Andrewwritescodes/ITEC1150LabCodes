school = 'Minneapolis College'
print(school)

name = 'Andrew'
print(name)

print(name + ' goes to ' + school)

favorite_food='Chicago tavern style pizza'
print(favorite_food)
print('My name is ' + name + ', I go to ' + school + ', and my favorite food is ' + favorite_food)

credits_taken = 6
print(credits_taken)

print('This semester I am taking ' + str(credits_taken) + ' credits.')

astronauts = 554
tourists = 7
total_people_in_space = astronauts + tourists
print(total_people_in_space)

miles_to_portland = 1425.81
miles_to_helena = 907.29
miles_helena_to_portland = miles_to_portland - miles_to_helena
print('It is ' + str(miles_helena_to_portland) + ' miles from Helena to Portland')

popcorn_cost = 4.25
bags_purchased = 3
# Multiply cost per bag by total bags purchased to calculate total
total_cost = popcorn_cost * bags_purchased
# Display total
print(total_cost)

name = input('Please enter your name: ')
print('Hello, ' + name)
name_length = len(name)
print('Your name is ' + str(name_length) + ' letters long')

miles_to_Seattle = float(input('How many miles to Seattle? '))
km_to_Seattle = miles_to_Seattle * 1.609
print('It is ' + str(km_to_Seattle) + ' kilometers to Seattle')