# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])
        # k value is not an argument, should be key

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", 
                         # Incorrect use of ' ; changed to ""
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, keys = {"lisa", "bart", "homer"})

# Two bugs:
    # 1 - Function second argument was not correctly defined, missing 
    # argument "keys="
    # 2 - missing {} brackets to call keys in dictionary
'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

