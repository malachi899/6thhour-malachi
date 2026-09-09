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
import statistics
median_val = statistics.median(num_list)
num_list.remove(median_val)
emp_list.append(median_val)
#5. Remove the first number from the first list and add it to the second list.

#6. Print both lists.

#7. Add the two numbers in the second list together and print the result.

#8. Move the number back to the first list (like you did in #4 and #5 but reversed).

#9. Sort the first list from lowest to highest and print it.