def full_name(first, last):
    name = f"{first} {last}"  # string newar jnn --> fstring use korechi
    return name


# take parameter in order(serialwise)
# name = full_name('Sharmin', 'Akter')

name = full_name(last="Akter", first="Sharmin")
# print(name)


# def famous(**kargs)
def famous_name(first, last, **addition):
    name = f"{first}{last}"
    for key, value in addition.items():
        print(key, value)
    return name


name = famous_name(first="Shamrin ", last="Akter", title="Miss", addition="Rahaman")
print(name)

# def funcion_name(num1, num2, *args, **kargs):


def a_lot(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    remain = num1 - num2
    # return sum, mul, remain
    return [sum, mul, remain]


everything = a_lot(55, 21)
print(everything)
