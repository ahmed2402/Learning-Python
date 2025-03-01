# Let‘s Practice
# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name 
        self.m1 = marks1 
        self.m2 = marks2 
        self.m3 = marks3

    def printAvg(self):
        self.avg = (self.m1 +self.m2+self.m3) / 3
        print("Avg of your marks is : ",self.avg)

s1 = Student("Ahmed",98,87,93)
s1.printAvg()        
