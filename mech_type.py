# use this file to define the 3 mech type - starting with over all definitions 

from enum import Enum
from stat_blocks import *
from card_type import CardType, Card
import random
from dice_roll import dice_roll

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
        self.hp = 0
        self.atk = 0
        self.spd = 0
        self.max_hp = 0
        self.shielded = False
        self.level = 1

    def show_stats(self):
        return f"-------------\nYour Stats\nHP = {self.hp}\nCurrent Attack Power = {self.atk}\nCurrent Speed = {self.spd}\nLevel ={self.level}"

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
        copyied_deck = self.deck.copy()
        while copyied_deck: 
                result = random.choice(copyied_deck)
                copyied_deck.remove(result)
                self.shuffled_deck.append(result)
        return self.shuffled_deck
    
    def re_shuffle_deck(self):
        copy_deck = self.shuffled_deck.copy()
        self.shuffled_deck.clear()
        while copy_deck:
                result = random.choice(copy_deck)
                copy_deck.remove(result)
                self.shuffled_deck.append(result)
        return self.shuffled_deck
    
    def create_starter_hand(self):
        self.hand = []
        for i in range(START_HAND_SIZE):
                if len(self.shuffled_deck) > 0:
                    self.hand.append(self.shuffled_deck.pop())
        return self.hand
        
    def draw_card(self):
        if len(self.shuffled_deck) < 1:
            self.create_deck_from_discard()
        card = self.shuffled_deck.pop()
        self.hand.append(card)
        return self.hand
    
    def show_hand(self):
        print(f"-----------------\nThere are {len(self.hand)} cards in your hand:")
        for index, card in enumerate(self.hand, start=1):
            print(f"{index}. {card}")

    def show_deck(self):
        print(f"-----------------\nThere are {len(self.shuffled_deck)} cards in your deck:")
        for index, card in enumerate(self.shuffled_deck, start=1):
            print(f"{index}. {card}")

    def play_card(self):
        while True:
            options = self.hand
            input_message = "----------------\nChoose An Action Card to Play:\n"
            for index, item in enumerate(options):
                input_message += f'{index+1}) {item}\n'
            user_input = input(input_message)
            if user_input.isnumeric():
                if int(user_input) <= len(options) and int(user_input) >= 1:
                    break
        card_choice = self.hand[int(user_input) - 1]
        print(f'playing: {card_choice}')
        self.discard_pile.append(self.hand.pop(int(user_input)-1))
        return card_choice
    
    def create_deck_from_discard(self):
        if self.discard_pile:
            self.shuffled_deck.extend(self.discard_pile)
        self.discard_pile.clear()
        self.re_shuffle_deck()
        return self.shuffled_deck
    
    def ai_card_choice(self, desired_card):
        for i, card in enumerate(self.hand):
            if card.card_type == desired_card:
                return self.hand.pop(i)
        return None

    def ai_turn(self, player_mech):
        if self.hp == self.max_hp:
            card_choice = self.ai_card_choice(CardType.SHOOT)
            if card_choice == None:
                card_choice = self.ai_card_choice(CardType.SHIELD)
                if card_choice == None:
                    card_choice = random.choice(self.hand)
                    self.hand.remove(card_choice)
            self.discard_pile.append(card_choice)   
            return card_choice 
        
        elif self.hp < (0.25 * self.max_hp):
            result = dice_roll(100)
            if result > 40:
                card_choice = self.ai_card_choice(CardType.REPAIR)
                if card_choice == None:
                    card_choice = self.ai_card_choice(CardType.SHIELD)
                    if card_choice == None:
                        card_choice = random.choice(self.hand)
                        self.hand.remove(card_choice)
                self.discard_pile.append(card_choice)
                return card_choice
            card_choice = random.choice(self.hand)
            self.hand.remove(card_choice)
            self.discard_pile.append(card_choice)
            return card_choice
        
        elif player_mech.shielded == True:
            result = dice_roll(100)
            if result > 40:
                card_choice = self.ai_card_choice(CardType.REPAIR)
                if card_choice == None:
                    card_choice = self.ai_card_choice(CardType.SHIELD)
                    if card_choice == None:
                        card_choice = random.choice(self.hand)
                        self.hand.remove(card_choice)
                self.discard_pile.append(card_choice)
                return card_choice  
            card_choice = random.choice(self.hand)
            self.hand.remove(card_choice)
            self.discard_pile.append(card_choice)
            return card_choice
        
        else:
            result = dice_roll(100)
            if result > 70:
                card_choice = self.ai_card_choice(CardType.SHIELD)
                if card_choice == None:
                    card_choice = random.choice(self.hand)
                    self.hand.remove(card_choice)
                self.discard_pile.append(card_choice)
                return card_choice  
            else:
                card_choice = self.ai_card_choice(CardType.SHOOT)
                if card_choice == None:
                    card_choice = random.choice(self.hand)
                    self.hand.remove(card_choice)
                self.discard_pile.append(card_choice)
                return card_choice

    def level_up(self):
        print("You have leveled up")
        while True:
            options = ["HP","ATK","SPD"]
            input_message = "-----------------\nPick a Stat to Improve\n"
            for index, item in enumerate(options):
                input_message += f'{index+1}) {item}\n'
            user_input = input(input_message)
            if user_input.isnumeric():
                if int(user_input) <= len(options) and int(user_input) >= 1:
                    break
        stat_choice = int(user_input) 
        print(f'You picked: {options[int(user_input) - 1]}')
        if stat_choice == 1:
            self.max_hp += 3
            self.hp = self.max_hp
        elif stat_choice == 2:
            self.atk += 1
        else:
            self.spd += 1
        while True:
            options = ["Shoot","Shield","Repair"]
            input_message = "-----------------\nPick a card to add to your deck\n"
            for index, item in enumerate(options):
                input_message += f'{index+1}) {item}\n'
            user_input = input(input_message)
            if user_input.isnumeric():
                if int(user_input) <= len(options) and int(user_input) >= 1:
                    break
        card_choice = int(user_input)
        if card_choice == 1:
            shoot_card = Card("Shoot", CardType.SHOOT)
            self.deck.append(shoot_card)
        elif card_choice == 2:
            shield_card = Card("Shield", CardType.SHIELD)
            self.deck.append(shield_card)
        else:
            repair_card = Card("Repair", CardType.REPAIR)
            self.deck.append(repair_card)
        print(f'You picked: {options[int(user_input) - 1]}')
        self.level += 1
        self.shuffle_deck()
    
    def end_turn_sequence(self):
        #if self.discard_pile:
            #self.shuffled_deck.extend(self.discard_pile)
        self.shuffled_deck.clear()
        self.discard_pile.clear()
        self.hand.clear()
        self.shuffle_deck()
        self.create_starter_hand()
        self.hp = self.max_hp
        self.shielded = False
        return self.shuffled_deck
    
    def ai_mech_upgrade(self):
        options = ["HP", "ATK", "SPD"]
        choice_1 = random.choice(options)
        if choice_1 == "HP":
            self.hp = self.hp * 1.25
            self.max_hp = self.hp
        if choice_1 == "ATK":
            self.atk = self.atk * 1.25
        if choice_1 == "SPD":
            self.spd = self.spd * 1.25
        choice_2 = random.choice(options)
        if choice_2 == "HP":
            self.hp = self.hp * 1.25
            self.max_hp = self.hp
        if choice_2 == "ATK":
            self.atk = self.atk * 1.25
        if choice_2 == "SPD":
            self.spd = self.spd * 1.25

