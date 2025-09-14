list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index_number = int(input('Please give a number between 0 and 8: '))

def sum_indexes(list_numbers, index_number):
    if index_number == 0:
        return 1
    else:
        return list_numbers[index_number] + sum_indexes(list_numbers, index_number - 1)

sum_indexes = sum_indexes(list_numbers, index_number)

print(f'The sum of the numbers in the list to the index {index_number} is equal to {sum_indexes}')
print(sum(list_numbers[:index_number + 1]))
print(sum_indexes)