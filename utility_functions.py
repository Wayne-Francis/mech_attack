# utility functions 

from mech_type import MechType
from card_type import CardType
from dice_roll import dice_roll
import sys, time
from stat_blocks import *
import os


### this is the old version of the resolve_card function, it worked but was very confusing to update - worked with AI to clean it up!
#def resolve_card(user,opponent, card):
    #if card.card_type == CardType.SHOOT:
        #damage = dice_roll(4) + user.atk
        #if not opponent.shielded:
            #if user.name =="player":
                #print(f"Player uses Shoot ---> {damage} damage done to enemy Mech")
           # elif user.name =="ai":
                #print(f"Enemy Mech uses Shoot ---> {damage} damage done to you")
            #opponent.hp -= damage
        #else:
            #if opponent.mech_type == MechType.TANK:
                #resolve_tank_shield_been_shot(opponent)
            #else:
                #opponent.shielded = False
                #if opponent.name =="player":
                    #print(f"Your shield is destroyed ---> You are vunerable to attack")
                #elif opponent.name =="ai":
                    #print(f"Enemy shield destroyed ---> Strike now!")
        #if user.mech_type == MechType.GUNNER:
            #if user.num_shots > 0:
                #user.num_shots -= 2
                #damage_2 = dice_roll(4) + user.atk
                #if not opponent.shielded:
                    #if user.name =="player":
                        #print(f"Player double Shoots ---> {damage_2} damage done to enemy Mech")
                   # elif user.name =="ai":
                        #print(f"Enemy Mech uses Shoot ---> {damage_2} damage done to you")
                   # opponent.hp -= damage_2
                #else:
                    #if opponent.mech_type == MechType.TANK:
                        #resolve_tank_shield_been_shot(opponent)
                   # else:
                       # if opponent.name =="player":
                           # print(f"Your shield is destroyed ---> You are vunerable to attack")
                       # elif opponent.name =="ai":
                           # print(f"Enemy shield destroyed ---> Strike now!")
                       # opponent.shielded = False
            #else:
                #print(f"You are out of ammo -> gun reloaded for next attack")
                #user.num_shots = 2
   # elif card.card_type == CardType.SHIELD:
        #if user.mech_type == MechType.TANK:
            #if user.name =="player":
               # print(f"You raise your Shields ---> You will absorb the next 2 attacks")
                #user.shield_hp = 2
            #elif user.name =="ai":
               # print(f"Enemy raised shields ---> It will absorb the next 2 attacks!")
               # user.shield_hp = 2
        #elif user.mech_type != MechType.TANK:
           # if user.name =="player":
               # print(f"You raise your Shields ---> You will absorb the next attack")
           # elif user.name =="ai":
               # print(f"Enemy raised shields ---> It will absorb the next attack!")
        #user.shielded = True
    #elif card.card_type == CardType.REPAIR:
        #user.hp += 3
        #if user.hp > user.max_hp:
           # user.hp = user.max_hp
       # if user.mech_type == MechType.BOMBER:
           # user.shielded = True
           # print(f"You repair some of the damage ---> Your HP is now {user.hp} and you raise your shield")
       # else:
           # if user.name =="player":
              #  print(f"You repair some of the damage ---> Your HP is now {user.hp}")
           # elif user.name =="ai":
              #  print(f"The enemy is repairing ---> Their HP is now {user.hp}")

## this is version 2 
def resolve_card(user, opponent, card):
    log = [] ## Record all messages instead of printing straight away , unlike V1 resolve card

