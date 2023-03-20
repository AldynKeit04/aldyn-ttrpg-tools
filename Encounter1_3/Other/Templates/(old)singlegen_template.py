import random

# This, as well as genresults are used to determine what exactly is rolled. In my North-West Forest generation script, it is
# replaced with an imported list.
TestList1 = ["AjdRaider", "HmnRaider", "Pig", "Goblin", "Blob", "Squirrel",
"Chicken", "Lamia"]

# used to determine how much is exactly generated. They are grouped based on what dice is used to roll them.
def genresults():
    result = random.choice(TestList1)
    if result in ["AjdRaider", "HmnRaider", "Lamia"]:
        return result, random.randint(1, 3) #1d3
    elif result in ["Pig", "Chicken", "Squirrel"]:
        return result, random.randint(3, 20) #Weird ass D20
    elif result in ["Goblin", "Blob"]:
        return result, random.randint(4, 10) #Weird ass D10
    else: return "error"

#obviously, prints the result of function 2
print(genresults())




