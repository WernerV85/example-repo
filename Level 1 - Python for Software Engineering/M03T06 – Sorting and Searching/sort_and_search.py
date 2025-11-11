
# University of Cape Town. (2014). Sorting, Searching and Algorithm Analysis – Object-Oriented Programming in Python 1 documentation. 
# Retrieved 25 February 2020, from https://python-textbok.readthedocs.io/en/1.0/Sorting_and_Searching_Algorithms.html
# 03 -013 Sorting and Searching, p 26-27

def binary_search(target, items):
    low, high = 0, len(items) - 1

    # Keep iterating until the low and high cross 
    while high >= low: 
        # Find midpoint
        mid = (low + high) // 2 
        
        # If item is found at midpoint, return its index 
        if items[mid] == target: 
            return mid 
        # Else, if item at midpoint is less than target, 
        # # search the second half of the list 
        elif items[mid] < target: 
            low = mid + 1 
            # Else, search the first half 
        else: 
            high = mid - 1 
            # Returns None if item not found 
    return None



# I believe the Binary search is the best option, as the list will first be sorted low to high,
# with this it will be easy to implement the binary search,
# as it will be easy to find the mid point and search from there with the negatives included

# Define and create list as specified in the task
sort_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Call the function and printing the results
new_list = sorted(sort_list)
print(f''' The sorted list, using Binary sort:
{new_list}''')

# Defining the requested number to be found
item_to_find = 9

# Calling the function and printing the results
found_item = binary_search(item_to_find, new_list)
if found_item is not None: 
    print(f"\n Item {item_to_find} found at index {found_item}.") 
else: 
    print(f"\n Item {item_to_find} not found in the list.")

## https://www.geeksforgeeks.org/python/python-program-for-insertion-sort/
## @GeeksforGeeks, Sanchhaya Education Private Limited, All rights reserved
## Insertion Sort

# Defining the function for insertion sort
def insertion_sort(sorted_list):
    # Calculating the length of the list to be sorted
    len_list = len(sorted_list)

    # For loop to run through the list
    for num1 in range(1, len_list):
        sort_num = sorted_list[num1]
        sort_num1 = num1 - 1
        # while loop to sort the number in order from smallest to largest
        while sort_num1 >= 0 and sort_num < sorted_list[sort_num1]:
            sorted_list[sort_num1 + 1] = sorted_list[sort_num1]
            sort_num1 -= 1
        sorted_list[sort_num1 + 1] = sort_num

# Calling the function and printing the result
insertion_sort(sort_list)
print(f''' \n The sorted list, using insertion sort:
{sort_list}''')

# University of Cape Town. (2014). Sorting, Searching and Algorithm Analysis – Object-Oriented Programming in Python 1 documentation. 
# Retrieved 25 February 2020, from https://python-textbok.readthedocs.io/en/1.0/Sorting_and_Searching_Algorithms.html
# 03 -013 Sorting and Searching, p 25
## Sequential Sort

def sequential_search(target, items):
    # Iterate over the list. If we find the target item, return its index. 
    for index in range(len(items)): 
        if items[index] == target: 
            return index 
        # If the target item is not found, return None. 
    return None  

# Calling the function and printing the result
found_item = sequential_search(item_to_find, new_list)
if found_item is not None: 
    print(f"\n Item {item_to_find} found at index {found_item}.") 
else: 
    print(f"\n Item {item_to_find} not found in the list.")


