
#========The beginning of the class==========
## Defining Class shoe
class Shoe:

    ## Initializing attributes for the class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass
        
    def get_cost(self):
        # open file inventory.txt
        # read the cost data from the file associated the product name
        # append the cost data into the shoe_cost list
        # return the cost of the shoe 

        shoe_cost = []

        with open('Level 1 - Python for Software Engineering\\M03T07 – OOP – Synthesis\\Code Files\\inventory.txt', 'r+', encoding='utf-8') as inventory_file:
            for product, cost in inventory_file:
                product, cost = inventory_file.readline().split(',')
                product, cost = product.strip(), cost.strip()
                print(product, cost)
                shoe_cost.append(product, cost)
                print(shoe_cost)
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        # open file inventory.txt
        # read the quantity data from the file associated the product name 
        # append the quantity data into the shoe_qnt list
        # return the quantity of the shoe
        # print(shoe_quantity) for debugging purpose
        shoe_qnt = []

        with open('Level 1 - Python for Software Engineering\\M03T07 – OOP – Synthesis\\Code Files\\inventory.txt', 'r+', encoding='utf-8') as inventory_file:
            for product, quantity in inventory_file:
                print(product, quantity)
                shoe_qnt.append(product, quantity)
                print(shoe_qnt)
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        # return a string representation of the shoe object
        # print for debugging purpose
            print(f"Shoe(country={self.country}, code={self.code}, product={self.product}, cost={self.cost}, quantity={self.quantity})")

    pass
    '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    # open file inventory.txt
    # read data from this file
    # create a shoes object with this data
    # append this object into the shoes list  
    # use try-except for error handling
    # skip the first line using your code
    with open('Level 1 - Python for Software Engineering\\M03T07 – OOP – Synthesis\\Code Files\\inventory.txt', 'r+', encoding='utf-8') as inventory_file:
        next(inventory_file)  # Skip the header line
        for line in inventory_file:
            try:
                country, code, product, cost, quantity = line.strip().split(',')
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
            except ValueError as e:
                print(f"Error processing line: {line.strip()}. Error: {e}")
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def capture_shoes():
    # Ask user for input new details on shoe
    # create a new shoe object with this data
    # append this object inside the shoe list
    # append to txt file inventory.txt
    country = input("Enter the country: ") 
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    with open('Level 1 - Python for Software Engineering\\M03T07 – OOP – Synthesis\\Code Files\\inventory.txt', 'a', encoding='utf-8') as inventory_file:
        inventory_file.write(f"\n{country},{code},{product},{cost},{quantity}")
    print(shoe_list)    
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    # Iterate over the shoes list and print the details of the shoes
    # return data using tabulate module
    
    from tabulate import tabulate

    table = []
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    for shoe in shoe_list:
        table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    print(tabulate(table, headers, tablegrid="grid"))
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    # Identify the shoe object with the lowest quantity
    # Ask the user if they want to add this quantity of shoes and then update it
    # This quantity should be updated on the file for this shoe
    # Update the shoe object in the shoe list as well
    for shoe in shoe_list:
        if shoe.quantity == min(shoe.quantity for shoe in shoe_list):
            print(f"Shoe with lowest quantity: {shoe}")
            add_quantity = int(input("Do you want to add more quantity? Enter the amount to add: "))
            shoe.quantity += add_quantity
            print(f"Updated quantity for {shoe.product}: {shoe.quantity}")

            # Update the inventory.txt file with user input quantity
            with open('Level 1 - Python for Software Engineering\\M03T07 – OOP – Synthesis\\Code Files\\inventory.txt', 'r+', encoding='utf-8') as inventory_file:
                lines = inventory_file.readlines()
                inventory_file.seek(0)
                for line in lines:
                    if shoe.code in line:
                        parts = line.strip().split(',')
                        parts[4] = str(shoe.quantity)  # Update quantity
                        inventory_file.write(','.join(parts) + '\n')
                    else:
                        inventory_file.write(line)
                inventory_file.truncate()
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe():
    # ask user what they want to search, code or product
    # search for the shoe from the list using the code or product
    search_option = input('''Do you want to search by code or product? 
    1 = code:
    2 = product: ''')
    if search_option == '1':
        code = input("Enter the shoe code to search: ")
        code2 = code.upper()
        for shoe in shoe_list:
            if shoe.code == code2:
                print(shoe)
                return
        print("Shoe with this code not found.")
    elif search_option == '2':
        product = input("Enter the shoe product to search: ")
        product2 = product.lower()
        for shoe in shoe_list:
            if shoe.product.lower() == product2():
                print(shoe)
                return
        print("Shoe with this product not found.")
    else:
        print("Invalid option selected.")
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    # Iterate over the shoes list and calculate the total value for each item
    # Print this information on the console for all the shoes
    for shoe in shoe_list:
        total_value = shoe.cost() * shoe.quantity()
        print(f"Total value for {shoe.product} (Code: {shoe.code}): {total_value}")
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    # Calculate the shoe with the highest quantity
    # Print this shoe as being for sale
    highest_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"Shoe with highest quantity for sale: {highest_shoe}")
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
# Creating a menu that executes each function above.
read_shoes_data()
while True:
    print('''
    Shoe Inventory Management System
    1. Capture Shoes
    2. View All Shoes
    3. Re-stock Shoes
    4. Search Shoe
    5. Calculate Value per Item
    6. Show Highest Quantity Shoe
    7. Exit
    ''')
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        capture_shoes()
    elif choice == '2':
        view_all()
    elif choice == '3':
        re_stock()
    elif choice == '4':
        search_shoe()
    elif choice == '5':
        value_per_item()
    elif choice == '6':
        highest_qty()
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''