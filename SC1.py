#Name: Malachi Campos
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.
creaturedictonary = {
    "skag" : {
        "danger" : "low",
        "type" : "physical",
        "damage" : 100,
        "health" : 50,
        "defense" : 5,
    },
    "psycho" : {
        "danger" : "low",
        "type" : "physical",
        "damage" : 200,
        "health" : 100,
        "defense" : 10,
    },
    "gardian" : {
        "danger" : "medium",
        "type" : "energy/plasma",
        "damage" : 500,
        "health" : 250,
        "defense" : 40,
     },
    "Handsome Jack" : {
        "danger" : "high",
        "type" : "shock",
        "damage" : 2000,
        "health" : 5000,
        "defense" : 250,
    },
    "The Warrior": {
        "danger": "extreme",
        "type": "fire",
        "damage": 5000,
        "health": 10000,
        "defense": 1000,
        "weak spot" : "chest"
    },
}
while True:

    enemyselect = str(input("What enemy needs changes(skag,The Warrior,Handsome Jack,gardian,psycho)"))
    enemystat = str(input("what stat needs to be changed(damage,health,defense)"))
    enemychange = int(input("what do you want to change the stat to"))
    creaturedictonary[enemyselect].update({enemystat: enemychange})
    keepgoing = input("Do you want to change another enemy? (yes/no): ").lower()
    if keepgoing != 'yes':
        print("Exiting setup. Final stats saved!")
        break
print(creaturedictonary)

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.