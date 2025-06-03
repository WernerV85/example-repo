## Auto graded task 1 - M02T07

# Import built-in function statistics
import statistics

# Create Empty list to store the user input
user_input = []

# Assign 0 to i for the while loop
i = 0

# While loop to append empty list
# Check inputs are less that 10
while i < 10:
    user_values = float(input("Please give any number (with or without decimal): "))
    user_input.append(user_values)
    i += 1

# Printing the total of the values 
print(f"The total sum of all 10 values is equal to: {sum(user_input)}")

# Calculate the Maximum
# Calculate the index of the Maximum
# Printing the result
input_maximum = max(user_input)
maximum_index = user_input.index(input_maximum)
print(f"The Maximum value of the 10 inputs is {input_maximum} and it is indexed at {maximum_index}.")

# Printing the minimum with embedded functions
# Creating an embedded min calculation
# Embedded function for calculating the index of the Minimum value
print(f"The Minimum value of the 10 inputs is {min(user_input)} and it is indexed at {user_input.index(min(user_input))}")

# Calculating the mean of the input
# Printing the result and rounding the value to 2 decimals
mean_input  = statistics.mean(user_input)
print(f"The Mean for the 10 values, rounded to two decimals, is: {round(mean_input,2)}.")

# Calculating the median of the input values
# Printing the result
median_input = statistics.median(user_input)
print(f"The median of the user input values is: {mean_input}")