numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_number = int (input("enter your first number"))
last_number = int (input("enter your last number"))

if first_number < last_number : 
    print (numbers[first_number : last_number])

elif first_number > last_number :
    print (numbers[last_number : first_number + 1])

else : 
    print ("error")