class Tank(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_TANK_HP
        self.max_hp = MECH_TANK_HP
        self.atk = MECH_TANK_ATK
        self.spd = MECH_TANK_SPD
        self.mech_type = MechType.TANK
        self.shield_hp = 2

class Gunner(Mech):
    def __init__(self, name:str):
        super().__init__(name)
       
        self.hp = MECH_GUNNER_HP
        self.max_hp = MECH_GUNNER_HP
        self.atk = MECH_GUNNER_ATK
        self.spd = MECH_GUNNER_SPD
        self.mech_type = MechType.GUNNER
        self.num_shots = 2

class Bomber(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_BOMBER_HP
        self.max_hp = MECH_BOMBER_HP
        self.atk = MECH_BOMBER_ATK
        self.spd = MECH_BOMBER_SPD
        self.mech_type = MechType.BOMBER

class Scout(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_SCOUT_HP
        self.max_hp = MECH_SCOUT_HP
        self.atk = MECH_SCOUT_ATK
        self.spd = MECH_SCOUT_SPD
        self.mech_type = MechType.SCOUT

    def show_stats(self):
        return f"-------------\nScout Stats\nHP = {self.hp}\nCurrent Attack Power = {self.atk}\nCurrent Speed = {self.spd}"

class Solider(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_SOLIDER_HP
        self.max_hp = MECH_SOLIDER_HP
        self.atk = MECH_SOLIDER_ATK
        self.spd = MECH_SOLIDER_SPD
        self.mech_type = MechType.SOLIDER

    def show_stats(self):
        return f"-------------\nSolider Stats\nHP = {self.hp}\nCurrent Attack Power = {self.atk}\nCurrent Speed = {self.spd}"

class Lieutenant(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_LIEUTENANT_HP
        self.max_hp = MECH_LIEUTENANT_HP
        self.atk = MECH_LIEUTENANT_ATK
        self.spd = MECH_LIEUTENANT_SPD
        self.mech_type = MechType.LIEUTENANT

    def show_stats(self):
        return f"-------------\nLieutenant Stats\nHP = {self.hp}\nCurrent Attack Power = {self.atk}\nCurrent Speed = {self.spd}"

class Captain(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_CAPTAIN_HP
        self.max_hp = MECH_CAPTAIN_HP
        self.atk = MECH_CAPTAIN_ATK
        self.spd = MECH_CAPTAIN_SPD
        self.mech_type = MechType.CAPTAIN

    def show_stats(self):
        return f"-------------\nCaptain Stats\nHP = {self.hp}\nCurrent Attack Power = {self.atk}\nCurrent Speed = {self.spd}"

class Commander(Mech):
    def __init__(self, name:str):
        super().__init__(name)

        self.hp = MECH_COMMANDER_HP
        self.max_hp = MECH_COMMANDER_HP
        self.atk = MECH_COMMANDER_ATK
        self.spd = MECH_COMMANDER_SPD
        self.mech_type = MechType.COMMANDER
    
    def show_stats(self):
        return f"-------------\nCommander Stats\nHP = {self.hp}\nCurrent Attack Power = {self.atk}\nCurrent Speed = {self.spd}"
     