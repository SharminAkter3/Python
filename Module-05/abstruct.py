# abstract base class
from abc import ABC, abstractmethod


class Animal(ABC):  # inherent korbo ABC theky
    @abstractmethod  # enforce all derived class to have a eat method
    def eat(self):
        print("Hlw everyone")

    @abstractmethod
    def move(self):
        pass


class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = "Monkey"
        self.name = name
        super().__init__()

    def eat(self):
        print("HII, everyone!!")

    def move(self):
        print("byee")


layka = Monkey("Lucky")
layka.eat()
layka.move()
# print(layka.eat())
