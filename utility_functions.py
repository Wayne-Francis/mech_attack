# utility functions 

import random
from mech_type import *
from card_type import *

def dice_roll(dice):
    if dice == 4:
        #print(f"rolling D4 .... {mech} rolled a {result}")
        return random.choice(range(1,5))
    if dice == 6:
        #print(f"rolling D6 .... {mech} rolled a {result}")
        return random.choice(range(1,7))
    if dice == 100:
        return random.choice(range(1,101))


def resolve_card(user,opponent, card):
    if card.card_type == CardType.SHOOT:
        damage = dice_roll(6) + user.atk
        if not opponent.shielded:
            opponent.hp -= damage
    elif card.card_type == CardType.SHIELD:
        user.shielded = True
    elif card.card_type == CardType.REPAIR:
        user.hp += 3
        if user.hp > user.max_hp:
            user.hp = user.max_hp

def play_turn(player_mech, ai_mech):
    player_card = player_mech.play_card()
    ai_card = ai_mech.ai_turn(player_mech)
    print(f"AI picked: {ai_card}")
    player_speed = dice_roll(4) + player_mech.spd
    ai_speed = dice_roll(4) + ai_mech.spd
    if player_speed >= ai_speed:
        resolve_card(player_mech, ai_mech, player_card)
        resolve_card(ai_mech, player_mech, ai_card)
    else:
        resolve_card(ai_mech, player_mech, ai_card)
        resolve_card(player_mech, ai_mech, player_card)



