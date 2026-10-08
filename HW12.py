#Name: malachi
#Class: 6th Hour
#Assignment: HW12

import random
#1. Print Hello World!
print("Hello World")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = random.choice([True, False])
login = random.choice([True, False])
admin = random.choice([True, False])
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
loginvar = 1
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".\
password = "Gin"
userinput = input("Enter your password: ")
if userinput == password:
    print("Access Granted!")
else:
    print("Access Denied. Incorrect password.")
if wifi:
    if login:
        if admin:
            print("wakey wakey time for school")
            loginvar+=1
        else:
            print("Error! Missing admin privileges.")
    else:
        print("Error! Missing login credentials.")
else:
    print("Error! Missing Wi-Fi connection.")