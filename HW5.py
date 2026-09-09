#Name: malachi
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!
print("hello world")
#1. Create a list with 5 strings containing 5 different names in it.
Bl2_list = ["Axton","maya","Salvador","Zer0","Gaige"]
#2. Append a new name onto the Name List.
Bl2_list.append(input("give me a name: "))
#3. Print out the 4th name on the list.
print(Bl2_list[3])
#4. Create a list with 4 different integers in it.
int_list = [4,7,12,2000]
#5. Insert a new integer into the 2nd spot and print the new list.
int_list.insert(1,17)
print(int_list)
#6. Sort the list from lowest to highest and print the sorted list.
int_list.sort()
print(int_list)
#7. Add the 1st three numbers on the sorted list together and print the sum.
int_list_sum = int_list[0] + int_list[1] + int_list[2]
print(int_list_sum)
#8. Create a list with two strings, two integers, and two boolean values.
mixed_list = ["Rafa","Amon",4,9,True,False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(mixed_list[int(input("enter index location: "))])