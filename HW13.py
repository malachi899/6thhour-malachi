#Name: Malachi
#Class: 6th Hour
#Assignment: HW13

#1. Import the random function
import random
#2. Create a variable called 'temp' that randomly generates a number between 1 and 30
temp = random.randint(1,30)
print(temp)
#3. Go to the link below and convert the flowchart into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg
#if the temperature is greater than 20 print "its hot"
#elif the temperature is greater than 10 print "its mild"
#else print its cold
#print "thank you"
if temp > 20:
    print("its hot")
elif temp > 10:
     print("its mild")
else :
     print("its cold")
print("thank you")
