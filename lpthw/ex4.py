# There are 100 cars
cars = 100

# Each car can accomodate 4 passengers
space_in_a_car = 4.0

# There are 30 drivers
drivers = 30

# There are 90 passengers
passengers = 90

# Available cars (i.e., cars without drivers)
cars_not_driven = cars - drivers

# Each driver has one car to drive
cars_driven = drivers

# Total number of seats available for carpool
carpool_capacity = cars_driven * space_in_a_car

# Average number of passengers for each car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
