# base class, parent class => common attribute + funtionality class
# derived class, child class => uncommon attribute + funtionality class


class Device:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        return f"running laptop : {self.brand}"


class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd

    def conding(self):
        return f"learning python and practching"


class Phone(Device):
    def __init__(self, brand, price, color, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color)

    def phone_call(self, number, text):
        return f"Sending SMS to : {number} with : {text}"

    def __repr__(self) -> str:
        return f"phone : {self.dual_sim}"


class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass


# inheritance
my_phone = Phone("redmi", 14000, "blue", True)
print(my_phone.brand, my_phone.price, my_phone.color)
# print(my_phone)
