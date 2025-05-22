# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") 
#Syntax error - No parentheses
print ("\n") 
#Syntax error - incorrect indentation

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" 
#Syntax error - incorrect indentation also incorrect usage of ==
age = int(age_Str) 
#Syntax error - incorrect indentation
print(f"I'm {age} years old.")  
#Syntax error - incorrect indentation also incorrect usage of f print

    # Variables declaring additional years and printing the total years of age
years_from_now = 3.5  
#Syntax error - incorrect indentation Logical error - variable set incorrectly as str
total_years = age + years_from_now  
#Syntax error - incorrect indentation

print (f"The total number of years: {total_years}")  
#Syntax error - No parentheses , Wrong "" and incorrect variable

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = int(total_years * 12) 
#Logical error, spelling mistake
print (f"In 3 years and 6 months, I'll be {total_months} months old")  
#Syntax error - No parentheses #Syntax error - incorrect indentation also incorrect usage of f print

#HINT, 330 months is the correct answer

