class GroceryShop:
    def __init__(self):
        self.inventory = {}  # dictionary of item names and their prices
        self.shopping_cart = set()  # set of item names in the shopping cart
        self.receipt = []  # list of item names and their prices in the receipt

    def load_inventory(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                name, price = line.strip().split(',')
                self.inventory[name] = float(price)

    def add_to_cart(self, item):
        if item in self.inventory:
            self.shopping_cart.add(item)

    def remove_from_cart(self, item):
        self.shopping_cart.discard(item)

    def checkout(self):
        total = 0
        for item in self.shopping_cart:
            price = self.inventory[item]
            self.receipt.append((item, price))
            total += price
        self.shopping_cart.clear()
        return total

    def print_receipt(self, filename):
        with open(filename, 'w') as f:
            f.write("Item\tPrice\n")
            f.write("----\t-----\n")
            for item, price in self.receipt:
                f.write(f"{item}\t{price:.2f}\n")
            f.write(f"Total:\t{self.checkout():.2f}")

grocery_shop = GroceryShop()

# load the inventory from a file
grocery_shop.load_inventory('inventory.txt')

# add some items to the shopping cart
grocery_shop.add_to_cart('apple')
grocery_shop.add_to_cart('banana')
grocery_shop.add_to_cart('orange')

# print the current shopping cart
print(grocery_shop.shopping_cart)

# checkout and print the total price
total = grocery_shop.checkout()
print(f"Total price: ${total:.2f}")

# print the receipt to a file
grocery_shop.print_receipt('receipt.txt')

