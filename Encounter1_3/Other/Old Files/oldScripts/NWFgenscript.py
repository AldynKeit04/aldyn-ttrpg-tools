#this imports the random module

import random

#this imports the encounter list for the North West Forest 
#Region

from encGenScripts.regLists.NWlist import NWlist1

# used to determine how much is exactly generated
# the different if statements contain the creatures from 
# NWlist1, and are grouped based on how much are generated.
def NWFresults():
    result = random.choice(NWlist1)
    if result in ["Ajdurian Raiders", "Human Raiders"]:
        return str(random.randint(3, 9))+" "+result #1d6+2

    elif result in ["Weasels", "Wolverines", "Boars",
            "Lesser Bears"]: 
        return str(random.randint(1, 6))+" "+result #1d6

    elif result in ["Hungry Wolves", "Foxes"]:
        return str(random.randint(1, 4))+" "+result #1d4

    elif result in ["Squirrels", "Passive Wolves",
            "Giant Rhino Beetles", "Jackals"]:
        return str(random.randint(1, 10))+" "+result #1d10

    elif result in ["Birds", "Giant Bees", "Giant Frogs"]:
        return str(random.randint(1, 20))+" "+result #1d20

#random +" " is because i forgot to put spaces before the strings
#in big ol NWlist1. Oops, might fix later.


