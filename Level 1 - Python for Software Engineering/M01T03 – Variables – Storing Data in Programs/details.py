#Auto-graded task 1

#request input from user:
#first input = Name
user_name = str(input("Please give your full name: "))

#second input = age
user_age = int(input("How old are you: "))

#third input = house number
user_house_num = int(input("What is the house number you stay in: "))

#fourth input = Street name
user_street_name = str(input("What street do you stay on: "))

#print output using f-string
print(f"This is {user_name}. He is {user_age} years old and he lives at house number {user_house_num} on {user_street_name}.")