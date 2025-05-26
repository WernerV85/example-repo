## --- Auto-graded task - M02T04

print('''
      Auto-graded task: M02T04
      part 1:
      
          ''')

# Define variables
user_input = str(input("Please type any sentence: "))
i = 0
input_len = int(len(user_input))

# Define empty string
altenate_text = ""

# While loop to check for alternating letter using if index number devided
# by 2 - 0 then is should be upper case
while i < input_len:
    if i % 2 == 0:
        altenate_text += str(user_input[i].upper())
    else: 
        altenate_text += str(user_input[i].lower())
    i += 1   

# Printing previous empty string
print(f"Here follows the input text: {altenate_text} .")

## Part 2:

print(''' 
      
    Auto-graded task: M02T04
    part 2:
      
      ''')

#Define Lists
upper_split = []

# Defining new list with join function for printing
new_upper = " ".join(upper_split)

# Splitting input sentence into individual words.
upper_split = user_input.split(' ')

# Setup variables for while loop and calculate count of items in list
j = 0
list_items = int(len(upper_split))

#While loop to calculate which words needs to be upper case
while j < list_items:
    if j % 2 == 0:
       new_upper += upper_split[j].lower() + " "
    else:
        new_upper += upper_split[j].upper() + " "
    j += 1

# Printing list 
print(new_upper)

