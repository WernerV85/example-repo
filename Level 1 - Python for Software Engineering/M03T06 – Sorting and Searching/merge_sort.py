# Copying text from 03-013 Sorting and Searching - Merge Sort
# https://www.codecademy.com/paths/software-engineer-career-path/tracks/se-30-03-data-structures-algorithms/modules/m03t06-sorting-and-searching/cheatsheets/03-013-sorting-and-searching-merge-sort
# Pages 22 - 24
# As instructed in Task 2 of the document
# sort a list of strings from longest to shortest using merge sort algorithm

def merge_sort(items):
    #get the length of the input list
    items_length = len(items)

    #Create temporary storage for merging
    temporary_storage = [None] * items_length

    # Initialise the size of the subsections to 1
    size_of_subsections = 1

    # Iterate until the size of the subsections is less than the length of the list
    while size_of_subsections < items_length:
        # Iterate over the list in steps of size_of_subsections *2
        for i in range(0, items_length, size_of_subsections * 2):
            # Determine the start and end indices of the two subsections 
            # to merge
            first_section_start, first_section_end = i, min(
                i + size_of_subsections, items_length
            )

            second_section_start, second_section_end = first_section_end, min(
                first_section_end + size_of_subsections, items_length
            )

            # Define the section to merge
            sections = (first_section_start, first_section_end), (
                second_section_start,
                second_section_end,
            )

            # Call the merge function to merge the subsections
            merge(items, sections, temporary_storage)
    
        # Double the size of subsections for the next iteration
        size_of_subsections *= 2
    
    # Return the sorted list
    return(items)

def merge(items, sections, temporary_storage):
    # Unpack the sections tuple to get the start and end indices
    # of each section.
    (first_section_start, first_section_end), (
        second_section_start, 
        second_section_end) = sections
    
    # Initialise indices for the two section and temporary storage
    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0

    # Loop until both section have been fully merged
    while left_index < first_section_end or right_index < second_section_end:
        # Check if both sections still have elements to compare
        if left_index < first_section_end and right_index < second_section_end:
            # Compare elements from both sections
            if items[left_index] < items[right_index]:
                # Place the smaller element into temporary storage
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
            else: # items[right_index] <= items[left_index]
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
            temp_index += 1

        # If section 1 still has elements left to merge
        elif left_index < first_section_end:
            # Copy remaining elements from section 1 to temporary storage
            for i in range(left_index, first_section_end):
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
                temp_index += 1

        # If section 2 still has elements left to merge
        else: # right_index , second_section_end  
            # Copy remaining elements from section 2 to temporary storage
            for i in range(right_index, second_section_end):
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
                temp_index += 1

    # Copy sorted elements from temporary storage back to the original list
    for i in range(temp_index):
        items[first_section_start + i] = temporary_storage[i]

example_list = ['Hi', 'Hello', 'Hey', 'Hola', 'Bonjour', 'Ciao', 'Namaste', 'Salaam', 'Konnichiwa', 'Zdravstvuyte']
word_length = [(word, len(word)) for word in example_list]
new_list = []
new_words = []
for word, length in word_length:
    new_list.append(length)
    sorted_list = merge_sort(new_list) 
    length == new_list
    new_words.append(word_length)
            
print(new_words)
print("Sorted List:", sorted_list[::-1])

#example_list2 = ['apple', 'orange', 'banana', 'grape', 'kiwi', 'mango', 'peach', 'pear', 'plum', 'cherry']
#sorted_list2 = merge_sort(example_list2)
#print("Sorted List 2:", sorted_list2[::-1])

#example_list3 = ['dog', 'cat', 'elephant', 'ant', 'zebra', 'lion', 'tiger', 'bear', 'giraffe', 'monkey']
#sorted_list3 = merge_sort(example_list3)
#print("Sorted List 3:", sorted_list3)

example_list4 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_list4 = merge_sort(example_list4)
print("Sorted List:", sorted_list4[::-1])

 
