from products import Product

class Store:

    def __init__(self, products_list):
        self.products = products_list


    def add_product(self, product: "Product") -> None:
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")
        if product in self.products:
            raise ValueError("Product is already in that store.")
        self.products.append(product)


    def remove_product(self, product: "Product") -> None:
        if product not in self.products:
            raise ValueError("Product is not in the store.")
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        return len(self.products)


    def get_all_products(self) -> list:
        return list(self.products)


    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price



# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product("MacBook Air M2", price=1450, quantity=100)
#
# best_buy = Store([bose, mac])
# price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
# print(f"Order cost: {price} dollars.")
#
# product_list = [Product("MacBook Air M2", price=1450, quantity=100),
#                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                 Product("Google Pixel 7", price=500, quantity=250),
#                ]
#
# best_buy = Store(product_list)
# products = best_buy.get_all_products()
# print(best_buy.get_total_quantity())
# print(best_buy.order([(products[0], 1), (products[1], 2)]))