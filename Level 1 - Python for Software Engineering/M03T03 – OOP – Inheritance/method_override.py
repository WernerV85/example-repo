''' Task 2
    Method override task'''

# Creating main class Adult 
# Assigning attributes to class
class Adult():
    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

# Defining method to populate if input user can drive
    def can_drive(self):
        print(self.name, ", is old enough to drive.")


# Creating new class Child
# Using Super() to initialise that Child has the same attributes as Adult class
class Child(Adult):
    def __init__(self, name, age, eye_color, hair_color):
        super().__init__(name, age, eye_color, hair_color)
  
# Creating method to override Adult can drive method
    def can_drive(self):
        print(self.name, ", is NOT old enough to drive!!")

# Creating input form for user to input information
user_input = Adult(
    name = str(input(f'Please give you Name: ')),
    age = int(input('How old are you: ')),
    eye_color = str(input(f'What is your eye color: ')),
    hair_color = str(input(f'What is the color of you hair: '))
)

# Creating logical test to determine what method to call from correct Class
# Printing the methods if logic test is true.
if user_input.age >= 18:
    user_input = Adult(user_input.name,
                        user_input.age, 
                        user_input.eye_color,
                        user_input.hair_color)
    user_input.can_drive()
elif user_input.age < 18:
    user_input = Child(user_input.name,
                        user_input.age, 
                        user_input.eye_color,
                        user_input.hair_color)
    user_input.can_drive()

