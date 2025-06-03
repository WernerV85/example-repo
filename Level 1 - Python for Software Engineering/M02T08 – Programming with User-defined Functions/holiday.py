##  Practical task - M02T08 
## Programming with user-defined Functions

def hotel_cost(num_nights, cost = 1500.00):
    hotel_cost_total = num_nights * cost
    return round(float(hotel_cost_total),3)

def plane_cost(cities_select, flight_rates):
    for item, value in cities_select.items():
        flight_cost = flight_rates[item]
        return (int(flight_cost[value]))
                  
def car_rental(rental_days, rental_cost = 530.50):
    if rental_car == "Y":
        car_rental_total = rental_days * rental_cost
        return(float(car_rental_total))
    
def holiday_cost(num_nights, city_flights, rental_day):
    total_holiday_cost = hotel_cost(num_nights) + plane_cost(cities_select, flight_rates) + car_rental(rental_days)
    return(float(total_holiday_cost))



cities_select = {1: "Johannesburg",
                 2: "Cape Town",
                 3: "Bloemfontein",
                 4: "KwaZulu Natal"}
city_flight = int(input(f'''Please select you destination by typing the corresponding number
{cities_select} : '''))

flight_rates = {1: 2500.00,
               2: 4800.00,
               3: 1900.00,
               4: 3450.00}

num_nights = int(input(f"How many nights are you staying in {cities_select[city_flight]}: "))

rental_car = str(input(f"Will you be needing a rental car (Y/N):"))
rental_car = rental_car.upper()
if rental_car == "Y":
    rental_days = int(input(f"How many days will you be needing a rental car: "))
elif rental_car == "N":
    rental_days = 0
    print(f"No rental car needed!")

hotel_stay = hotel_cost(num_nights)
print(f"Your hotel cost is R {hotel_stay}")

flight_cost = plane_cost(cities_select, flight_rates)
print(f"Your flight with cost R {flight_cost} (one-way).")

car_rental_cost = car_rental(rental_days)
if rental_car == "Y":
    print(f"To rent a car for {rental_days} days will cost R {car_rental_cost}")
else:
    print("Rental car was not selected")

holiday_total_cost = holiday_cost(num_nights, city_flight, rental_days)
print(f'''The cost for your trip to {city_flight} for {num_nights} totals:
      
      R{holiday_total_cost}''')