class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"Item": item, "Price": price, "Quantity": quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item["Price"] * item["Quantity"]
        print("total Price", total)
        if amount < total:
            print(f"Please Provide {total - amount} more")
        else:
            extra = amount - total
            print(f"here is your items and extra money {extra}")


Simran = Shopping("Simran Rahaman")
Simran.add_to_cart("Potato", 50, 5)
Simran.add_to_cart("Tomato", 100, 2)
Simran.add_to_cart("Rice", 150, 3)

print(Simran.cart)
# Simran.checkout(700)
Simran.checkout(7000)
