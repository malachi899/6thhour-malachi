#Name: malachi
#Class: 6th Hour
#Assignment: HW11

import random
#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
numlist = [random.randint (1,100), random.randint (1,100), random.randint (1,100),]
#3. Print the list.
print(numlist)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
num1 = numlist[0]
num2 = numlist[1]
num3 = numlist[2]
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)
#5. Tie the result (the largest number) from #4 to a variable called "num".
num = max(num1, num2, num3)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2
