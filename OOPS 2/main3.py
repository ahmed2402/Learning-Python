# Let's Practice
# Qs. Create a class called Order which stores item & its price.
# Use Dunder function __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2.

class Order : 
    def __init__(self, i , p):
        self.item = i
        self.price = p

    def __gt__(self,obj2):
         if(self.price>obj2.price):
             print(f"Price of Item 1  {self.item} is greater")
         else :
             print(f"Price of Item 2  {obj2.item} is greater")     
        # return self.price > obj2.price

o1 = Order("apple",10)
o2 = Order("mango",20)

print(o1>o2)

