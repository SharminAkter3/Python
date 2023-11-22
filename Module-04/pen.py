class Pen:
    pass

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


myPen = Pen("AlTime", 7)
print(myPen.brand, myPen.price)
hisPen = Pen("HighSchool", 6)
print(hisPen.brand, hisPen.price)
