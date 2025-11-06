# utility functions 

import random

def dice_roll(mech, dice):
    d4_dice = [1,2,3,4]
    d6_dice = [1,2,3,4,5,6]
    if dice == 4:
        result = random.choice(d4_dice)
        #print(f"rolling D4 .... {mech} rolled a {result}")
        return result
    if dice == 6:
        result = random.choice(d6_dice)
        #print(f"rolling D6 .... {mech} rolled a {result}")
        return result


