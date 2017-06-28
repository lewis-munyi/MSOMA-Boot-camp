class Vendingmachine(object):
    def __init__(self, product, price):
        self.product = product
        self.stock = 0
        self.price = price
        self.balance = 0

    def restock(self, amount):
        self.stock += amount
        return "Successfully added " + str(amount) + " items. The total stock is now " + str(self.stock) + " items."
    
    def vend(self):
        if self.stock == 0:
            return "The machine is out of stock"
        else:
            self.stock -= 1
            return "Item returned. " + str(self.stock) + " items left in stock"
