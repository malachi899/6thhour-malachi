#Name: Malachi
#Class: 6th Hour
#Assignment: HW14
import random

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i = 5
while i > -1:
    print(i)
    i -= 1
else:
    print("Hello World!")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
k = 1
while k < 30:
    k += 1
    if k % 2 == 0:
        print(k)
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.

l = 0

while l < 30:
    l += 1
    if l % 3 == 0:
        continue
    else:
        print(l)
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
while True:
    y = random.randint(1, 6)
    print(y)
    if y == 1:
        break
#5. Create a while loop that asks for a number input until the user inputs the number 0.
while True:
    t = int(input("input a 0"))
    if t == 0:
        break