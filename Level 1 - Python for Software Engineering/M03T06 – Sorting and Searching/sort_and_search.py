
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

sort_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

new_list = sorted(sort_list)
print(new_list)


item_to_find = 9
result = binary_search(item_to_find, new_list)
if result is not None: 
    print(f"Item {item_to_find} found at index {result}.") 
else: 
    print(f"Item {item_to_find} not found in the list.")



## Sequential Sort

def sequential_search(target, items):
    # Iterate over the list. If we find the target item, return its index. 
    for index in range(len(items)): 
        if items[index] == target: 
            return index 
        # If the target item is not found, return None. 
    return None  

result = sequential_search(item_to_find, new_list)
if result is not None: 
    print(f"Item {item_to_find} found at index {result}.") 
else: 
    print(f"Item {item_to_find} not found in the list.")


