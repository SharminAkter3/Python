class Calculator:
    brand = "Casio MS92"
    price = 450

    def add(self, num1, num2):
        addition = num1 + num2
        return addition

    def sub(self, num1, num2):
        substruction = num1 - num2
        return substruction

    def mult(self, num1, num2):
        multiplication = num1 * num2
        return multiplication

    def divi(self, num1, num2):
        division = num1 // num2
        return division


myCalcultor = Calculator()
result1 = myCalcultor.add(10, 20)
result2 = myCalcultor.sub(30, 20)
result3 = myCalcultor.mult(10, 20)
result4 = myCalcultor.divi(10, 5)
print(result1, result2, result3, result4)
