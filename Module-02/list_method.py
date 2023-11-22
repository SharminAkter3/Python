numbers= [12, 13, 14, 15, 16]
numbers.append(18)   #list er shes e new element add kora 
print(numbers)

numbers.insert(2, 20)  # list er j kono ak ta perticular position e value add kora #insert(index, value)
print(numbers)

numbers.remove(14) # kono akta item k remove kory dewa
print(numbers)

#element ta agy achy kina check korbo ...tarpor remove korbo
if 20 in numbers:
    numbers.remove(20)
print(numbers)

last = numbers.pop()  #last element ta delete korbo
print(last, numbers)

index= numbers.index(12)  #index khujy ber kora 
print(index)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)