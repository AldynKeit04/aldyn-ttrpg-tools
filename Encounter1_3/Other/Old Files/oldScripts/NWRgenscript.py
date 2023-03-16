import random

#This is mainly a test for a set of random generation scripts
#in my random generator project.
import random
from regLists.NWroadlist import NWRlist 

#The irl matrix has various sublists with things assigned to
#them. This is a way of simulating that.
testDict = {
        "Passive Animals" : [
            str(random.randint(1, 4))+" Foxes", 
            str(random.randint(1, 6))+" Wolverines", 
            str(random.randint(1, 10))+" Squirrels",
            str(random.randint(1, 20))+" Birds", 
            str(random.randint(1, 6))+" Weasel", 
            str(random.randint(1, 10))+"Passive Wolves"],
        "Hostile Animals" : [
        str(random.randint(3, 30))+" Hungry Wolves",
        str(random.randint(1, 6))+" Giant Rhino Beetles",
        str(random.randint(1, 6))+" Jackals",
        str(random.randint(1, 2))+" Lesser Bear",
        str(random.randint(1, 10))+" Giant Bees",
        str
            ]
        }

def testfunction():
    tx = random.choice(NWRlist)
    if tx == "Human Raiders":
        return tx + str(random.choice(1, 3))
    elif tx == "Ajdurian Raiders":
        return tx + str(random.choice(1, 3))
    elif tx == "Test2":
        return random.choice(testDict["Test2"])
    elif tx == "Test3":
        return random.choice(testDict["Test3"])

print (testfunction())
