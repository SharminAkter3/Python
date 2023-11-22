class Shopping:
    cart = []  # class attribute # static attribute
    origin = "China"

    def __init__(self, name, location) -> None:
        self.name = "Big bazar"  # instance attribute
        self.location = "Patiya"

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"buying : {item} for price : {price} and remaining amount : {remaining}")

    @staticmethod
    def multiply(a, b):
        result = a * b
        print(result)

    @classmethod
    def for_show(self, item):
        print("hudai dekhi : ", item)


# Shopping.purchase("Tops", 2, 500, 1300)
basundara = Shopping("hudi", "Patiya")
# basundara.purchase("tops", 500, 1000)
basundara.for_show("tops")

Shopping.multiply(4, 6)
