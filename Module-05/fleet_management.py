# kono ak ta company manage korar cesta


class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fair = []


class Driver:
    def __init__(self, name, license, age) -> None:
        self.name = name
        self.license = license
        self.age = age


class Counter:
    def __init__(self) -> None:
        pass

    def purcahse_a_ticket(self, start, destination):
        pass


class Passenger:
    pass


class Supervisor:
    pass


john = Driver("John", "123", 20)
