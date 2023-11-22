numbers = [12, 13, 14, 15, 16, 14, 13, 17]
person =['Tawan', 'Patiya', 3, 'baby']
#key value pair
#dictionary
#object
#hash table
#overlap with set

person = {'name' : 'Tawan', 'address' : 'Patiya', 'age' : 3, 'job' : 'Baby'}
# print(person)
# print(person['age'])
print(person.keys())

print(person.values())

person['language'] ='Python'  #new key : value add korbo
print(person)

person['name']='Ishmam' #name update korbo
print(person)

del person['age'] #delete korar jnn
print(person)

#special dictionary looping
for key, value in person.items():
    print(key, value)
