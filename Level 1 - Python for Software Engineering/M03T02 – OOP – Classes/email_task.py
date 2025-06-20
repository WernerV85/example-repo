"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
# Initialise the instance variables for each email.


# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.
    def mark_as_read(self):
        self.has_been_read = True
# Create the __str__() method to return a string representation of the Email object.
#    def __str__(self):
#        return f"From: {self.email_address}\nSubject: {self.subject_line}\nContent: {self.email_content}\nRead: {self.has_been_read}"

# empty variable list to store email objects
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    email1 = Email("testemail@test.co.za","Test email Subject 1", "This is the first email for the task.")
    inbox.append(email1)
    email2 = Email("testemail2@test.co.za", "Test email Subject 2", "This it the second test email for the task.")
    inbox.append(email2)
    email3 = Email("testemail3@test.co.za", "Test email Subject 3", "This is the third test email for the task.")
    inbox.append(email3)
    pass


def list_emails():
    # Create a function that prints each email's subject line 
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line} - {'Read' if email.has_been_read else 'Unread'}")
        pass


def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"From: {email.email_address}\nSubject: {email.subject_line}\nContent: {email.email_content}")
        email.mark_as_read(True)
    pass


def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    for index, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{index}: {email.subject_line} - Unread")
        else:
            print(f"{index}: {email.subject_line} - Read")
    pass


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Add logic here to read an email
        list_emails()
        email_index = int(input("Enter the index of the email you want to read: "))
        read_email(email_index)
        # Call the read_email function with the selected index
        # This will display the email details and mark it as read.
        populate_inbox()
        # Call the populate_inbox function to ensure the inbox is populated with sample emails.
        list_emails()
        # Call the list_emails function to display all emails with their subject lines.
        # This will allow the user to select an email to read.

        pass

    elif user_choice == 2:
        # Add logic here to view unread emails
        view_unread_emails()
        # Call the view_unread_emails function to display all unread emails.
        populate_inbox()
        # Call the populate_inbox function to ensure the inbox is populated with sample emails.
        list_emails()
        # Call the list_emails function to display all emails with their subject lines.
        # This will allow the user to see which emails are unread.
        pass

    elif user_choice == 3:
        # Add logic here to quit application.
        print("Quitting application. Goodbye!")
        # Exit the loop and terminate the program.
        pass

    else:
        print("Oops - incorrect input.")
