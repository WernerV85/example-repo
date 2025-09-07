class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # method to display Head office
    def head_office(self):
        print("Head Office: Cape Town, South Africa")


# New inherent class
class OOPCourse(Course):
    
    #Define Attributes for OOPCourse class
    description = "OOP Fundamentals"
    trainer = "Mr. Anon A. Mouse"
        
    # Define method to display in OOPCourse Class
    def trainer_details(self):
        print("In this course you will learn about", self.description, ". The name of your trainer is ", self.trainer)

    # Define method to display course id
    def course_id(Self):
        print("The course ID is: #12345")


course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.course_id()



# Example usage:
# Create an instance of the Course class
#course = Course()

# Call the contact_details method to display contact information
#course.contact_details()
