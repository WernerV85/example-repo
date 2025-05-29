## Auto Grade task 2 - Data Structures - Lists and Dictionaries

print('''Auto grade task 2
      
      
      ''')

# Create meny list
# Convert list to dictionary for calculations
menu = [(1, "Apples") , (2, "Pears") , (3, "Lemons") , (4, "Strawberries")]
menu_dict = dict(menu)

# Create Dictionaries for stock and Price of items
stock = {1: 10,
         2: 5,
         3: 2,
         4: 8}
price = {1: 5.25,
         2: 4.00,
         3: 2.99,
         4: 1.85}

#Creating empty dictionary to store calculated values
item_value = {}

# For loop to calculate stock value for each item in the menu
i = 0

for i in menu_dict:
    item_value[i] = (stock[i] * price[i])
    i += 1
    items = menu_dict.values()
    stock_price = item_value.values()

# Printing results
print(menu)
print(item_value)
