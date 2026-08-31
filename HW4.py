#Name: Malachi
#Class: 6th Hour
#Assignment: HW4

#1. Print "Hello World!"
print("Hello World")
#2. import the 'math' library
import math
#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.
x = float(input("Enter a decimal number for x: "))
y = int(input("Enter an integer for y: "))
#4. Create a variable with the value that is x and y added together.
int_sum = x+y
#5. Print the variable from #4.
print(int_sum)
#6. Create a variable with the value that is x and y added together, then divide the sum by 3.
var1 = (x+y) / 3
#7. Print the variable from #6.
print(var1)
#8. Create a variable with the value of the square root of y, then print the result.
var3 = (math.sqrt(y))
print(var3)
#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.
print(round(x,1))
#10. Use the ceiling function to round x up to the nearest whole number. Print the result.
rounded_up = math.ceil(x)
print(rounded_up)
#11. Use the floor function to round x down to the nearest whole number. Print the result.
result = math.floor(x)
print(result)