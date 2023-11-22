class Shop:
    shopping_mall = "Patiya"

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # cart is an instance attributes

    def add_to_cart(self, item):
        self.cart.append(item)


simran = Shop("Simran")
simran.add_to_cart("Shoes")
simran.add_to_cart("Phone")
print(simran.cart)

rafsan = Shop("Rafsan")
rafsan.add_to_cart("Watch")
rafsan.add_to_cart("Shirt")
print(rafsan.cart)
