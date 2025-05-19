#** Capstone Project 1: Finance calculator**

#import Python math module as instructed
import math

#Text displayed as instructed
print('''Investment - to calculate the amount on interest you'll earn on your investment
Bond       - to calcuate the amount you'll have to pay on a home loan. ''')

#Define first variable user choice to select what calculation they want to calculate.
user_choice = str(input('''Enter either "Investment" or "Bond" form the menu above to proceed: '''))

    ##This part was tricky, my first thought was to populate a list with all the different types the user may input
    ##As I work for a software company, I had a chat regarding this assignment with one of our developers
    ##I told him about my initial plans, and he suggested the conversion to uppercase
    ##I took the day and thought this over and decided to use his suggestion
    ##As he only gave me the suggestion I am not going to reference him as he did not help me with the code, only the idea and it was verbal
user_choice = user_choice.upper()

#If statement start for if user select Investment
if user_choice == "INVESTMENT":

    #Request all inputs from user as instructed
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

        #used calculation as setout in the reading material
            ##HyperionDev, M01T07 – Capstone Project – Variables and Control Structures, page 3, copyright 2025 HyperionDev
        calculate_simple = dep_amount * (1 + interest_percen * invest_year)
        
        #Used the rounding function to show final result as 2 decimals or cents
            #HyperionDev, 10-006 The String and Numerical Data Types, page 10, copyright 2025 HyperionDev
        calculate_simple = round(calculate_simple, 2)

        #print text to inform user of how much interst will be earned, used H$ as in example in Capstone reading material
            ##HyperionDev, M01T07 – Capstone Project – Variables and Control Structures, page 3, copyright 2025 HyperionDev
        #Thousand seperator was used to make the reading of the value even more user friendly, got the syntax from W3school website
            ##https://www.w3schools.com/python/python_operators.asp, W3Schools - WE.CSS. , copyright 1999 - 2025 by Refsnes Data
        print(f"The interest you will earn over {invest_year} years is equal to H$ {calculate_simple:,}!")

    #second part (elif) to calculate the compound interest
    elif interest == "COMPOUND":

        #used calculation as setout in the reading material
            ##HyperionDev, M01T07 – Capstone Project – Variables and Control Structures, page 3, copyright 2025 HyperionDev
        calculate_compound = dep_amount * math.pow((1 + interest_percen), invest_year)

        #Used the rounding function to show final result as 2 decimals or cents
            ##HyperionDev, 10-006 The String and Numerical Data Types, page 10, copyright 2025 HyperionDev
        calculate_compound = round(calculate_compound, 2)

        #print text to inform user of how much interst will be earned, used H$ as in example in Capstone reading material
            ##HyperionDev, M01T07 – Capstone Project – Variables and Control Structures, page 3, copyright 2025 HyperionDev
        #Thousand seperator was used to make the reading of the value even more user friendly, got the syntax from W3school website
            ##https://www.w3schools.com/python/python_operators.asp, W3Schools - WE.CSS. , copyright 1999 - 2025 by Refsnes Data
        print(f"The interest you will earn over {invest_year} years is equal to H$ {calculate_compound:,}!")

        #Created a 'end' or else statement if the user entered any other selection as stated in the instruction in line 36
    else :
        print("Incorrect selection!! Please return to Main Menu!!")


#Second part/ elif statement for if bond was selected in the first input in line 11
elif user_choice == "BOND":

    #requested input from user as instructed in reading material
     #used H$ as in example in Capstone reading material
        ##HyperionDev, M01T07 – Capstone Project – Variables and Control Structures, page 3, copyright 2025 HyperionDev
    house_value = float(input("What is the value of the house (H$): "))

    house_interest_rate = float(input('''What is the interest rate (percentage) of the bond
    (please only give the value, exclude the % symbol): '''))
    #calculated the interest rate per month to be used in final calculation
    house_month_interest = (house_interest_rate / 100) / 12

    num_months = int(input('''Bond period - Months
    (In how many months will the bond be paid off?): '''))
    
    #used calculation as setout in the reading material
         ##HyperionDev, M01T07 – Capstone Project – Variables and Control Structures, page 3, copyright 2025 HyperionDev
    monthly_repay = (house_month_interest * house_value) / (1 - (1 + house_month_interest) ** (-num_months))

    #Used the rounding function to show final result as 2 decimals or cents
        ##HyperionDev, 10-006 The String and Numerical Data Types, page 10, copyright 2025 HyperionDev
    monthly_repay = round(monthly_repay,2)

    #print text to inform user of how much the bond repayment per month will be, used H$ as in example in Capstone reading material
        ##HyperionDev, M01T07 – Capstone Project – Variables and Control Structures, page 3, copyright 2025 HyperionDev
    #Thousand seperator was used to make the reading of the value even more user friendly, got the syntax from W3school website
        ##https://www.w3schools.com/python/python_operators.asp, W3Schools - WE.CSS. , copyright 1999 - 2025 by Refsnes Data
    print(f"The monthly Bond repayment is equal to H$ {monthly_repay:,}!")

#Created a 'end' or else statement if the user entered any other selection as stated in the instruction in line 11
else :
    print("Incorrect selection!! Please return to Main Menu!!")

   
    

    
