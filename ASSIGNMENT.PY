class Student:
    
    #   now this is a Constructor or initialiser function for Student class
    def __init__(self, name, regno):
        self.name = name
        self.regno = regno
       
    
    # Method to display entered Values
    def display(self):
         
        # An if statement to check if the entered value for name is not a digit 
        if not self.name.isdigit():
            print(f"your name  is: {self.regno}\n Your Registration Number is : {self.name}")
        
        # If the entered value for name is a digit, it returns this print statement
        else:
            print(f"Error: Please input characters for name")

# Variables to capture values for regno and name
name = input("Please enter your name:\n")
regno = input("Please enter your Registration Number:\n")

        #if i put in my details it will display when i run the code but if i dont it will ask me to enter my name
#name = input("robert ssekisonge:\n")
#regno = input("m23b13/056:\n")



# Object of the class Student 
capture = Student(name, regno)
capture.display()