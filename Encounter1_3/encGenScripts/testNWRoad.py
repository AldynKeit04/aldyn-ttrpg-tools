import random
from regLists.NWRlist import *

result = random.choice(mainList)

def testfubnt():
    if "Commoner Party" in result:
        return random.choice(list(comDict.items()))
    else:
        return result

print(testfubnt())
