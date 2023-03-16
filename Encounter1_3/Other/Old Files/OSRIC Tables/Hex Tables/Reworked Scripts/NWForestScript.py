import random
import sys
def NWforest():
    x = ["Human Raiders", "4 Ajdurian Raiders", "3 Ajdurian Raiders", "Hostile Animals", "Hostile Animals",
         "Hostile Animals",
        "Passive Animals", "Passive Animals", "Passive Animals", "Passive Animals", "Passive Animals", "Passive Animals",
        "Passive Animals", "Passive Animals", "Hostile Animals", "Hostile Animals", "Hostile Animals",
        "3 Ajdurian Raiders",
        "4 Ajdurian Raiders", "Ajdurian Raiders"]
    y = ["Fox(es)", "Wolverine(s)", "Squirrel(s)", "Bird(s)", "Bird(s)", "Bird(s)", "Bird(s)", "Squirrel(s)", "Weasel(s)",
         "Passive Wolves"]
    z = ["Hungry Wolves", "Giant Rhino Beetle(s)", "Jackal(s)", "Boar(s)", "Lesser Bear(s)", "Giant Bee(s)",
         "Giant Frog(s)"]

    def main_roll():
        return random.choice(x)
    def secondary_roll():
        return random.choice(y)
    def tertiary_roll():
        return random.choice(z)

    def detail():
        if "Hostile Animals" in main_roll():
            return secondary_roll()
        elif "Passive Animals" in main_roll():
            return tertiary_roll()
        elif "Ajdurian Raiders" in main_roll():
            return "Ajdurian Raiders", random.randint(3, 8)
        elif "Human Raiders" in main_roll():
            return "Human Raiders", random.randint(3, 8)
        elif "4 Ajdurian Raiders" in main_roll() or "3 Ajdurian Raiders" in main_roll():
            return "Ajdurian Raiders", random.randint(3, 4)
        else:
            return "Error1"

    def amount():
        if "Wolverine(s)" or "Weasel(s)" or "Jackal(s)" or "Boar(s)" or "Giant Rhino Beetle(s)" in detail():
            return random.randint(1, 6)
        elif "Passive Wolves" or "Squirrel(s)" or "Giant Bee(s)" in detail():
            return random.randint(1, 10)
        elif "Birds" in detail():
            return random.randint(1, 20)
        elif "Hungry Wolves" in detail():
            return random.randint(3, 30)
        elif "Lesser Bear(s)" in detail():
            return random.randint(1, 2)
        elif "Giant Frog(s)" in detail():
            return random.randint(4, 11)
        elif "4 Ajdurian Raiders" in detail() or "3 Ajdurian Raiders" in detail():
            return None
        else:
            return "Error2"
    return detail(), amount()
while True:
    print(NWforest())


