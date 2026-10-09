#Name: malachi
#personal work


import random
import time
wifi = random.choice([True, False])
login = random.choice([True, False])
admin = random.choice([True, False])
loginvar = 1
password = "Gin"
userinput = input("Enter your password: ")
if userinput == password:
    print("Access Granted!")
else:
    print("Access Denied. Incorrect password.")
    penalty_time = 60
    for i in range(penalty_time, 0, -1):
        print(f"Please wait {i} seconds to try again...", end="\r")
        time.sleep(1)
    print("\n")
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