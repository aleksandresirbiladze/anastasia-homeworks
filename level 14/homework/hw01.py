list = []
for i in range (5) :
    pets = input ("enter five favorite animals ")
    list.append (pets)
print (list)

print (list [0])
print (list [-1])

pets = input ("enter the second pet ")
list [1] = pets
print (list)