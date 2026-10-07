#Name:malachi
#Class: 6th Hour
#Assignment: HW10

import random
#1. Print "Hello World!"
print("Hello World")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
a = random.randint(1,10)
b = random.randint (1,10)
c = random.randint (1,10)
#3. Print A, B, and C on the same line.
print(a,b,c)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if a < 5:
    print("less than 5")
else:
    print("greater than 5")
#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if 3 < b < 7:
    print(" in between 3 and 7")
else:
    print("not in between 3 and 7")
#6. Make an if statement that prints if variable C is even or odd.
if c % 2 == 0:
    print("even number")
else:
    print("odd number")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
d = 3 + random.randint (1,20)
print(d)
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
if d > a + b + c:
    print("greater than")
else:
    print("less than")