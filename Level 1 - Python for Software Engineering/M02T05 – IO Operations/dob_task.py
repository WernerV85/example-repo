## Auto-graded task - 10-039IO Operations

print(''' Auto-graded tast 1
      
      ''')

# Define empty lists to store content
name_list = []
date_list = []

print("Name: ")

# Open file and split the list into individual words
# Create new list to print concatinating first two word in list
with open('Level 1 - Python for Software Engineering\M02T05 – IO Operations\Code Files\Input\Task file\DOB.txt', 'r') as file:
    for lines in file:
        name_list = lines.split(" ")
        name_list = " ".join(name_list[:2])
        print(name_list)

print('''
      
Birthdate: ''')   

# Open file and split list into individual words
# Create new list to print by concatinating the last 3 word
with open('Level 1 - Python for Software Engineering\M02T05 – IO Operations\Code Files\Input\Task file\DOB.txt', 'r') as d_file1:
    for lines in d_file1:
        date_list = lines.split(" ")
        date_list = " ".join(date_list[2:])
        print(date_list)