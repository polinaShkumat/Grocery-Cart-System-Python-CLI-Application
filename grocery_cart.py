"""
Grocery Cart System — CLI Application
=======================================
A small interactive grocery shopping simulator: add items to a cart while
checking live stock, remove items back into stock, undo the last action,
and check out with a 10% discount for orders over 30€.

Author: (your name)
"""

price = {"apple": 2, "banana": 1, "milk": 3, "bread": 2}
quantity = {"apple": 200, "banana": 100, "milk": 30, "bread": 25}

cart = {}
last_action = None


def add_to_cart():
    """Repeatedly prompt for products to add until the user types 'done'."""
    global last_action
    while True:
        name = input("\n1: Add (or type 'done' to end): ")
        if name == "done":
            break

        if name not in quantity:
            print(f"Error: there is no such product. Products available: {quantity}")
            continue

        qty = int(input(f"Type amount for {name}: "))

        if qty <= quantity[name]:
            quantity[name] -= qty
            cart[name] = cart.get(name, 0) + qty
            print(f"Added {qty} {name} to our cart. There is {quantity[name]} left")
            last_action = ("add", name, qty)
        else:
            print(f"There is not enough {name}! Available: {quantity[name]}")


def remove_from_cart():
    """Repeatedly prompt for products to remove from the cart back into stock."""
    global last_action
    while True:
        name = input("\n1: Type name of product to remove it (or 'done' to end): ")
        if name == "done":
            break

        if name not in cart or cart[name] == 0:
            print(f"Error: there is no such product in your cart. Cart contents: {cart}")
            continue

        qty = int(input(f"Type amount for {name} to remove: "))

        if qty <= cart[name]:
            cart[name] -= qty
            quantity[name] += qty
            print(f"Removed {qty} of {name}. There is {cart[name]} left in cart")
            last_action = ("remove", name, qty)
        else:
            print(f"There is not enough {name} in your cart to remove! Available: {cart[name]}")


def undo_last_action():
    """Ask whether to undo the last add/remove action, and roll it back."""
    global last_action
    undo_choice = input("You want to discard last action? (yes/no): ")

    if undo_choice != "yes":
        return

    if last_action is None:
        print("There is no action to discard")
        return

    act_type, item, qty = last_action

    if act_type == "add":
        cart[item] -= qty
        quantity[item] += qty
        if cart[item] == 0:
            del cart[item]
        print(f"Successfully cancelled addition of {qty} {item}")

    elif act_type == "remove":
        cart[item] = cart.get(item, 0) + qty
        quantity[item] -= qty
        print(f"Successfully cancelled removal of {qty} {item}")

    last_action = None


def checkout():
    """Print a receipt for everything in the cart, applying a 10% discount over 30€."""
    print("\n--- RECEIPT ---")
    gross_price = 0

    for item, count in cart.items():
        item_total = count * price[item]
        gross_price += item_total
        print(f"{item} : {count} x {price[item]}€ = {item_total}€")

    print(f"Initial sum: {gross_price}€")

    if gross_price > 30:
        discount = int(gross_price * 0.10)
        final_price = gross_price - discount
        print(f"Discount 10% applied: -{discount}€")
        print(f"Total price with discount: {final_price}€")
    else:
        print(f"Total price: {gross_price}€")


def main():
    add_to_cart()
    remove_from_cart()
    undo_last_action()
    checkout()


if __name__ == "__main__":
    main()
