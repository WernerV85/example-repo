## Auto grade task - 1
print(f'''Auto-graded task 1
      
      
      ''')

# Calculate average of user input number

# Define variables
num_input = 1
num_count = 0
num_total = 0

# While loop that request user input as well as checking
# vadility of the inputs
while num_input >= 1:
    num_input = int(input(f"Please give any number: "))
    num_total += num_input
    num_count +=1

    #if num_input == 0:
     #   print(f"Invalid input!!")

    if num_input <= 0:
        num_total == 1
        num_count -= 1
        print(f"The sum of the values are: {num_total}")
        print(f"The count of the values you've entered is: {num_count}")
        num_ave = num_total / num_count
        print(f"Average of the numbers entered is: {num_ave}")



    