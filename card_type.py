# Use this file to define the class for card type 

from enum import Enum

class CardType(Enum):
   SHOOT = "Shoot"
   SHIELD = "Shield"
   REPAIR = "Repair"

class Card():
    def __init__(self, name:str, card_type: CardType):
        
        self.name = name
        self.card_type = card_type

    def __repr__(self):
        return f"Card(name={self.name!r}, card_type={self.card_type.name})"
    
    def __str__(self):
        return self.name

    
        
