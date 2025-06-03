import statistics

user_input = []
i = 0

while i < 10:
    user_values = float(input("Please give any number (with or without decimal): "))
    user_input.append(user_values)
    i += 1
    
input_maximum = max(user_input)
maximum_index = user_input.index(input_maximum)
print(f"The total sum of all 10 values is equal to: {sum(user_input)}")
print(f"The Maximum value of the 10 inputs is {input_maximum} and it is indexed at {maximum_index}.")
print(f"The Minimum value of the 10 inputs is {min(user_input)} and it is indexed at {user_input.index(min(user_input))}")
mean_input  = statistics.mean(user_input)
print(f"The Mean for the 10 values, rounded to two decimals, is {round(mean_input,2)}.")