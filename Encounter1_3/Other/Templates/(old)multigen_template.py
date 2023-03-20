import random

#This is mainly a test for a set of random generation scripts
#in my random generator project.


#Provides a base matrix for things to be chosen
Tlist1 = ["Test1", "Test2", "Test3"]

#The irl matrix has various sublists with things assigned to
#them. This is a way of simulating that.
testDict = {
        "Test1" : ["1Test", "2Test", "3Test"],
        "Test2" : ["21Test", "22Test", "23Test"],
        "Test3" : ["31Test", "32Test", "33Test"],}

def testfunction():
    tx = random.choice(Tlist1)
    if tx == "Test1":
        return random.choice(testDict["Test1"])
    elif tx == "Test2":
        return random.choice(testDict["Test2"])
    elif tx == "Test3":
        return random.choice(testDict["Test3"])

print (testfunction())
