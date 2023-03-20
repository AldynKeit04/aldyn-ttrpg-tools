import random

#This template is based on NWForest.

#This list is the first thing which the script goes over 
#in order to determine what is generated. There are multiple 
#of the same thing, because I don't know how else to weigh the 
#statistical chances of them.
mainList = ["Passive Animals", "Passive Animals",
        "Passive Animals", "Passive Animals", 
        "Passive Animals",
        "Human Raiders", "Ajdurian Raiders", 
        "Ajdurian Raiders",
        "Hostile Animals", "Hostile Animals"]

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
#There is no "Raider" list because there aren't any specific 
#types
#of raiders.

#This determines the actual encounter results themselves, 
#and type of animals.
def results():
    rand_dict = random.choice(mainList)
    if "Passive Animals" in rand_dict:
        return random.choice(list(passDict.items()))
    elif "Hostile Animals" in rand_dict:
        return random.choice(list(hostDict.items()))
    elif "Ajdurian Raiders" or "Human Raiders" in rand_dict:
        return rand_dict, random.randint(1, 3)

#This unpacks the data, so that it can be nice and stringy.
creature_type, creature_count = results()

#This, of course prints the data.
print(creature_count, creature_type)
