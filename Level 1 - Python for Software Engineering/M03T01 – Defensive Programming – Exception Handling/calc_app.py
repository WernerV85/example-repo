
def additions_input(num1, num2):
    total_additions = num1 + num2
    return (total_additions)

def subtraction_input(num1, num2):
    total_subtraction = num1 - num2
    return (total_subtraction)

def multiplication_input(num1, num2):
    total_multiplication = num1 * num2
    return (total_multiplication)

def division_input(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero!!!")
    else:
        total_division = num1 / num2
        return (total_division)

calculation_select = {1 : "Addition:",
                       2 : "Subtraction:",
                       3 : "Multiplication:",
                       4 : "Division:",
                       5 : "Print calculations:"}

print("Calculation Option: ")
for key, value in calculation_select.items():
    print(f"{key} : {value}")

function_selection = int(input("Select Calculation you want to perform: "))
print(f"You selected {calculation_select[function_selection]}.")

calculation_1 = ()
with open("Level 1 - Python for Software Engineering\M03T01 – Defensive Programming – Exception Handling\calculation.txt", "a+") as f:
    
    

    while True:
        try:
            if function_selection == 1:
                num1 = int(input("Please enter the first number: "))
                num2 = int(input("Please enter the second number:"))
                addition_total = additions_input(num1, num2)
                print(f"{num1} + {num2} = {addition_total}")
                f.write(f"{num1} + {num2} = {addition_total} \n")
           
            elif function_selection == 2:
                num1 = int(input("Please enter the first number: "))
                num2 = int(input("Please enter the second number:"))
                subtraction_total = subtraction_input(num1, num2)
                print(f"{num1} - {num2} = {subtraction_total}")
                f.write(f"{num1} - {num2} = {subtraction_total} \n")
        
            elif function_selection == 3:
                num1 = int(input("Please enter the first number: "))
                num2 = int(input("Please enter the second number:"))
                multiplication_total = multiplication_input(num1, num2)
                print(f"{num1} * {num2} = {multiplication_total}")
                f.write(f"{num1} * {num2} = {multiplication_total} \n")   
        
            elif function_selection == 4:
                num1 = int(input("Please enter the first number: "))
                num2 = int(input("Please enter the second number:"))
                division_total = division_input(num1, num2)
                print(f"{num1} / {num2} = {division_total}")
                f.write(f"{num1} / {num2} = {division_total} \n") 
        
            elif function_selection == 5:
                with open("Level 1 - Python for Software Engineering\M03T01 – Defensive Programming – Exception Handling\calculation.txt", "r") as file:
                    previous_cals = file.read()
                print(f"Your previous calculation results: \n{previous_cals}")
            break

        except ValueError:
            print("Please supply correct option.")
