import os

'''OOP Synthesis - Task Inventory
Algorithm populated to structure Supplied -
Populated function as stated in task document'''

# Inventory calculator using menu to give user information needed.

# ========The beginning of the class==========

# Declare class shoes, with attributes found in inventory.txt


class Shoe:
    # Initializing attributes for the class

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass

    def get_cost(self):
        # create empty list shoe_cost for printing purposes
        # read the cost data from shoe_list[]
        # using the product name as reference
        # append the cost data into the shoe_cost list
        # return the cost of the shoes

        shoe_cost = []
        for shoe in shoe_list:
            if shoe.product == self.product:
                shoe_cost.append(shoe.cost)
                print(shoe_cost)
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        # creating empty list shoe quantity for printing purpose
        # read the quantity data from shoe_list[]
        # using the product name as reference.
        # append the quantity data into the shoe_qnt list
        # return the quantity of the shoes

        shoe_qnt = []
        for shoe in shoe_list:
            if shoe.product == self.product:
                shoe_qnt.append(shoe.quantity)
                print(shoe_qnt)
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        # Returning a string to represent the shoe_list object
        return (f'''\nStock Information:\n
        Country:    {self.country}
        Code:       {self.code}
        Product:    {self.product}
        Cost:       {self.cost}
        Quantity:   {self.quantity}''')
    pass
    '''
        Add a code to returns a string representation of a class.
        '''


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
# Create a global list object to store shoes objects

shoe_list = []


# ==========Functions outside the class==============


def read_shoes_data():
    # Open file inventory.txt
    # Read all lines except the first line
    # Create shoe object with this data
    # Append shoe object into the shoe list
    # Using try-except for error handling
    # Append to shoe_list[]
    #C:\Users\WernerV\Documents\GitHub\WV25050018135\Level 1 - Python for Software Engineering\M03T07 – OOP – Synthesis\Code Files\inventory.txt
    #Level 1 - Python for Software Engineering\M03T07 – OOP – Synthesis\Code Files\inventory.txt

    try:
        with open('./Level 1 - Python for Software Engineering\\M03T07 – OOP – Synthesis\\Code Files\\inventory.txt', 'r', encoding='utf-8') as inventory_file:
            next(inventory_file)  # Skip the header line.
            for line in inventory_file:
                country, code, product, cost, quantity = line.strip().split(',')
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: The file inventory.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    pass


# Defining update function to write back to inventory.txt
def update():
    with open('./Level 1 - Python for Software Engineering\\M03T07 – OOP – Synthesis\\Code Files\\inventory.txt', 'w', encoding='utf-8') as inventory_file:
        inventory_file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            inventory_file.write(f'''
                {shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n
        ''')
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file
    represents
    data to create one object of shoes. You must use the try-except
    in this function
    for error handling. Remember to skip the first line using your code.
    '''


def capture_shoes():
    # Ask user for details on  new shoe to add
    # create a new shoe object with data provided
    # append this object inside the shoe list

    country = input("\nPlease enter the country: ")
    code = input("Please enter the  stock code: ")
    product = input("Enter the product name: ")
    cost = float(input("Enter the item price: "))
    quantity = int(input("Enter the stock quantity: "))
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

# update inventory.txt using update() function

    update()
    print(f"\nNew shoe {product} added to inventory.")

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
        table.append([shoe.country, shoe.code, shoe.product,
                      shoe.cost, shoe.quantity])
    print(tabulate(table, headers, tablefmt="grid"))
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''


def re_stock():
    # Identify the shoe object with the lowest quantity
    # request if user want to add a quantity to shoe
    # Ask the user quantity of shoes and then update it
    # Update the shoe object in the shoe list as well
    for shoe in shoe_list:
        if shoe.quantity == min(shoe.quantity for shoe in shoe_list):
            print(f"\nShoe with lowest quantity: {str(shoe)}")
            first_request = input('''\nDo you want to add more quantity?
        Yes/No: ''')
            if first_request.lower() == 'no':
                print("\n No quantity added.")
                # If option is 'no' return to main menu
            elif first_request.lower() == 'yes':
                add_quantity = int(input("Enter the quantity to add: "))
                shoe.quantity += add_quantity
                print(f"\n{shoe.product} updated with {add_quantity} units.")
                print(f"\nUpdated quantity {shoe.product}: {shoe.quantity}")
                pass
            # Update the inventory.txt file with user input quantity
            update()
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''


def search_shoe():
    # ask user what they want to search, code or product (product Additional)
    # search for the shoe from the list using the code or product
    # returning the search product details
    search_option = input('''\nDo you want to search by code or product?
    1 = Code:
    2 = Product:
    \nPlease enter you choice here: ''')
    if search_option == '1':
        code = input("\nEnter the shoe code to search: ")
        code2 = code.upper()
        for shoe in shoe_list:
            if shoe.code == code2:
                print(str(shoe))
                return
        print(f"Shoe code {shoe.code} not found.")
    elif search_option == '2':
        product = input("\nEnter the shoe product to search: ")
        for shoe in shoe_list:
            if shoe.product.lower() == product.lower():
                print(str(shoe))
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
    # Print this information on the console for all the shoes in table format
    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        print(f'''
    Stock Value {shoe.product} ({shoe.code}): ${total_value:.2f}
              ''')
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
    print(f'''\nShoe with highest quantity:
          {str(highest_shoe)}
        \nPlease put {highest_shoe.product} on sale!''')
    pass

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

# ==========Main Menu=============
# Creating a menu that executes each function above.
# Changed the menu to have more of a flow to selections
# Value per item was included, I just renamed
# it to Inventory Cost as it sounded better


read_shoes_data()


while True:
    print('''
    Shoe Inventory Management System
        1. Shoe Inventory (all)
        2. Inventory Cost
        3. Search Product
        4. Adding Inventory
        5. Adding Stock
        6. Identify Sale Item
        7. Exit
    ''')
    choice = input("Please select operation to complete (1-7): ")
    if choice == '1':
        view_all()
    elif choice == '2':
        value_per_item()
    elif choice == '3':
        search_shoe()
    elif choice == '4':
        capture_shoes()
    elif choice == '5':
        re_stock()
    elif choice == '6':
        highest_qty()
    elif choice == '7':
        print('''\nExiting the program.
Have a great day!''')
        break
    else:
        print("Invalid option. Please select a option on the list.")
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# =======End of the program========
