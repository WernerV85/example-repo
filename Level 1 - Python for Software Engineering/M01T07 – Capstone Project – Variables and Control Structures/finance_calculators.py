import math

print('''Investment - to calculate the amount on interest you'll earn on your investment
Bond       - to calcuate the amount you'll have to pay on a home loan. 
      ''')
user_choice = str(input('''Enter either "Investment" or "Bond" form the menu above to proceed: '''))
user_choice = user_choice.upper()
print(user_choice)
if user_choice == "INVESTMENT":
    dep_amount = float(input("Please supply the amount of money being deposited: "))
    interest_rate = float(input('''What is the interest rate (percentage) at which the money is being deposited: 
                                (please only give the number, exclude the % symbol)'''))
    interest = str(input('''Are you investing the money to earn simple or compounded interest?
                         Please enter either "Simple" or "Compound" for calculation to start: '''))
    
