import time
import sys
from ImportNWForest import importfunction

print("Welcome to...")
for i in range(10):
    time.sleep(0.2)
    print("...")
print("Raziel's Scriptorium")

time.sleep(2)

for i in range(4):
    time.sleep(0.2)
    print(".")

username = input("What is your name?\n")
print("\nWelcome "+ username+".", " Here is the list of HexScripts\n")
print("Use the shorthanded name to the right of the colon.")
time.sleep(1)
print("--------------------")
print("North-West Forest Matrix: NWFM")
time.sleep(0.4)
print("North-West Forest Road Matrix: NWFRM")
time.sleep(0.4)
print("Failroads")
time.sleep(0.4)
print("Hallman")
print("--------------------")



while True:
    newvar = input()
    if "cum" in newvar or "Cum" in newvar or "penis" in newvar or "Penis" in newvar or "fuck" in newvar or "Fuck" in newvar or "dick" in newvar or "Dick" in newvar or "pussy" in newvar or "Pussy" in newvar:
        print("Die, fucker")
        time.sleep(1)
        sys.exit()
    elif newvar == "NWFM":
        print(importfunction())
        continue
    elif newvar == "exit":
        sys.exit()
    else: print("Invalid, please try again")


 # Notes/to do
 # Script currently return NWFM, but a new result isn't generated. NWFM probably needs to be reworked to be more efficient, and standardized similarily to the road matrix, but the
 # road matrix has its own problems (though not in direct functionality).
 # Functionality needs to be added to the other HexScripts.
 # A selector for HexScripts and Dungeon Scripts needs to be added. It could either be an initial selection of HexScript and DungeonScript categories, or
 # all selections but in their own category listed on the screen.
