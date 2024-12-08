#1
user_name = input("enter your name: ")
friend_surname = input("enter the friend's last name: ")
print ("your name and your friend's last name: " + user_name + " " + friend_surname) 

#2
age = int(input("enter your age: "))
print ("your age will be 10 years: " + str(age + 10))

# 4. ახსნა (კომენტარებში)

# Case Sensitive ნიშნავს, რომ ასოები დიდსა და პატარას შორის განსხვავდება.
# მაგ., "name" და "Name" Python-ში სხვადასხვა ცვლადებია.

# Snake Case არის სახელწოდებების დასაწერი სტილი, სადაც სიტყვები ერთმანეთისგან ქვედა ტირეს (_) საშუალებით გამოიყოფა.
# მაგ., user_name, first_name

#5 
# Debugging ნიშნავს კოდის შეცდომების პოვნასა და გასწორებას.

# შეცდომა 1:
prin ("Hello World")  #ფუნქციის სახელია print, არა prin

# შეცდომა 2:
age = input("შეიყვანეთ ასაკი: ")
print("თქვენი ასაკი არის: " + age + 10)  #უნდა გარდავქმნათ age მთლიან რიცხვად, სწორი ვერსია: int(age)

# შეცდომა 3:
name = "ტასო"
print("გამარჯობა", name) # სწორია, მაგრამ უნდა იყოს print("გამარჯობა " + name) თუ + ვიყენებთ

# შეცდომა 4:
num = 5
if num = 5:  #პირობა უნდა იყოს ==, სწორი ვერსია: if num == 5:
 print("რიცხვი ხუთია")

# შეცდომა 5:
average = sum([1, 2, 3, 4, 5] / 5)  #sum ფუნქცია მთლიან სიას ამატებს. სწორი: sum([1, 2, 3, 4, 5]) / 5
