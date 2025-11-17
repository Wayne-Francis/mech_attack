import random

def dice_roll(dice):
    if dice == 4:
        #print(f"rolling D4 .... {mech} rolled a {result}")
        return random.choice(range(1,5))
    if dice == 6:
        #print(f"rolling D6 .... {mech} rolled a {result}")
        return random.choice(range(1,7))
    if dice == 100:
        return random.choice(range(1,101))
