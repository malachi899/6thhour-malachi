#Name: Malachi
#Class: 6th Hour
#Assignment: HW8


#1. Import the "random" library
import random
from random import shuffle

#2. print "Hello World!"
print("hello world")
#3. Create three different variables that each randomly generate an integer between 1 and 10
var1 = random.randint (1,10)
var2 = random.randint (1,10)
var3 = random.randint (1,10)
#4. Print the three variables from #3 on the same line.
print(var1, var2, var3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
var1 = var1 + 2
var2 = var2 - 4
var3 = var3 * 1.5
#6. Print each result from #5 on the same line.
print(var1, var2, var3)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
list1 = [random.randint(1, 6) for _ in range(4)]
#8. Sort the list in #7 and print it.
list1.sort()
print(list1)
#9. Add together the highest three numbers in the list from #7 and print the result.
highsum = sum(list1[1:])
print(highsum)
#10. Create a list with 5 names of other students in this class and print the list.
classlist = ["owen", "misa", "raph","bensen","owyn"]
print(classlist)
#11. Shuffle the list in #10 and print the list again.
shuffle(classlist)
print(classlist)
#12. Print a random choice from the list of names from #10.
print(random.choice(classlist))