# this will be my main file for running the game - 

import random
from mech_type import *
from card_type import *
from utility_functions import *
import pyfiglet


def main():
    #print("Welcome to Mech Attack")
    #print("Your goal is too destroy the enemey commander")
    #print("Please Choose a Mech")
    WIDTH = 100
    print("╔" + "═" * WIDTH + "╗")
    big_text = pyfiglet.figlet_format("Welcome to Mech Attack")
    bordered_line(big_text.center(WIDTH))
    bordered_line()
    mech_ascii = """\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⠦⢄⣠⡟⢁⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⡀⠀⠀⠀⠀⢹⣿⣿⣄⣤⣶⡒⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣀⠀⠹⣿⠿⣿⣦⡀⢀⡀⢛⣿⢿⣭⣿⣻⣿⣾⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⠖⠋⠀⣀⣼⣧⣼⣧⠀⢈⣹⣿⣶⣷⣾⣿⠀⠈⠻⣿⣿⣿⠟⢰⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣀⣠⣾⠛⠁⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣶⣦⠀⠹⡿⠷⠴⣿⣿⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣿⣿⣿⣷⣤⡴⠛⣹⣿⠿⣿⠟⠁⠀⠀⣸⣿⣿⣿⣿⣿⣾⣿⣿⣿⣦⣇⠀⠀⠘⣿⣦⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠉⢻⣿⣿⣿⣷⠞⠛⠁⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⣿⣿⣯⣽⣿⣿⡏⠀⣿⣿⣿⣿⡎⢠⣤⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠰⣿⡋⠙⠉⠏⠀⠀⠀⠀⠀⠀⠐⠗⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡟⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⣹⣿⡿⠻⣿⣿⣿⣿⠛⠟⠰⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠓⠀⠀⣰⠟⣽⠃⣹⠛⠉⠻⣶⣄⢹⠻⡿⣷⡀⠀⠀⠈⠙⠛⠛⠛⠛⠻⡿⠏⠈⠛⠙⠛⠿⢷⣶⣤⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⠀⠀⠀⣠⣿⡟⣏⠀⡟⠀⠀⢀⡿⣿⣾⠀⣰⣿⣃⣶⠦⠤⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠻⢷⣶⣤⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠖⠚⣿⣿⣸⣿⠀⠛⠳⢶⠞⣠⣿⣏⣰⣿⣿⣛⠻⣷⣄⠀⠻⡙⢦⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠶⣤⣿⣿⣿⣿⣿⣼⣧⣤⢀⡿⢿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣷⣦⠙⣦⣸⡷⣿⡆⠠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢁⣿⣿⣿⣿⣿⡿⣿⣿⣿⡿⠃⠈⠙⠛⠛⠿⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣄⣾⡟⠀⠈⠓⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠟⢩⣿⣿⡇⠁⢠⣿⣿⡿⠀⠀⠀⠀⠀⢠⣤⣶⣾⣿⣿⣿⢿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠏⠀⠈⢿⣿⣧⣴⣿⣿⣿⠇⠀⠀⡀⢀⣶⣼⣿⣿⣿⢿⣿⣿⣶⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠉⠀⠟⠀⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⠿⠟⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⣾⣿⣿⣿⣿⡟⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡅⠀⠀⠀⠀⠈⠙⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢹⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠐⠻⠿⠿⠿⠿⠿⠿⠿⠿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠶⠶⠾⠿⠿⡶⠲⠗⠒⠒⠒⠶⠶⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    for line in mech_ascii.splitlines():
        bordered_line(line)
    bordered_line()
    bordered_line("Pick A Mech".center(WIDTH))
    bordered_line()
    bordered_line(f"1) \033[1mTank\033[0m : HP:{MECH_TANK_HP}, ATTACK: {MECH_TANK_ATK}, SPEED {MECH_TANK_SPD}, Abilitie: Shield Takes 2 Hits To Break".center(WIDTH))
    bordered_line()
    bordered_line(f"2) \033[1mGunner\033[0m : HP:{MECH_GUNNER_HP}, ATTACK: {MECH_GUNNER_ATK}, SPEED {MECH_GUNNER_SPD}".center(WIDTH))
    bordered_line(f"Abilitie: Double shoot but must reload every 2 shoot actions (play a thrid shoot card to reload)".center(WIDTH))
    bordered_line()
    bordered_line(f"3) \033[1m Bomber \033[0m : HP:{MECH_BOMBER_HP}, ATTACK: {MECH_BOMBER_ATK}, SPEED {MECH_BOMBER_SPD}, Abilitie: Will Sheild when Repairing".center(WIDTH))
    bordered_line()
    print("╚" + "═" * WIDTH + "╝")
    player_choice = choose_mech()
    if player_choice == 1:
        player_mech = Tank("player")
    elif player_choice == 2:
        player_mech = Gunner("Player")
    else:
        player_mech = Bomber("Player")
    #print("A Scout Mech for the enemy forces approaches, destroy him before he betrays your position!")
    ai_mech_1 = Scout("ai")
    ai_mech_1.create_starter_player_deck()
    ai_mech_1.create_starter_hand()
    ai_mech_2 = Solider("ai")
    ai_mech_2.create_starter_player_deck()
    ai_mech_2.create_starter_hand()
    ai_mech_3 = Lieutenant("ai")
    ai_mech_3.create_starter_player_deck()
    ai_mech_3.create_starter_hand()
    ai_mech_4 = Captain("ai")
    ai_mech_4.create_starter_player_deck()
    ai_mech_4.create_starter_hand()
    ai_mech_5 = Commander("ai")
    ai_mech_5.create_starter_player_deck()
    ai_mech_5.create_starter_hand()
    ai_mech_list = [ai_mech_5, ai_mech_4, ai_mech_3, ai_mech_2, ai_mech_1]
    player_mech.create_starter_player_deck()
    player_mech.create_starter_hand()
    round = 1
    while player_mech.hp > 0:
        print(f"round {round}")
        ai_mech_this_turn = ai_mech_list.pop()
        ai_mech_list.remove(ai_mech_this_turn)
        print(player_mech.show_stats())
        print(ai_mech_this_turn.show_stats())
        result = battle_round(ai_mech_this_turn,player_mech)
        if result == False:
            print(f"Game over! You made it to round {round}")
            return
        player_mech.end_turn_sequence()
        ai_mech_this_turn.end_turn_sequence()
        player_mech.level_up()
        round += 1
        if round % 5 == 0:
            ai_mech_list = [ai_mech_5, ai_mech_4, ai_mech_3, ai_mech_2, ai_mech_1]
            for i in range(len(ai_mech_list)):
                ai_mech_list[i].ai_mech_upgrade()
        

        
####
    #print("Destroy the guard at the camp")
    #ai_mech = Solider("ai")
    #ai_mech.create_starter_player_deck()
    #ai_mech.create_starter_hand()
    #print(player_mech.show_stats())
    #print(ai_mech.show_stats())
    #result = battle_round(ai_mech,player_mech)
    #if result == False:
        #print("Game over!")
        #return
    #player_mech.end_turn_sequence()
    #player_mech.level_up()
    #print("Destroy the leader of the camp")
    #ai_mech = Lieutenant("ai")
    #ai_mech.create_starter_player_deck()
    #ai_mech.create_starter_hand()
    #print(player_mech.show_stats())
    #print(ai_mech.show_stats())
    #result = battle_round(ai_mech,player_mech)
    #if result == False:
        #print("Game over!")
        #return
    #player_mech.end_turn_sequence()
    #player_mech.level_up()
    #print("A dangerous captain defends his commander, destroy him!!")
    #ai_mech = Captain("ai")
    #ai_mech.create_starter_player_deck()
    #ai_mech.create_starter_hand()
    #print(player_mech.show_stats())
    #print(ai_mech.show_stats())
    #result = battle_round(ai_mech,player_mech)
    #if result == False:
        #print("Game over!")
        #return
    #player_mech.end_turn_sequence()
    #player_mech.level_up()
    #print("Finally the commander, finish this")
    #ai_mech = Commander("ai")
    #ai_mech.create_starter_player_deck()
    #ai_mech.create_starter_hand()
    #print(player_mech.show_stats())
    #print(ai_mech.show_stats())
    #result = battle_round(ai_mech,player_mech)
###

if __name__ == "__main__":
    main()