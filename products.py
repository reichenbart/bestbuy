
class Product:


    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity) -> float:
        if self.quantity >= quantity:
            new_quantity = self.quantity - quantity
            self.set_quantity(new_quantity)
            return quantity * self.price
        else:
            raise ValueError(f"Only {self.quantity} products left.")





# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product("MacBook Air M2", price=1450, quantity=100)
#
# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())
#
# bose.show()
# mac.show()
#
# bose.set_quantity(1000)
# bose.show()