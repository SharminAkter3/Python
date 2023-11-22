numbers = [45, 23, 34, 67, 89, 20, 23, 55, 50]
odds = []
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
# print(odds)

odd_num = [num for num in numbers if num % 2 == 1 and num % 5 == 0]
# print(odd_num)

players = ['Tahsin', 'Tawan', 'Tasnuba']
ages = [8, 3, 9]

age_comb=[]
for player in players:
    print('Player :' , player)
    for age in ages:
        print(player , age)
        age_comb.append([player, age])
print(age_comb)
age_comb2 = [(player, age) for player in players for age in ages]
print(age_comb2)