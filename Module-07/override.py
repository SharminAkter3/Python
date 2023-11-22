class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Rice, Fish, Water")

    def exercise(self):
        raise NotImplementedError  # force korbo


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # Override
    def eat(self):
        print("Vegetables")

    def exercise(self):
        print("hudai time lose")

    # + sign operator overload
    def __add__(self, other):
        return self.age + other.age  # age jog korbo

    def __mul__(self, other):
        return self.weight * other.weight


sakib = Cricketer("Sakib", 30, 6.4, 70, "BD")
rakib = Cricketer("Rakib", 32, 5.4, 10, "BD")

# sakib.eat()
# sakib.exercise()


print(200 + 100)
print("simran" + "rafsan")
print([12, 98] + [3, 6, 8, 8])
print(sakib + rakib)
print(sakib * rakib)
