#** Capstone Project 1: Finance calculator**

#import Python math module as instructed
import math

#Text displayed as instructed
print('''Investment - to calculate the amount on interest you'll earn on your investment
Bond       - to calcuate the amount you'll have to pay on a home loan. ''')

#Define first variable user choice to select what calculation they want to calculate.
user_choice = str(input('''Enter either "Investment" or "Bond" form the menu above to proceed: '''))

#This part was tricky, my first thought was to populate a list with all the different types the user may input
#As I work for a software company, I had a chat regarding this assignment with one of our developers
#I told him about my initial plans, and he suggested the conversion to uppercase
#I took the day and thought this over and decided to use his suggestion
#As he only gave me the suggestion I am not going to reference him as he did not help me with the code, only the idea and it was verbal
user_choice = user_choice.upper()

#If statement start for if user select Investment
if user_choice == "INVESTMENT":

    #Request all inputs from user
    dep_amount = float(input("Please supply the amount of money being deposited (H$): "))

    interest_rate = float(input('''What is the interest rate (percentage) at which the money is being deposited 
    (please only give the value, exclude the % symbol): '''))

    #Converting the investement rate to show as a float and not percentage
    interest_percen = interest_rate / 100

    invest_year = int(input("How many years do you want to invest your money: "))

    #user input on weather they need simple or compound interest calculation
    interest = str(input('''Are you investing the money to earn simple or compounded interest?
    Please enter either "Simple" or "Compound" for calculation to start: '''))
    
    #Start of the inbedded if statement for the last input of simple or compound interest
    #Used the same thought as for investment or bond here to ease the way of identifying user input
    interest = interest.upper()

    #If statement to calculate Simple investment interest
    if interest == "SIMPLE":
        calculate_simple = dep_amount * (1 + interest_percen * invest_year)
        #Used the rounding function to show final result as 2 decimals or cents
        #Hyoerion 10-006 The String and Numerical Data Types, page 10
        calculate_simple = round(calculate_simple,2)
        print(f"The interest you will earn over {invest_year} years is equal to H$ {calculate_simple:,}!")
    elif interest == "COMPOUND":
        calculate_compound = dep_amount * math.pow((1 + interest_percen), invest_year)
        calculate_compound = round(calculate_compound,2)
        print(f"The interest you will earn over {invest_year} years is equal to H$ {calculate_compound:,}!")
    else :
        print("Incorrect selection!! Please return to Main Menu!!")

elif user_choice == "BOND":
    house_value = float(input("What is the value of the house (H$): "))
    house_interest_rate = float(input('''What is the interest rate (percentage) of the bond
    (please only give the value, exclude the % symbol): '''))
    house_month_interest = (house_interest_rate / 100) / 12
    num_months = int(input('''Bond period - Months
    (In how many months will the bond be paid off?): '''))

    monthly_repay = (house_month_interest * house_value) / (1 - (1 + house_month_interest) ** (-num_months))
    monthly_repay = round(monthly_repay,2)
    print(f"The monthly Bond repayment is equal to H$ {monthly_repay:,}!")

else :
    print("Incorrect selection!! Please return to Main Menu!!")

   
    

    