## Shoot Logic

    if card.card_type == CardType.SHOOT:


        shooter = "Player" if getattr(user, "is_player", False) else "Enemy" ### Ai gave me this fix

        def apply_shot(dmg, label):

            if not opponent.shielded:
                opponent.hp -= dmg
                log.append(f"{label} → {dmg} damage dealt")
            else:
                if opponent.mech_type == MechType.TANK:
                    resolve_tank_shield_been_shot(opponent)
                    if opponent.shielded:
                        log.append(f"{label} → Tank shield absorbs the hit ({opponent.shield_hp} hits left)")
                    else:
                        log.append(f"{label} → Tank shield breaks!")
                else:
                    opponent.shielded = False
                    log.append(f"{label} → Shield destroyed!")

        if user.mech_type == MechType.GUNNER:
        # If out of ammo → reload only
            if user.num_shots == 0:
                user.num_shots = 2
                log.append(f"{shooter} reloads their weapon")
                return log
            for i in range(2):
                dmg = dice_roll(4) + user.atk
                apply_shot(dmg, f"{shooter} fires shot {i+1}")
            user.num_shots = 0
            return log
        dmg = dice_roll(4) + user.atk
        apply_shot(dmg, f"{shooter} fires")
        return log
    
## Shield Logic 

    elif card.card_type == CardType.SHIELD:
        user.shielded = True

        if user.mech_type == MechType.TANK:
            user.shield_hp = 2
            msg = "Tank raises a heavy shield (2 hits)"
        else:
            msg = "Shield raised (1 hit)"
        log.append(msg)

## Repair logic

    elif card.card_type == CardType.REPAIR:
        user.hp = min(user.hp + 3, user.max_hp)

        if user.mech_type == MechType.BOMBER:
            user.shielded = True
            log.append(f"Repaired to {user.hp} and raised a shield (Bomber ability)")
        else:
            log.append(f"Repaired → HP is now {user.hp}")

    return log

def print_summary(player_log, ai_log, player, ai, acted_first):
    WIDTH = 70
    print("\n" + "─" * WIDTH)
    print("ACTION SUMMARY".center(WIDTH))
    print("─" * WIDTH)
    print(f"Turn Order: {acted_first} acted first!")
    print("─" * WIDTH)

    print("\nPlayer:")
    for msg in player_log:
        print(f"  • {msg}")

    print("\nEnemy:")
    for msg in ai_log:
        print(f"  • {msg}")

    print("\n" + "-" * WIDTH)

    print(f"Your HP:  {player.hp}/{player.max_hp}   | Shield: {player.shielded} "
          f"| Ammo: {player.num_shots if player.mech_type == MechType.GUNNER else '-'}")
    print(f"Enemy HP: {ai.hp}/{ai.max_hp}         | Shield: {ai.shielded}")

    input(" Press Enter to continue to Continue")

    print("─" * WIDTH + "\n")

def print_battle_start_summary(player, ai):
    WIDTH = 70
    print("\n" + "═" * WIDTH)
    print("⚔️  BATTLE START  ⚔️".center(WIDTH))
    print("═" * WIDTH + "\n")

    ai_type_name = ai.mech_type.name.capitalize()
    print(f"⚠️  Prepare! the {ai_type_name} is about to attack!\n")

    print("Your Mech Stats".center(WIDTH, "-"))
    print(f"  HP:     {player.hp}/{player.max_hp}")
    print(f"  Attack: {player.atk}")
    print(f"  Speed:  {player.spd}\n")

    print(f"{ai_type_name} Stats".center(WIDTH, "-"))
    print(f"  HP:     {ai.hp}/{ai.max_hp}")
    print(f"  Attack: {ai.atk}")
    print(f"  Speed:  {ai.spd}\n")

    input("Press ENTER to engage...")

    print("═" * WIDTH + "\n")

def print_victory_summary():
    WIDTH = 70
    print("\n" + "═" * WIDTH)
    print("🎺  Victory  🎺".center(WIDTH))
    print("═" * WIDTH + "\n")
    print(f"You have destroyed the enemy Mech\n")
    print(f"It looks like you can upgrade your Mech\n")

    input("Press ENTER to upgrade")

    print("═" * WIDTH + "\n")

def resolve_tank_shield_been_shot(opponent):
    if opponent.mech_type == MechType.TANK:
        opponent.shield_hp -= 1
        if opponent.shield_hp <= 0:
            opponent.shielded = False
            opponent.shield_hp = 0  
    else:
        opponent.shielded = False
        opponent.shield_hp = 0
      


