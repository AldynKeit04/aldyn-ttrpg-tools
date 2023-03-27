import random
from encGenScripts.regLists.NWRlist import *

#This determines the actual encounter results themselves, 
#and type of animals.
def NWRresults():
    rand_dict = random.choices(mainList, weights=(10, 10, 5, 10,
        15, 20, 30))
    if "Passive Animals" in rand_dict:
        return random.choice(list(passDict.items()))
    elif "Hostile Animals" in rand_dict:
        return random.choice(list(hostDict.items()))
    elif "Ajdurian Raiders" or "Human Raiders" in rand_dict:
        return rand_dict, random.randint(1, 3)
    elif "Commoner Party" in rand_dict:
        return random.choice(comDict)
