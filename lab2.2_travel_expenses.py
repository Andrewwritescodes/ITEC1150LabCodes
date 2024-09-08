#Program to calculate amount of money spent on bus fares last month
print() # Blank line

# Ask user how many times they rode the bus last month
bus_rides = int(input('How many times did you ride the bus last month: '))

# Ask user for the price of the bus ride
bus_fare = float(input('What is the price of one bus ride: '))

# Calculate total cost of bus rides
total = bus_rides * bus_fare
print() # Blank line

# Print output of total cost of bus rides taken last month
print('You rode the bus ' + str(bus_rides) + ' times last month. ' 'One bus ride costs $' + str(bus_fare) + '. Your total cost was $' + str(total) + '.')



