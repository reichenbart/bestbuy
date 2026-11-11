from products import Product
from store import Store


def list_products(products):
    """Print a numbered list of the given products."""
    for index, product in enumerate(products, start=1):
        print(f"{index}. ", end="")
        product.show()


def get_shopping_list(store):
    """
    Ask the user which products and amounts to order.

    Shows the available products and loops until the user enters
    an empty text.
    :param store: instance of the Store class
    :return: list of tuples (product, amount)
    """
    products = store.get_all_products()
    shopping_list = []

    print("--------")
    list_products(products)
    print("--------")
    print("When you want to finish order, enter empty text.")

    while True:
        users_choice = input("Which product # do you want? ")
        if users_choice == "":
            break

        if (not users_choice.isdigit()
                or not 1 <= int(users_choice) <= len(products)):
            print("Invalid product number!")
            continue
        product = products[int(users_choice) - 1]

        amount = input("What amount do you want? ")
        if not amount.isdigit() or int(amount) <= 0:
            print("Please enter a positive number!")
            continue

        shopping_list.append((product, int(amount)))
        print("Product added to list!\n")

    return shopping_list


def make_order(store):
    """
    Let the user create a shopping list and order it.

    Prints the total price of the order or an error message.
    :param store: instance of the Store class
    """
    shopping_list = get_shopping_list(store)

    if not shopping_list:
        print("No products selected.")
        return

    try:
        total = store.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: {total}")
    except ValueError as error:
        print(f"Order failed: {error}")


def start(store):
    """
    Show the store menu and handle the user's choices until they quit.

    :param store: instance of the Store class
    """
    while True:
        print(
            "\n  Store Menu",
            "\n  ----------",
            "\n1. List all products in store",
            "\n2. Show total amount in store",
            "\n3. Make an order",
            "\n4. Quit"
        )
        user_input = input("Please choose a number: ")

        if user_input == "1":
            list_products(store.get_all_products())
        elif user_input == "2":
            print(f"Total of {store.get_total_quantity()} items in store")
        elif user_input == "3":
            make_order(store)
        elif user_input == "4":
            break
        else:
            print("Invalid choice.")


def main():
    """Set up the initial stock of inventory and start the store menu."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()