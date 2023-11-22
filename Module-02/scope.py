balance = 4000 #global variable

def buy_things(item, price):
    #local scope variable
    #you can access global variable without using the global keyword
    # balance=500 #local variable
    # print('Balance inside the function', balance)
    #if you want to modify a global variable, you have to use the global keyword
    global balance
    balance=balance - price
    print(f'Balance after buying {item}', balance)

buy_things('Sunglass', 1000)