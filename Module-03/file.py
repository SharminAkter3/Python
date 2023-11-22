#.csv : comma seperated value
#.txt : text file

# with open('message.txt', 'w') as file:
#     file.write('I learn python!')

# with open('message.txt', 'a') as file:
#     file.write('I learn python!')

with open('message.txt', 'r') as file:
    text = file.read()
    # print(text)

num = lambda a:a*a
print(num(2**2))