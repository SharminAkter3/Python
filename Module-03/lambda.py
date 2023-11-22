# lambda

# def double(x):
#     return x*2

double = lambda num : num * 2
square = lambda num : num * num
result = double(2)
output = square(3)
# print(result, output)

add = lambda x, y : x + y
sum = add(44, 31)
# print(sum)

numbers = [12, 13, 14, 15, 16, 14, 13, 17]
# double_nums= map(double, numbers)
double_nums = map(lambda x : x*2, numbers)
# print(numbers)
# print(list(double_nums))

actors =[
    {'name' : 'Sabana', 'age' : 60},
    {'name' : 'Sabnur', 'age' : 65},
    {'name' : 'Sabila', 'age' : 30},
    {'name' : 'Simran', 'age' : 20},
    {'name' : 'Sawon', 'age' : 10},
]

juniors = filter(lambda actor : actor['age'] < 30, actors)
print(list(juniors))