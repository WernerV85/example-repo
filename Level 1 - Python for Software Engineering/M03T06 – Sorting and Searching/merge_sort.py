# Copying text from 03-013 Sorting and Searching - Merge Sort
# https://www.codecademy.com/paths/software-engineer-career-path/tracks/se-30-03-data-structures-algorithms/modules/m03t06-sorting-and-searching/cheatsheets/03-013-sorting-and-searching-merge-sort
# Pages 22 - 24
# As instructed in Task 2 of the document

def merge_sort(items):
    #get the length of th input list
    items_length = len(items)

    #Create temporary storage for merging
    temporary_storage = [None] * items_length

    # Initialise the size of the subsections to 1
    size_of_subsections= 1

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
            section = (first_section_start, first_section_end), (
                second_section_start,
                second_section_end,
            )

            # Call the merge function to merge the subsections
            merge(items, sections, temporary_storage)
    
        # Double the size of subsections for the next iteration
        size_of_subsection *= 2
    
    # Return the sorted list
    return(items)
        
