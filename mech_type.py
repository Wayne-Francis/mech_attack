# use this file to define the 3 mech type - starting with over all definitions 

from enum import Enum
from stat_blocks import *
from card_type import CardType, Card
import random
import sys 

class MechType(Enum):
   TANK = "tank"
   GUNNER = "gunner"
   BOMBER = "bomber"
   SCOUT = "scout"
   SOLIDER = "solider"
   LIEUTENANT = "lieutenant" 
   CAPTAIN = "captain"
   COMMANDER = "commander"


class Mech():
    def __init__(self, name:str):
        self.name = name
        self.deck = []
        self.shuffled_deck = []
        self.hand = []
        self.discard_pile = []
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
            shoot_card = Card("Shoot", CardType.SHOOT)
            self.deck.append(shoot_card)
        for i in range(num_shield_cards):
            shield_card = Card("Shield", CardType.SHIELD)
            self.deck.append(shield_card)
        for i in range(num_repair_cards):
            repair_card = Card("Repair", CardType.REPAIR)
            self.deck.append(repair_card)
        self.shuffle_deck()
        return self.shuffled_deck
    
    def shuffle_deck(self):
        self.shuffled_deck = []
        for i in range(len(self.deck)):
            if len(self.deck) > 0:
                result = random.choice(self.deck)
                self.deck.remove(result)
                self.shuffled_deck.append(result)
        return self.shuffled_deck
    
    def create_starter_hand(self):
        self.hand = []
        for i in range(START_HAND_SIZE):
                if len(self.shuffled_deck) > 0:
                    self.hand.append(self.shuffled_deck.pop())
        return self.hand
        
    def draw_card(self):
        self.hand.append(self.shuffled_deck.pop())
        return self.hand
    
    def show_hand(self):
        print(f"There are {len(self.hand)} cards in your hand:")
        for index, card in enumerate(self.hand, start=1):
            print(f"{index}. {card}")

    def play_card(self):
        while True:
            options = self.hand
            input_message = "Pick a card to play (please type a number):\n"
            for index, item in enumerate(options):
                input_message += f'{index+1}) {item}\n'
            user_input = input()
            if user_input.isnumeric():
                if int(user_input) <= len(options) and int(user_input) >= 1:
                    break
        card_choice = self.hand[int(user_input) - 1]
        print(f'playing: {card_choice}')
        self.hand.pop(int(user_input)-1)
        return card_choice
    


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

class Scout(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_SCOUT_HP
        self.atk = MECH_SCOUT_ATK
        self.spd = MECH_SCOUT_SPD
        self.mech_type = MechType.SCOUT

class Solider(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_SOLIDER_HP
        self.atk = MECH_SOLIDER_ATK
        self.spd = MECH_SOLIDER_SPD
        self.mech_type = MechType.SOLIDER

class Lieutenant(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_LIEUTENANT_HP
        self.atk = MECH_LIEUTENANT_ATK
        self.spd = MECH_LIEUTENANT_SPD
        self.mech_type = MechType.LIEUTENANT

class Captain(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_CAPTAIN_HP
        self.atk = MECH_CAPTAIN_ATK
        self.spd = MECH_CAPTAIN_SPD
        self.mech_type = MechType.CAPTAIN

class Commander(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_COMMANDER_HP
        self.atk = MECH_COMMANDER_ATK
        self.spd = MECH_COMMANDER_SPD
        self.mech_type = MechType.COMMANDER
     