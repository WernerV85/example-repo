
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
    
calculation_select = {1 : "Addition",
                       2 : "Subtraction",
                       3 : "Multiplication",
                       4 : "Division"}

print("Calculation Option: ")
for key, value in calculation_select.items():
    print(f"{key} : {value}")
print(int(input("Select Calculation you want to perform: ")))

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number:"))

while True:
    try:
        if calculation_select in (1, 2, 3, 4):
            
            break
    except Exception:
        print("Please supply correct calculation option.")