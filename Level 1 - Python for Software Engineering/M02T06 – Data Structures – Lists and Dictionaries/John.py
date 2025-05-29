## Auto grade task 1 - 10-021 Data Structures - Lists and Dictionairies

print('''Auto graded task 1:
      
      
      ''')

# Define list that will be used in while loop
incorrect_name = []
user_input = []

# Start while loop with incorrect values check
# Included upper to check for case sensitivity
while user_input != "JOHN":
    user_input = str(input("Please give any name: "))
    user_input = user_input.upper()
    incorrect_name.append(user_input)
# When John is inserted removing john from the list
# Print the incorrect values
else: 
    user_input = "JOHN"
    incorrect_name.remove("JOHN")

    print(f"All incorrect name input: {incorrect_name}")
    