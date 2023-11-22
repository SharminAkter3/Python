# print('Now I take input')
# input()
# input('Now I take input : ')
# money = input('Now I take input : ')
# print(money)

first_money = input('Now I take money from first person : ')
second_money = input('Now I take money from second person : ')
# print(first_money, second_money)
print(type(first_money))
# by default the input user will be string type

first_money_int = int(first_money)
second_money_int = int(second_money)
print(type(first_money_int))
print(type(second_money_int))

# print("total money i got : " ,first_money + second_money)

total= first_money_int+ second_money_int;
print(total)