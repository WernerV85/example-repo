import math

print('''Investment - to calculate the amount on interest you'll earn on your investment
Bond       - to calcuate the amount you'll have to pay on a home loan. 
      ''')
user_choice = str(input('''Enter either "Investment" or "Bond" form the menu above to proceed: '''))

user_choice = user_choice.upper()

if user_choice == "INVESTMENT":
    dep_amount = float(input("Please supply the amount of money being deposited: "))
    interest_rate = float(input('''What is the interest rate (percentage) at which the money is being deposited 
    (please only give the number, exclude the % symbol): '''))
    invest_year = int(input("How many years do you want to invest your money: "))
    interest = str(input('''Are you investing the money to earn simple or compounded interest?
    Please enter either "Simple" or "Compound" for calculation to start: '''))
    
    interest = interest.upper()

    if interest == "SIMPLE":
        interest_percen = interest_rate / 100
        calculate_simple = dep_amount * (1 + interest_percen * invest_year)
        print(f"The interest you will earn over {invest_year} will be equal to {calculate_simple}")
    
