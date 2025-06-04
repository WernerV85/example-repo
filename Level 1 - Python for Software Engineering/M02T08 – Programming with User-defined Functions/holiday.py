##  Practical task - M02T08 
## Programming with user-defined Functions

def hotel_cost(num_nights, cost = 1500.00):
    hotel_cost_total = num_nights * cost
    return float(hotel_cost_total)

def plane_cost(city_flight, flight_price):
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
    if rental_car == "Y":
        car_rental_total = rental_days * rental_cost
    elif rental_car == "N":
        car_rental_total = rental_days * 1
    return(float(car_rental_total))
    
def holiday_cost(num_nights, city_flight, rental_day):
    total_holiday_cost = hotel_cost(num_nights) + plane_cost(cities_select, flight_cost) + car_rental(rental_days)
    return(float(total_holiday_cost))



cities_select = {1 : "Johannesburg",
                 2 : "Cape Town",
                 3 : "Bloemfontein",
                 4 : "KwaZulu Natal"}
city_flight = int(input(f'''Please select you destination by typing the corresponding number
{cities_select} : '''))
city_flight_ref = cities_select

num_nights = int(input(f"How many nights are you staying in {cities_select[city_flight]}: "))

rental_car = str(input(f"Will you be needing a rental car (Y/N):"))
rental_car = rental_car.upper()
if rental_car == "Y":
    rental_days = int(input(f"How many days will you be needing a rental car: "))
elif rental_car == "N":
    rental_days = 0
    print(f"No Rental car was selected!")

    

hotel_stay = hotel_cost(num_nights)
print(f"Your hotel cost is R {hotel_stay:,}0")


flight_cost = float(plane_cost(city_flight, flight_price = 0))
print(f"Your flight will cost R {flight_cost:,}0 (one-way).")

car_rental_cost = car_rental(rental_days)
if rental_car == "Y":
    print(f"To rent a car for {rental_days} days will cost R {car_rental_cost:,}0")
else:
    print("Rental car was not selected")

holiday_total_cost = holiday_cost(num_nights, city_flight, rental_days)
print(f'''The cost for your trip to {cities_select[city_flight]} for {num_nights} nights totals:
      
                    R {holiday_total_cost:,}0''')