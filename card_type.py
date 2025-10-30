# Use this file to define the class for card type 

from enum import Enum

class CardType(Enum):
   SHOOT = "shoot"
   SHIELD = "shield"
   REPAIR = "repair"

class Card():
    def __init__(self, name:str, card_type: CardType):
        
        self.name = name
        self.card_type = card_type

    def __repr__(self):
        return f"Card(name={self.name!r}, card_type={self.card_type.name})"

    
        
