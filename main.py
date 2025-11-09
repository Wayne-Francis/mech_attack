# this will be my main file for running the game - 

import sys
import random
from mech_type import *
from card_type import *
from utility_functions import *


def main():
    print("Welcome to Mech Attack")
    print("For this Demo, player will be a Tank")
    player_mech = Tank("player")
    player_mech.show_stats()
    print("Your opponent is the enemy Scout")
    ai_mech = Scout("ai")
    ai_mech.show_stats()
    print("For this demo battle by playing cards until one of you is destroyed")
    player_mech.create_starter_player_deck()
    player_mech.create_starter_hand()
    ai_mech.create_starter_player_deck()
    ai_mech.create_starter_hand()
    while True:
        play_turn(player_mech, ai_mech)
        print(player_mech.show_stats())
        print(ai_mech.show_stats())
        player_mech.draw_card()
        ai_mech.draw_card()
        if player_mech.hp <= 0:
            print("You are Destroyed, Try Again")
            break
        if ai_mech.hp <= 0:
            print("Victory!!")
            break

if __name__ == "__main__":
    main()