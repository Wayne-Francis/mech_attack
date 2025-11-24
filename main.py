# this will be my main file for running the game - 

import random
from mech_type import *
from card_type import *
from utility_functions import *


def main():
    #print("Welcome to Mech Attack")
    #print("Your goal is too destroy the enemey commander")
    #print("Please Choose a Mech")
    WIDTH = 100
    print("╔" + "═" * WIDTH + "╗")
    bordered_line("Welcome to Mech Attack".center(WIDTH))
    bordered_line()
    text = "The enemy has found your homebase, how many waves can you survive?".center(WIDTH)
    #slow_print(text, delay=0.05)
    bordered_line(text)
    bordered_line()
    text = "Both mechs choose an action, the mech with highest speed goes first".center(WIDTH)
    #slow_print(text, delay=0.05)
    bordered_line(text)
    bordered_line()
    text = "If you destroy a mech, upgrade! choose a stat to upgrade and a card to add to your deck".center(WIDTH)
    #slow_print(text, delay=0.05)
    bordered_line(text)
    bordered_line()
    text = "After each commander kill, the enemie mechs will get tougher!".center(WIDTH)
    #slow_print(text, delay=0.05)
    bordered_line(text)
    bordered_line()
    text = "Good luck Pilot".center(WIDTH)
    #slow_print(text, delay=0.05)
    bordered_line(text)
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
⠀⠐⠻⠿⠿⠿⠿⠿⠿⠿⠿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠶⠶⠾⠿⠿⡶⠲⠗⠒⠒⠒⠶⠶⠒⠒⠀⠀⠀
"""
    for line in mech_ascii.splitlines():
        bordered_line(line)
    bordered_line()
    bordered_line("Pick A Mech".center(WIDTH))
    bordered_line()
    bordered_line(f"1) Tank: HP:{MECH_TANK_HP}, ATTACK: {MECH_TANK_ATK}, SPEED {MECH_TANK_SPD}".center(WIDTH))
    bordered_line(f"Tank Ability: Shield Takes 2 Hits To Break".center(WIDTH))
    bordered_line()
    bordered_line(f"2) Gunner: HP:{MECH_GUNNER_HP}, ATTACK: {MECH_GUNNER_ATK}, SPEED {MECH_GUNNER_SPD}".center(WIDTH))
    bordered_line(f"Gunner Ability: Double shoot but must reload after each shot".center(WIDTH))
    bordered_line()
    bordered_line(f"3) Bomber: HP:{MECH_BOMBER_HP}, ATTACK: {MECH_BOMBER_ATK}, SPEED {MECH_BOMBER_SPD}".center(WIDTH))
    bordered_line(f"Bomber Ability: Will Sheild when Repairing".center(WIDTH))
    bordered_line()
    print("╚" + "═" * WIDTH + "╝")
    player_choice = choose_mech()
    if player_choice == 1:
        player_mech = Tank("player")
    elif player_choice == 2:
        player_mech = Gunner("Player")
    else:
        player_mech = Bomber("Player")
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
        ai_mech_this_turn = ai_mech_list.pop()
        print_battle_start_summary(player_mech, ai_mech_this_turn)
        result = battle_round(ai_mech_this_turn, player_mech)
        if result == False:
            print_end_summary(round)
            return  
        player_mech.end_turn_sequence()
        ai_mech_this_turn.end_turn_sequence()
        print_victory_summary()
        player_mech.level_up()
        round += 1
        if not ai_mech_list:
            ai_mech_list = [ai_mech_5, ai_mech_4, ai_mech_3, ai_mech_2, ai_mech_1]
            for i in range(len(ai_mech_list)):
                ai_mech_list[i].ai_mech_upgrade()

def run_game():
    while True:  
        main()  

if __name__ == "__main__":
    run_game()


#if __name__ == "__main__":
    #main()

        
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

