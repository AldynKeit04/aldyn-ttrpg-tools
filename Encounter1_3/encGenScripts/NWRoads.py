import random
from regLists.NWRlist import *

#This determines the actual encounter results themselves, 
#and type of animals.
def NWRresults():
    rand_dict = random.choice(mainList)
    if "Passive Animals" in rand_dict:
        return random.choice(list(passDict.items()))
    elif "Hostile Animals" in rand_dict:
        return random.choice(list(hostDict.items()))
    elif "Ajdurian Raiders" or "Human Raiders" in rand_dict:
        return rand_dict, random.randint(1, 3)
    elif "Commoner Party" in rand_dict:
        return random.choice(comDict)


print (NWRresults())

