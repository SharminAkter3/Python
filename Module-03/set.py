#set : unique item collection. no duplicate 
# list : []
# tuple : ()
# set : {}

numbers = [12, 13, 14, 15, 16, 14, 13, 17]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)

numbers_set.remove(13)
print(numbers_set)

A={21, 23, 4,5 ,67}
B={21, 43, 34, 56}
print(A & B)  #& -> intersection
print(A | B)  #| -> union 