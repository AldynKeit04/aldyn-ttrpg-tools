import random

#This list is the first thing which the script goes over i
#in order to determine what is generated. There are multiple 
#of the same thing, because I don't know how else to weigh the 
#statistical chances of them.
mainList = ["Human Raiders", "Ajdurian Raiders", 
        "Noble Party", "Hostile Animals",
        "Passive Animals", "Guard Patrol", "Commoner Party",
        ]

#If the function below gets "Passive Animals", it randomly 
#chooses on
#this script to determine the specific type of animals.
passDict = {
        "Foxes" : random.randint(1, 4),
        "Squirrels" : random.randint(1, 10),
        "Weasels" : random.randint(1, 6),
        "Passive Wolves" : random.randint(1, 10),
        "Wolverines" : random.randint(1, 6),
        "Birds" : random.randint(1, 20),
        }

#Same as above, but with Hostile Animals.
hostDict = {
        "Hungry Wolves" : random.randint(1, 4),
        "Giant Rhino Beetles" : random.randint(1, 10),
        "Boars" : random.randint(1, 6),
        "Jackals" : random.randint(1, 10),
        "Lesser Bears" : random.randint(1, 6),
        "Giant Bees" : random.randint(1, 20),
        "Giant Frogs" : random.randint(1, 20),
        }
comDict = {
        "Merchants" : 
        ["Merchants", random.randint(1,10), "Guards", random.randint(1,8)],
        "Mercenaries" : 
        ["Guards", random.randint(4,11), "Leaders", random.randint(1,4)],
        "Travellers" :
        ["Unarmed Travellers"+str(random.randint(2,5)),
            "Armed Travellers"+str(random.randint(1,4))]
        }
nobDict = {
    "Nobleman's Escort" : 
        ["Guards", random.randint(6,13), "Nobles", random.randint(2,4)],
    "Grand Wizard's Escort" : 
        ["Guards", random.randint(4, 7), "Magic-Users", random.randint(4,9)],
    "Holy Convoy" :
        ["Level 3 Clerics", random.randint(2,8), "Paladins", random.randint(1,5)],
    "Military Contingent" : 
        ["Solders", random.randint(2,24), "Level 2 Leaders", random.randint(1,4)],    
        }

#There is no "Raider" list because there aren't any specific 
#types
#of raiders.

