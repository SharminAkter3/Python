def sum(num1, num2, num3=0): #num3 optinal hiseby rakhchi 
    result= num1+num2+num3
    return result

total = sum(12, 10)
# print("Total : ", total)


#args
def all_sum(num1, num2, *numbers): #parameter er agy * dily... icca moto parameter newa jaby 
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum = sum + num
    return sum

total = all_sum(44, 31, 44, 30, 12)
print("all total : ", total)
