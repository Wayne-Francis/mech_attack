from card_type import CardType, Card

def create_starter_player_deck():
    deck = []
    num_shoot_cards = 6
    num_shield_cards = 2
    num_repair_cards = 2
    for i in range(0, num_shoot_cards):
        shoot_card = Card("shoot", CardType.SHOOT)
        deck.append(shoot_card)
    for i in range(0, num_shield_cards):
        shield_card = Card("shield", CardType.SHIELD)
        deck.append(shield_card)
    for i in range(0, num_repair_cards):
        repair_card = Card("repair", CardType.REPAIR)
        deck.append(repair_card)
    return deck
