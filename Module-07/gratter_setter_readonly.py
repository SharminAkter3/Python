# read only --> you can not set the value. Value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute
# setter --> set a value of a property through a method. Most of the time,  you will set the value of a private property.


class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    # getter without any setter(kono man set kora) is readonly attribute
    @property  # decorator
    def age(self):
        return self._age

    # getter  --> kono man newa
    @property
    def salary(self):
        return self.__money

    # setter
    @salary.setter  # salary ta ky setter banabo
    def salary(self, value):
        if value < 0:
            return "Salary can not be negative"
        self.__money += value


samsu = User("Kopa", 21, 2400)
# print(samsu.__money)
print(samsu.age)
print(samsu.salary)
samsu.salary = 4000
