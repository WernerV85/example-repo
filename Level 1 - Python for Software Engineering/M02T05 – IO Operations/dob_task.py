name_list = []
date_list = []

print("Name: ")

with open('Level 1 - Python for Software Engineering\M02T05 – IO Operations\Code Files\Input\Task file\DOB.txt', 'r') as file:
    for lines in file:
        name_list = lines.split(" ")
        name_list = " ".join(name_list[:2])
        print(name_list)

print('''
      
Birthdate: ''')   

with open('Level 1 - Python for Software Engineering\M02T05 – IO Operations\Code Files\Input\Task file\DOB.txt', 'r') as file:
    for lines in file:
        date_list = lines.split(" ")
        date_list = " ".join(date_list[2:])
        print(date_list)