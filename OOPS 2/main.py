# **Let's Practice**  
# **Qs.** Define a **Circle** class to create a circle with radius r using the constructor.  
# Define an **Area()** method of the class which calculates the area of the circle.  
# Define a **Perimeter()** method of the class which allows you to calculate the perimeter of the circle.

class Circle : 
    def __init__(self, r):
        self.radius = r

    def Area(self):
        self.area = 3.142 * self.radius * self.radius
        print(f"AREA OF CIRCLE = {self.area}") 
    def Perimeter(self):
        self.perimeter = 2*3.142*self.radius   
        print(f"PERIMETER OF CIRCLE = {self.perimeter}")     

c1 = Circle(8.5)
print(c1.radius)
c1.Area()
c1.Perimeter()