import random

#This list is the first thing which the script goes over. This list used
#to have many more items in them, however I learned how to better weigh
#things with random.choices rather than random.choice.
mainList = ["Passive Animals",
        "Human Raiders", "Ajdurian Raiders", 
        "Hostile Animals"]

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

