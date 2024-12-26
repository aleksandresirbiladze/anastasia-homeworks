user = []

for i in range (10) :
    user1 = int (input("enter 10 numbers "))
    user.append(user1)
print (user)

print (user[0 : 4])

user2 = []

user2.extend(user [3 : 7])

print (user[-1] == 10)