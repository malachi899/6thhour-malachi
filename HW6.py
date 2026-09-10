#Name: malachi
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
num_list = [7,10,15,8,4,19,6,17,18]
#2. Sort the list from highest to lowest.
num_list.sort(reverse=True)
#3. Create an empty list.
emp_list = []
#4. Remove the median number from the first list and add it to the second list.
var1 = num_list.pop(4)
emp_list.append(var1)
#5. Remove the first number from the first list and add it to the second list.
var2 = num_list.pop(0)
emp_list.append(var2)
#6. Print both lists.
print(num_list)
print(emp_list)
#7. Add the two numbers in the second list together and print the result.
emp_list_sum = emp_list[0] + emp_list[1]
print(emp_list_sum)
#8. Add the sum from #7 to the first list.
num_list.append(emp_list_sum)
#9. Sort the first list from lowest to highest and print it.
num_list.sort()
print(num_list)