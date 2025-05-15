import math

print('''Investment - to calculate the amount on interest you'll earn on your investment
Bond       - to calcuate the amount you'll have to pay on a home loan. 
      ''')
user_choice = str(input('''Enter either "Investment" or "Bond" form the menu above to proceed: '''))

user_choice = user_choice.upper()

if user_choice == "INVESTMENT":
    dep_amount = float(input("Please supply the amount of money being deposited: "))
    interest_rate = float(input('''What is the interest rate (percentage) at which the money is being deposited 
    (please only give the value, exclude the % symbol): '''))
    interest_percen = interest_rate / 100
    invest_year = int(input("How many years do you want to invest your money: "))
    interest = str(input('''Are you investing the money to earn simple or compounded interest?
    Please enter either "Simple" or "Compound" for calculation to start: '''))
    
    interest = interest.upper()

    if interest == "SIMPLE":
        calculate_simple = dep_amount * (1 + interest_percen * invest_year)
        calculate_simple = round(calculate_simple,2)
        print(f"The interest you will earn over {invest_year} years is equal to {calculate_simple}!")
    elif interest == "COMPOUND":
        calculate_compound = dep_amount * math.pow((1 + interest_percen), invest_year)
        calculate_compound = round(calculate_compound,2)
        print(f"The interest you will earn over {invest_year} years is equal to {calculate_compound}!")
    else :
        print("Incorrect selection!! Please return to Main Menu!!")

elif user_choice == "BOND":
    house_value = float(input("What is the value of the house: "))
    house_interest_rate = float(input('''What is the interest rate (percentage) of the bond
    (please only give the value, exclude the % symbol): '''))
    house_month_interest = (house_interest_rate / 100) / 12
    num_months = int(input('''Bond period - Months
    (In how many months will the bond be paid off?): '''))

    monthly_repay = (house_month_interest * house_value) / (1 - (1 + house_month_interest) ** (-num_months))
    round(monthly_repay,2)
    print(f"The monthly Bond repayment is equal to {monthly_repay}!")

else :
    print("Incorrect selection!! Please return to Main Menu!!")

   
    

    
