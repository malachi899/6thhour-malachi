#Name: Malachi campos
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("hello world")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
Bldictionary = {"Bl1" : "2009",
                 "Bl2" : "2012",
                 "Bl4" : [2024,2025,2026]}
#3. Print the keys of the dictionary from #2.
print(Bldictionary.keys())
#4. Print the values of the dictionary from #2
print(Bldictionary.values())
#5. Print one of the three numbers from the list by itself
print(Bldictionary["Bl4"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
Bldictionary.update({"bl3" : "2019"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(Bldictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
studentdictionary = {
    "student1" :
        {"name" : "raph",
         "grade" : 11,
         },
    "student2" :
        {"name" : "bensen",
          "grade" : 10,
         },
    "student3" : {
        "name" : "owyn",
        "grade" : 10,
    },
}


#9. Print the names of all three classmates on the same line.
print(studentdictionary)
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
studentdictionary.pop("student2")
print(studentdictionary)