def play_turn(player_mech, ai_mech):
    player_card = player_mech.play_card()
    ai_card = ai_mech.ai_turn(player_mech)
    #print(f"------\n{ai_mech.name}:{ai_card}")
    player_speed = dice_roll(4) + player_mech.spd
    ai_speed = dice_roll(4) + ai_mech.spd
    acted_first = "Player" if player_speed >= ai_speed else "Enemy"
    player_log = []
    ai_log = []
    if  acted_first == "Player":
        #print(f"----------\nYou outpace the enemy and go first")
        player_log = resolve_card(player_mech, ai_mech, player_card)
        if ai_mech.hp > 0:
            ai_log = resolve_card(ai_mech, player_mech, ai_card)
    else:
        #print(f"-----------\nThe enemy gets the drop on you")
        ai_log = resolve_card(ai_mech, player_mech, ai_card)
        if player_mech.hp > 0:
            player_log = resolve_card(player_mech, ai_mech, player_card)

    print_summary(player_log, ai_log, player_mech, ai_mech, acted_first)

def choose_mech():
    while True:
        options = [f"Tank: HP:{MECH_TANK_HP}, ATTACK: {MECH_TANK_ATK}, SPEED {MECH_TANK_SPD}, 🛡️ Takes 2 Hits To Break", 
                   f"Gunner: HP:{MECH_GUNNER_HP}, ATTACK: {MECH_GUNNER_ATK}, SPEED {MECH_GUNNER_SPD}, Double 🔫 but must reload every 2 shoot actions (play a thrid shoot card to reload)", 
                   f"Bomber: HP:{MECH_BOMBER_HP}, ATTACK: {MECH_BOMBER_ATK}, SPEED {MECH_BOMBER_SPD}, Will 🛡️ when 🔨"]
        #input_message = "----------------\nChoose Your Mech:\n"
        #for index, item in enumerate(options):
            #input_message += f'{index+1}) {item}\n'
        user_input = input()
        if user_input.isnumeric():
            if int(user_input) <= len(options) and int(user_input) >= 1:
                break
    player_choice = int(user_input) 
    #print(f'You picked {options[int(user_input) - 1]}')
    return player_choice

def battle_round(ai_mech,player_mech):
    turn = 1
    while player_mech.hp > 0 and ai_mech.hp >0:
        #print(f"--------\nTurn {turn}")
        play_turn(player_mech, ai_mech)
        #print(f"-------\nYou have {player_mech.hp} remaining")
        #print(f"-------\nEnemy has {ai_mech.hp} remaining")
        if len(player_mech.shuffled_deck) < 1:
            player_mech.create_deck_from_discard()
        player_mech.draw_card()
        if len(ai_mech.shuffled_deck) < 1:
            ai_mech.create_deck_from_discard()
        ai_mech.draw_card()
        if player_mech.hp <= 0:
            #print("You are Destroyed, Try Again")
            return False
        if ai_mech.hp <= 0:
            #print(f"You have destroyed the enemy!")
            return True
        #player_mech.show_deck() I added this line for debugging 
        turn += 1
        #print(
        #"-------------------------------------------------------\n"
        #"-------------------------------------------------------\n")

def bordered_line(text=""):
    WIDTH = 100
    text = text[:WIDTH]  
    padded = text + " " * (WIDTH - len(text))
    print(f"║{padded}║")

def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_end_summary(round):
    WIDTH = 70
    print("\n" + "─" * WIDTH)
    print(" DEFEAT ".center(WIDTH))
    print("─" * WIDTH)

    print("\nYour cockpit goes dark...")
    print("Warning lights flicker... then fade.")
    print("Metal groans as your mech collapses beneath you.\n")

    print(f"You held off {round} enemys while defending your home.\n")

    choice = input("PRESS ENTER TO REDEPLOY or Q TO QUIT: ").strip().lower()
    if choice == "q":
        print("Quitting... Thanks for playing!")
        exit()  # stops the Python program

    print("─" * WIDTH + "\n")
    clear()
    return True



def clear():
    os.system("cls" if os.name == "nt" else "clear")



