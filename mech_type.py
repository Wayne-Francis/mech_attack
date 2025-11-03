# use this file to define the 3 mech type - starting with over all definitions 

from enum import Enum
from stat_blocks import *
from card_type import CardType, Card
import random

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
        self.deck = []
        self.hand = []
        self.mech_type = "Generic"

    def show_stats(self):
        return f"HP = {self.hp}\nCurrent Attack Power = {self.atk}\nCurrent Speed = {self.spd}"

    def __repr__(self):
        return f"Mech={self.mech_type},name={self.name!r}"
    
    def create_starter_player_deck(self):
        self.deck = []
        num_shoot_cards = STARTING_SHOOT_CARDS
        num_shield_cards = STARTING_SHIELD_CARDS
        num_repair_cards = STARTING_REPAIR_CARDS
        for i in range(num_shoot_cards):
            shoot_card = Card("shoot", CardType.SHOOT)
            self.deck.append(shoot_card)
        for i in range(num_shield_cards):
            shield_card = Card("shield", CardType.SHIELD)
            self.deck.append(shield_card)
        for i in range(num_repair_cards):
            repair_card = Card("repair", CardType.REPAIR)
            self.deck.append(repair_card)
        return self.deck
    
    def create_starter_hand(self):
        self.hand = []
        for i in range(START_HAND_SIZE):
            self.hand.append(self.deck.pop())
        return self.hand
    
    def shuffle_deck(self):
        self.shuffled_deck = []
        for i in range(len(self.deck)):
            if len(self.deck) > 0:
                result = random.choice(self.deck)
                self.deck.remove(result)
                self.shuffled_deck.append(result)
        return self.shuffled_deck
        
    def draw_card(self):
        self.hand.append(self.deck.pop())
        return self.hand
    
class Tank(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_TANK_HP
        self.atk = MECH_TANK_ATK
        self.spd = MECH_TANK_SPD
        self.mech_type = MechType.TANK

class Gunner(Mech):
    def __init__(self, name:str):
        super().__init__(name)
       
        self.hp = MECH_GUNNER_HP
        self.atk = MECH_GUNNER_ATK
        self.spd = MECH_GUNNER_SPD
        self.mech_type = MechType.GUNNER

class Bomber(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_BOMBER_HP
        self.atk = MECH_BOMBER_ATK
        self.spd = MECH_BOMBER_SPD
        self.mech_type = MechType.BOMBER
     