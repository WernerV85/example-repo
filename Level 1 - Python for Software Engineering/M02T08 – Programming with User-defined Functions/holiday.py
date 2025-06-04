##  Practical task - M02T08 
## Programming with user-defined Functions

## Task = Take user input to calculate holiday cost

# Create dictionary with selection of destinations
cities_select = {1 : "Johannesburg",
                 2 : "Cape Town",
                 3 : "Bloemfontein",
                 4 : "KwaZulu Natal"}


# Printing destination Dictionary for user to see option
print("Destination List")
for key, value in cities_select.items():
   print(f"{key}: {value}")


# Requesting user input to select destination
# Informing user to only use number assigned value
city_flight = int(input(f'''Please select you destination. 
Insert the corresponding number: '''))


# Requesting user input to input number of days staying in destination
num_nights = int(input(f'''How many nights are you staying in 
{cities_select[city_flight]}: '''))


# Decided to request user input if rental car is needed
# Convert input to upper to ease if statement
# Embedded if statement to either ask for number of days if Y
# Or return rental days 0 and print statement if N was selected
rental_car = str(input(f"Will you be needing a rental car (Y/N):"))
rental_car = rental_car.upper()
if rental_car == "Y":
    rental_days = int(input(f'''
Number of days car rental required: '''))
elif rental_car == "N":
    rental_days = 0
    

# Creating Functions:
def hotel_cost(num_nights, cost = 1500.00):
    """
    Calculate hotel cost:

        Parameters: 
        num_nights: integer value from user input
        cost set to 1500 for all destination

        Returns:
        Float: cost of night
    """
    hotel_cost_total = num_nights * cost
    return float(hotel_cost_total)


def plane_cost(city_flight, flight_price):
    """
    Cost for flights:

        Parameters:
        Destination taken from user input form destination list
        Flight price: Value set out in if statement,
                        different for each destination

        Returns:
        Value set out in if statement per destination.
    """
    if city_flight == 1:
        flight_price = 2500
    elif city_flight == 2:
        flight_price = 4800
    elif city_flight == 3:
        flight_price = 1900
    elif city_flight == 4:
        flight_price = 3450
    return(float(flight_price))


def car_rental(rental_days = 1, rental_cost = 530.50):
    """
    Calculate cost for car rental:

        Parameters:
        Rental days: set to 1 for if rental car is not selected,
        Uses number of days inputted by user if rental car is selected
        Rental cost: Standard value used for all destination

        Returns:
        Float value: Rental cost total
    """
    if rental_car == "Y":
        car_rental_total = rental_days * rental_cost
    elif rental_car == "N":
        car_rental_total = rental_days * 1
    return(float(car_rental_total))
    

def holiday_cost(num_nights, city_flight, rental_day):
    """
    Calculate total of holiday:

        Parameters:
        Hotel cost: user defined function
        Plane cost: user defined function
        Car rental: user defined function

        Returns:
        Sum of all total values calculated in defined functions.
    """
    total_holiday_cost = hotel_cost(num_nights) + plane_cost(cities_select, flight_cost) + car_rental(rental_days)
    return(float(total_holiday_cost))

# Printing calculated values of user inputs
hotel_stay = hotel_cost(num_nights)
print(f'''
Your hotel cost for {num_nights} nights: 
    R {hotel_stay:,}0''')

flight_cost = float(plane_cost(city_flight, flight_price = 0))
print(f'''
Your flight to {cities_select[city_flight]} will cost: 
    R {flight_cost:,}0 (one-way).''')

car_rental_cost = car_rental(rental_days)
if rental_car == "Y":
    print(f'''
To rent a car for {rental_days} days will cost: 
    R {car_rental_cost:,}0''')
else:
    print('''
Rental car was not selected''')

holiday_total_cost = holiday_cost(num_nights, city_flight, rental_days)
print(f'''
Total cost for {num_nights} days in {cities_select[city_flight]}:
    R {holiday_total_cost:,}0''')      
