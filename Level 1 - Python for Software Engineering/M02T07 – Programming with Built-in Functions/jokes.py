## Auto grade task 2 - M02T07

# Import built in function random
import random

# Create dictionairy of joke to randomise
# Couldn't think of any joke, so pulled some jokes off internet
# References listed below:
#  https://www.rd.com/list/short-jokes/
#  https://parade.com/1287449/marynliles/short-jokes/

joke_list = ['''What do you call a magic dog?
             
        A Labracadabrador!!!''',
             '''What's ornage and sounds like a carrot?
             
        A Parrot!!!''',
             '''What do you call a woman with one leg?
             
        Eileen!!!''',
             '''Why did the frog take the bus to work today?
             
        His car got toad away!!!''',
             '''What did the buffalo say when his son left for college?
             
        Bison!!!''',
             '''Why do French people eat snails?
             
        They don't like fast food!!!''',
             '''Why did the golfer wear two pairs of pants?
             
        Just in case he got a hole in one!!!''',
             '''Why don't the circus lions eat the clowns?
             
        Because they tast funny!!!''',
             '''What is fast, loud and crunchy?
             
        A Rocket chip!!!''',
             '''What's the smartest insect?
             
        A spelling Bee!!!''',
            '''Why did the teddy bear say no to dessert?
            
        Becasue he was stuffed!!!''']



# Created a joke output variable to print
# Assigned random choice function to select joke form dictionairy
joke_output = random.choice(joke_list)

# Printing Joke!!!
print(f'''The random joke for today is: 
      
{joke_output}''')