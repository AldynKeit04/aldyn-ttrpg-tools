#this imports the random module

import random

#this imports the encounter list for the North West Forest 
#Region

from encGenScripts.regLists.NWlist import NWlist1

# used to determine how much is exactly generated
# the different if statements contain the creatures from 
# NWlist1, and are grouped based on how much are generated.
result = random.choice(NWlist1)

NWFresults = {
    ["Ajdurian Raiders", "Human Raiders"]:
        str(random.randint(3, 9))+" "+result, #1d6+2

    ["Weasels", "Wolverines", "Boars", "Lesser Bears"]: 
        str(random.randint(1, 6))+" "+result, #1d6

        ["Hungry Wolves", "Foxes"]:
        str(random.randint(1, 4))+" "+result, #1d4

    ["Squirrels", "Passive Wolves", "Giant Rhino Beetles", 
        "Jackals"]:
         str(random.randint(1, 10))+" "+result, #1d10

         ["Birds", "Giant Bees", "Giant Frogs"]: 
         str(random.randint(1, 20))+" "+result, #1d20
        }
#random +" " is because i fo:rgot to put spaces before the strings
#in big ol NWlist1. Oops, might fix later.
output1 = NWFresults[result]

