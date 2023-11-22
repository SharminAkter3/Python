# in, not, not in, is, is not, and , or

a=4
if a>5:
    print("Grater than 5")
elif a>3:
    print('much grater')
else:
    print("Less than 5")


is_single = True
if is_single is True:
    print("Yes")
else:
    print("No")


is_single = False
if is_single is not True:
    print("Yes")
else:
    print("No")

#nested condition
boss= True
sister= "Single"
if boss == True:
    print("Hello")
    if sister == "Double":
        print("Hurry")
    else:
        print("Sad")
else:
    print("Hii")