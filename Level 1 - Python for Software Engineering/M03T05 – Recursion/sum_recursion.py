''' Auto grade task 1: Sum list of number to index using recursion.'''

# Define list of numbers to sum.
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Define input from user for index number to use as sum limit.
index_number = int(input('Please give a number between 1 and 9: '))
# Minus 1 to correct the index number as list start from 0.
correct_index = index_number - 1

# Define Function that will sum the numbers
def sum_indexes(list_numbers, correct_index):
    # Base case that will return 1 if the first index is used.
    if correct_index == 0:
        return 1
    # Else statement to calculate the sum if the first index was not used.
    else:
        return list_numbers[correct_index] + sum_indexes(list_numbers, correct_index - 1)

# Call the function.
sum_indexes = sum_indexes(list_numbers, correct_index)

# Printing the result.
print(f'The sum of the numbers in the list to the index {correct_index} is equal to {sum_indexes}')

