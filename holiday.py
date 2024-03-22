def hotel_cost(city, num_nights):
    # Defining hotel rates for different cities
    city_rates = {
        'london': 150,
        'paris': 122,
        'barcelona': 92,
        'berlin': 78
    }

    # Checking if the provided city is in the rates dictionary
    if city.lower() in city_rates:
        rate_per_night = city_rates[city.lower()]
        total_cost = num_nights * rate_per_night
        return total_cost
    else:
        print("City not recognized. Cannot calculate hotel cost.")
        return 0  # Return 0 if the city is not recognized


def plane_cost(city_flight):
    # Defining flight cost for different cities
    if city_flight.lower() == 'london':
        return 222
    elif city_flight.lower() == 'paris':
        return 101
    elif city_flight.lower() == 'barcelona':
        return 234
    elif city_flight.lower() == 'berlin':
        return 172
    else:
        return 0  # Returning 0 if the city is not recognized


def car_rental(rental_days_wanted):
    # Defining cost per day for car rental
    return rental_days_wanted * 75


def holiday_cost(city_flight, num_nights, rental_days_input):
    # Calculateing costs for plane, hotel, and car rental
    plane_cost_value = plane_cost(city_flight)
    hotel_cost_value = hotel_cost(city_flight, num_nights)  # Pass 'city_flight' to 'hotel_cost'

    if rental_days_input.lower() == 'yes':
        # Asking user for rental days if they want to rent a car
        rental_days_wanted = int(input("Enter the number of days you want to rent the car: "))
        car_rental_value = car_rental(rental_days_wanted)
    else:
        print("Thank you for confirming that you will not need a car.")
        car_rental_value = 0

    # Calculating total holiday cost
    total_cost = plane_cost_value + hotel_cost_value + car_rental_value
    return total_cost

# Getting user input for destination, nights, and car rental preference
city_flight = input("Where are you flying to? (London, Paris, Barcelona, Berlin) ")

# Validate the city for the flight
if plane_cost(city_flight) == 0:
    print(f"We do not offer flights to {city_flight}. Please try again.")
else:
    num_nights_str = input("How many nights are you planning to stay? (Please enter a number) ")
    while not num_nights_str.isdigit():
        print("Please enter a valid number for the nights.")
        num_nights_str = input("How many nights are you planning to stay? (Please enter a number) ")

    num_nights = int(num_nights_str)

    rental_days_input = input("Would you like to rent a car? (yes/no) ")

    # Calculating and print total holiday cost
    total_holiday_cost = holiday_cost(city_flight, num_nights, rental_days_input)
    print(f"Total holiday cost for {num_nights} nights: $ {total_holiday_cost}")
