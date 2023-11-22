#list, array, collection is same(simple terms)
#index =   0  1   2   3   4   5   6   7   8
numbers = [32, 4, 56, 43, 34, 25, 89, 78, 57]
#index =  -8  -7   -6   -5   -4   -3   -2   -1   #python ulta dhik theky ak ta list maintain kory 

print(numbers[3], numbers[-3])

#list(start:end)
print(numbers[2:6])   # index 2 theky 6 er ag porjonto print 

#list(start : end : step)
print(numbers[2:6:1])
print(numbers[2:6:2])  #2 step kory agaby

print(numbers[7 : 2 : -1])  #ulta dhik theky print korby 

print(numbers[4 : ])   # 4th index theky last porjonto 
print(numbers[ : 5])    # 5th index er ag porjonto print korby 
print(numbers[:])   #1st to last sob golo print korby  #shortcut to copy a list

print(numbers[ : :-1]) #1st to last porjonto print korby reverse way ty  # shortcu to reverse a list 