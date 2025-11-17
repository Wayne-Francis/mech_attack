# utility functions 

from mech_type import MechType
from card_type import CardType
from dice_roll import dice_roll

def resolve_card(user,opponent, card):
    if card.card_type == CardType.SHOOT:
        damage = dice_roll(4) + user.atk
        if not opponent.shielded:
            if user.name =="player":
                print(f"Player uses Shoot ---> {damage} damage done to enemy Mech")
            elif user.name =="ai":
                print(f"Enemy Mech uses Shoot ---> {damage} damage done to you")
            opponent.hp -= damage
        else:
            if opponent.mech_type == MechType.TANK:
                resolve_tank_shield_been_shot(opponent)
            else:
                opponent.shielded = False
                if opponent.name =="player":
                    print(f"Your shield is destroyed ---> You are vunerable to attack")
                elif opponent.name =="ai":
                    print(f"Enemy shield destroyed ---> Strike now!")
        if user.mech_type == MechType.GUNNER:
            if user.num_shots > 0:
                user.num_shots -= 1
                damage_2 = dice_roll(4) + user.atk
                if not opponent.shielded:
                    if user.name =="player":
                        print(f"Player double Shoots ---> {damage_2} damage done to enemy Mech")
                    elif user.name =="ai":
                        print(f"Enemy Mech uses Shoot ---> {damage_2} damage done to you")
                    opponent.hp -= damage_2
                else:
                    if opponent.mech_type == MechType.TANK:
                        resolve_tank_shield_been_shot(opponent)
                    else:
                        if opponent.name =="player":
                            print(f"Your shield is destroyed ---> You are vunerable to attack")
                        elif opponent.name =="ai":
                            print(f"Enemy shield destroyed ---> Strike now!")
                        opponent.shielded = False
            else:
                print(f"You are out of ammo -> gun reloaded for next attack")
                user.num_shots = 2
    elif card.card_type == CardType.SHIELD:
        if user.mech_type == MechType.TANK:
            if user.name =="player":
                print(f"You raise your Shields ---> You will absorb the next 2 attacks")
                user.shield_hp = 2
            elif user.name =="ai":
                print(f"Enemy raised shields ---> It will absorb the next 2 attacks!")
                user.shield_hp = 2
        elif user.mech_type != MechType.TANK:
            if user.name =="player":
                print(f"You raise your Shields ---> You will absorb the next attack")
            elif user.name =="ai":
                print(f"Enemy raised shields ---> It will absorb the next attack!")
        user.shielded = True
    elif card.card_type == CardType.REPAIR:
        user.hp += 3
        if user.hp > user.max_hp:
            user.hp = user.max_hp
        if user.mech_type == MechType.BOMBER:
            user.shielded = True
            print(f"You repair some of the damage ---> Your HP is now {user.hp} and you raise your shield")
        else:
            if user.name =="player":
                print(f"You repair some of the damage ---> Your HP is now {user.hp}")
            elif user.name =="ai":
                print(f"The enemy is repairing ---> Their HP is now {user.hp}")

def resolve_tank_shield_been_shot(opponent):
        if opponent.mech_type == MechType.TANK:
                opponent.shield_hp -= 1

                if opponent.name =="player":
                    print(f"Your shield takes a hit")
                else:
                    print(f"The enemy shield takes a hit")

                if opponent.shield_hp >= 1:
                    if opponent.name =="player":
                        print(f"Your shield can take 1 more hit")
                    else:
                        print(f"The enemy can take 1 more hit")
                       
                else:
                    opponent.shielded = False
                    opponent.shield_hp = 0
                    if opponent.name =="player":
                        print(f"Your shield is destroyed")
                    else:
                        print(f"The enemy shield is destroyed")
      


def play_turn(player_mech, ai_mech):
    player_card = player_mech.play_card()
    ai_card = ai_mech.ai_turn(player_mech)
    print(f"------\n{ai_mech.name}:{ai_card}")
    player_speed = dice_roll(4) + player_mech.spd
    ai_speed = dice_roll(4) + ai_mech.spd
    if player_speed >= ai_speed:
        print(f"----------\nYou outpace the enemy and go first")
        resolve_card(player_mech, ai_mech, player_card)
        if ai_mech.hp > 0:
            resolve_card(ai_mech, player_mech, ai_card)
    else:
        print(f"-----------\nThe enemy gets the drop on you")
        resolve_card(ai_mech, player_mech, ai_card)
        if player_mech.hp > 0:
            resolve_card(player_mech, ai_mech, player_card)

def choose_mech():
    while True:
        options = ["Tank", "Gunner", "Bomber"]
        input_message = "----------------\nChoose Your Mech:\n"
        for index, item in enumerate(options):
            input_message += f'{index+1}) {item}\n'
        user_input = input(input_message)
        if user_input.isnumeric():
            if int(user_input) <= len(options) and int(user_input) >= 1:
                break
    player_choice = int(user_input) 
    print(f'playing: {options[int(user_input) - 1]}')
    return player_choice

def battle_round(ai_mech,player_mech):
    turn = 1
    while player_mech.hp > 0 and ai_mech.hp >0:
        print(f"--------\nTurn {turn}")
        play_turn(player_mech, ai_mech)
        print(f"-------\nYou have {player_mech.hp} remaining")
        print(f"-------\nEnemy has {ai_mech.hp} remaining")
        if len(player_mech.shuffled_deck) < 1:
            player_mech.create_deck_from_discard()
        player_mech.draw_card()
        if len(ai_mech.shuffled_deck) < 1:
            ai_mech.create_deck_from_discard()
        ai_mech.draw_card()
        if player_mech.hp <= 0:
            print("You are Destroyed, Try Again")
            return False
        if ai_mech.hp <= 0:
            print(f"You have destroyed the enemy!")
            return True
        player_mech.show_deck()
        turn += 1
        print(
        "-------------------------------------------------------\n"
        "-------------------------------------------------------\n")



