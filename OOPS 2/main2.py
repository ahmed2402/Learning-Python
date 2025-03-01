# Qs. Define a Employee class with attributes role, department & salary. This class should have a showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

class Employee : 
    def __init__(self,r,d,s):
        self.role = r
        self.department = d
        self.salary = s

    def showDetails(self):
        print(f"Your role is {self.role}")  
        print(f"Your department is {self.department}")  
        print(f"Your salary is {self.salary}")   

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("ML Engineer", "Cloud Team", 200000)


e1 = Engineer("Ahmed",19)
e1.showDetails()
