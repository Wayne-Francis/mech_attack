# use this file to define the 3 mech type - starting with over all definitions 

from enum import Enum
from stat_blocks import *
from card_type import CardType, Card

class MechType(Enum):
   TANK = "tank"
   GUNNER = "gunner"
   BOMBER = "bomber"
   SCOUT = "scout"
   SOLIDER = "solider"
   LIEUTENANT = "lieutenant" 
   CAPTAIN = "captain"
   COMMANDER = "commander"
   GENERAl = "general"


class Mech():
    def __init__(self, name:str):
        
        self.name = name

    def show_stats(self):
        print(f"HP = {self.hp}\nCurrent Attack Power = {self.atk}\nCurrent Speed = {self.spd}")

    def __repr__(self):
        return f"Mech(name={self.name!r})"
    
    def create_starter_player_deck(self):
        deck = []
        num_shoot_cards = STARTING_SHOOT_CARDS
        num_shield_cards = STARTING_SHIELD_CARDS
        num_repair_cards = STARTING_REPAIR_CARDS
        for i in range(num_shoot_cards):
            shoot_card = Card("shoot", CardType.SHOOT)
            deck.append(shoot_card)
        for i in range(num_shield_cards):
            shield_card = Card("shield", CardType.SHIELD)
            deck.append(shield_card)
        for i in range(num_repair_cards):
            repair_card = Card("repair", CardType.REPAIR)
            deck.append(repair_card)
        return deck
    
    def create_starter_hand(self,deck):
        hand = []
        for i in range(START_HAND_SIZE):
            hand.append(deck.pop())
        return hand
    
    def draw_card(self,hand,deck):
        hand.append(deck.pop())
        return hand 
    
class Tank(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_TANK_HP
        self.atk = MECH_TANK_ATK
        self.spd = MECH_TANK_SPD

class Gunner(Mech):
    def __init__(self, name:str):
        super().__init__(name)
       
        self.hp = MECH_GUNNER_HP
        self.atk = MECH_GUNNER_ATK
        self.spd = MECH_GUNNER_SPD

class Bomber(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_BOMBER_HP
        self.atk = MECH_BOMBER_ATK
        self.spd = MECH_BOMBER_SPD
     