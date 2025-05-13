#******Auto grade 3*****

#define 3 variables and requesting input from the user for all three numbers.
num1 = int(input("Please supply the first of three numbers: "))
num2 = int(input("Please supply the second of three numbers: "))
num3 = int(input("Please give the third and last of the three numbers: "))

#printing the three numbers input from the user
print(f"The number you selected are {num1} , {num2} and {num3} .")

#define the function of the sum of all three numbers, and printing the result
cal1 = num1 + num2 + num3
print(f"The sum of all three numbers is equal to {cal1}.")

#Define the second function of subtracting the second number from the first number and printing the result.
cal2 = num1 - num2
print(f"The difference between the first number and second number is equal to {cal2}.")

#Define the third function that multiplies the first and third numbers and printing the result.
cal3 = num3 * num1
print(f"Multiplying the third number and first number will equal {cal3}.")

#defining the last function of deviding the sum of the three numbers by the third number and printing the result.
cal4 = cal1 / num3
print(f"Deviding the sum of all three number by the third number equals {float(cal4)}.")