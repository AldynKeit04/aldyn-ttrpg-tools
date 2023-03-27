#use /n to put cli interface into one print function

#Python modules
import time
import random

#My modules
from encGenScripts.regLists import *
from encGenScripts import *
from encGenScripts.utils import *
#These modules import generation scripts and the lists needed for them to function

#Introduction and "sign in"
print("Welcome to...")
time.sleep(1)

for i in range(10):
    time.sleep(0.2)
    print("***************")
print("Aldyn's Scriptorium")
time.sleep(1)

#User "sign in"

print("What is your name?")

name = input()

print("Welcome "+name+".")
time.sleep(0.5)

#List of actual scripts

print("Here are the current scripts, use the shorthanded names to the right. \n")

print(
"""==================================
Random Encounter Generators
==================================
North-West Forest Encounters|NWFE
----------------------------------
North-West Road Encounters|NWRE
==================================
Utilities")
==================================
OSRIC Monster THAC0 Chart |OMTC
__________________________________
\n
Or, type exit to leave."""
)
#The following code is the actual mechanism for the user to retrieve generated encounters

while True:
    userinput = input()
    if userinput == "NWFE":
        NWcreatures, NWamount = NWForest.NWFresults()
        print(NWamount, NWcreatures)
        userinput = 0
        continue
    elif userinput == "NWRE":
        NWRcreatures, NWRamount = NWRoads.NWRresults()
        print(NWRamount, NWRcreatures)
        userinput = 0
        continue
    elif userinput == "exit":
        print("Goodbye")
        break
    elif userinput == "OMTC":
        print (monsterAtkMatrix.MatkMatrix)
