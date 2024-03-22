def holiday_cost(city_flight, num_nights, rental_days_input):
    # Calculate costs for plane, hotel, and car rental
    plane_cost_value = plane_cost(city_flight)
    hotel_cost_value = hotel_cost(city_flight, num_nights)

    if rental_days_input.lower() == 'yes':
        # Asking user for rental days if they want to rent a car
        while True:
            try:
                rental_days_wanted = int(input("Enter the number of days you want to rent the car: "))
                break
            except ValueError:
                print("Please enter a valid integer for the number of days.")
        car_rental_value = car_rental(rental_days_wanted)
    elif rental_days_input.lower() == 'no':
        print("Thank you for confirming that you will not need a car.")
        car_rental_value = 0
    else:
        print("Invalid input for car rental preference. Assuming you do not need a car.")
        car_rental_value = 0

    # Calculating total holiday cost
    total_cost = plane_cost_value + hotel_cost_value + car_rental_value
    return total_cost

# Getting user input for destination, nights, and car rental preference
city_flight = input("Where are you flying to? (London, Paris, Barcelona, Berlin) ").lower()

# Validate the city for the flight
if plane_cost(city_flight) == 0:
    print(f"We do not offer flights to {city_flight.capitalize()}. Please try again.")
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
