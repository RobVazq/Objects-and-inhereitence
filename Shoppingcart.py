import math 
class Item:
    def __init__(self, description, price, quantity):
        self.description = description
        self.price = price
        self.quantity = quantity

    def cost(self):
        costAmt = self.price * self.quantity

        return costAmt

    def description(self):
        return self.description
    
if __name__ == "__main__":
    cart = []
    print(cart)
    print("one shopping trip later")

    p1 = Item('Banana', 3, 2)
    cart.append(p1.description)
    cart.append(p1.cost())
    p2 = Item("Shampoo", 7, 1)
    cart.append(p2.description,)
    cart.append(p2.cost())
    p3 = Item("Paper Clips", 2, 2)
    cart.append(p3.description)
    cart.append(p3.cost())
    p4 = Item("Chicken Nuggets", 5, 2)
    cart.append(p4.description)
    cart.append(p4.cost())


    
#im getting confused on how to .add the attributes on the list
#.append seems to the the thing that works for me

#I also dont think im displaying the loop in the correct way to show the cost
# and the items together using the class.
    TotalAmt = p1.cost() + p2.cost() + p3.cost() + p4.cost()
    
    for items in cart:
        print(items)

print("Your Shopping list costs ${}".format(TotalAmt))
        
