from products import Product


class Store:
    """A store that holds products and handles orders."""

    def __init__(self, products_list):
        """Create a store with an initial list of products."""
        self.products = list(products_list)

    def add_product(self, product: Product) -> None:
        """
        Add a product to the store.

        :raises TypeError: if the argument is not a Product
        :raises ValueError: if the product is already in the store
        """
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")
        if product in self.products:
            raise ValueError("Product is already in that store.")
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Remove a product from the store.

        :raises ValueError: if the product is not in the store
        """
        if product not in self.products:
            raise ValueError("Product is not in the store.")
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total number of items of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list:
        """Return a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """
        Buy all products of a shopping list.

        :param shopping_list: list of tuples (product, quantity)
        :return: total price of the order
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price