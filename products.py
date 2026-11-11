
class Product:
    """A single product in the store with a name, a price and a quantity."""

    def __init__(self, name, price, quantity):
        """
        Validate the input data and create a new, active product.

        :param name: name of the product, must be a non-empty string
        :param price: price of a single item, must not be negative
        :param quantity: number of items in stock, must not be negative
        :raises ValueError: if the name is empty or price/quantity negative
        :raises TypeError: if an argument has the wrong type
        """
        if not isinstance(name, str):
            raise TypeError("Product name must be a string.")
        if not name.strip():
            raise ValueError("Product name must not be empty.")

        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise TypeError("Product price must be a number.")
        if price < 0:
            raise ValueError("Product price must not be negative.")

        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError("Product quantity must be a whole number.")
        if quantity < 0:
            raise ValueError("Product quantity must not be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the number of items in stock."""
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set the number of items in stock.

        The product is deactivated when the quantity reaches 0.
        :raises ValueError: if the quantity is negative
        """
        if quantity < 0:
            raise ValueError("Product quantity must not be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print the name, price and quantity of the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """
        Buy a given quantity of the product and update the stock.

        :param quantity: number of items to buy, must be positive
        :return: total price of the purchase
        :raises ValueError: if the product is inactive, the quantity is not
                            positive or there is not enough stock
        """
        if not self.is_active():
            raise ValueError(f"{self.name} is not available.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")
        if quantity > self.quantity:
            raise ValueError(
                f"Only {self.quantity} items of {self.name} left."
            )

        self.set_quantity(self.quantity - quantity)
        return quantity * self.price
