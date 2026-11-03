#Name:
#Class: 6th Hour
#Assignment: SC3

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
f = 1
while f < 100:
    f += 1
    print(f)
    if f % 3 == 0 and f % 5 == 0:
        print("FizzBuzz")
    elif f % 3 == 0:
        print("Fizz")
    elif f % 5 == 0:
        print("Buzz")

