from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)


def get_shopping_list(store):
    """
    shows the available products,
    asks for user input to choose a product and an amount of such product
    loops until it gets no input value, then adds all products and amounts to a list
    :param store: needs an input of the instance of the store-class
    :return: returns a list of tuples of products and their amount
    """
    products = store.get_all_products()
    shopping_list = []

    print("--------")
    for index, product in enumerate(best_buy.get_all_products(), start=1):
        print(f"{index}. ", end="")
        product.show()
    print(
        "--------",
        "\nWhen you want to finish order, enter empty text."
    )

    while True:
        users_choice = input("Which product # do you want? ")
        if users_choice == "":
            break

        if not users_choice.isdigit() or not 1 <= int(users_choice) <= len(products):
            print("Invalid product number!")
            continue
        product = products[int(users_choice) -1]

        amount = input("What amount do you want? ")
        if not amount.isdigit() or int(amount) <= 0:
            print("Please enter a positive number!")
            continue

        shopping_list.append((product, int(amount)))
        print("Product added to list!\n")

    return shopping_list


def make_order(store):
    """
    gets products from the shopping list with its amount, checks for the products price
    prints the price of the whole checkout (single price * amount)
    :param store: needs an input of the instance of the store-class
    :return: no return value
    """
    shopping_list = get_shopping_list(store)

    if not shopping_list:
        print("No products selected.")
        return

    try:
        total = store.order(shopping_list)
        print(
            "********",
            f"\nOrder made! Total payment: {total} "
        )
    except ValueError as e:
        print(f"Order failed: {e}")


def start(store):
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
            for index, product in enumerate(store.get_all_products(), start=1):
                print(f"{index}. ", end="")
                product.show()

        elif user_input == "2":
            print(f"Total of {store.get_total_quantity()} items in store")

        elif user_input == "3":
            make_order(store)

        elif user_input == "4":
            break

        else:
            print("Invalid choice.")

start(best_buy)