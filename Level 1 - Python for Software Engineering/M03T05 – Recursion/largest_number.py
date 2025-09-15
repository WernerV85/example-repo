''' Auto grade task 1: Finding the largest number in a list using Recursion.'''

# Define the list of number that will be used to find the largest number.
number_list = [15, 22, 84, 14, 96, 12, 2, 6, 13]

# Define the function that will find the largest number.
def find_largest_num(number_list):
    # Base case that if there is only one number in the list that that will the the largest.
    if len(number_list) == 1:
        return number_list[0]
    # Else statement that will find the largest number.
    else:
        return max(number_list[0], find_largest_num(number_list[1,:]))

# Call the function to find the largest number
largest_number = find_largest_num(number_list)

# Print the result.
print(f'The largest number in the list is equal to {largest_number}')


