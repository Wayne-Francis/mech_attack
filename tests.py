import unittest
from card_type import Card, CardType
from mech_type import *
from utility_functions import dice_roll
import random

class TestDeckCreation(unittest.TestCase):
    def test_deck_counts(self):
        player_mech = Tank("player")
        deck = player_mech.create_starter_player_deck()
        self.assertEqual(len(deck), 10)
        self.assertEqual(sum(c.card_type == CardType.SHOOT for c in deck), 6)
        self.assertEqual(sum(c.card_type == CardType.SHIELD for c in deck), 2)
        self.assertEqual(sum(c.card_type == CardType.REPAIR for c in deck), 2)

    def test_new_Tank_mech(self):
        player_mech = Tank("player")
        self.assertEqual(repr(player_mech), "Mech=MechType.TANK,name='player'")
        self.assertEqual(player_mech.mech_type, MechType.TANK)

    def test_new_Gunner_mech(self):
        player_mech = Gunner("player")
        self.assertEqual(repr(player_mech), "Mech=MechType.GUNNER,name='player'")
        self.assertEqual(player_mech.mech_type, MechType.GUNNER)

    def test_new_Bomber_mech(self):
        player_mech = Bomber("player")
        self.assertEqual(repr(player_mech), "Mech=MechType.BOMBER,name='player'")
        self.assertEqual(player_mech.mech_type, MechType.BOMBER)

    def test_show_stats(self):
        player_mech = Gunner("player")
        self.assertEqual(player_mech.show_stats(), "HP = 12\nCurrent Attack Power = 1\nCurrent Speed = 3")

    def test_starter_hand(self):
        player_mech = Tank("player")
        deck = player_mech.create_starter_player_deck()
        hand = player_mech.create_starter_hand()
        self.assertEqual(len(hand), 3)

    def test_draw_card(self):
        player_mech = Tank("player")
        deck = player_mech.create_starter_player_deck()
        hand = player_mech.create_starter_hand()
        hand = player_mech.draw_card()
        self.assertEqual(len(hand), 4)

    
    def test_d4_range(self):
        # Roll a D4 multiple times to check the range
        for _ in range(100):
            result = dice_roll("Player", 4)
            self.assertIsInstance(result, int)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 4)

    def test_d6_range(self):
        # Roll a D6 multiple times to check the range
        for _ in range(100):
            result = dice_roll("Player", 6)
            self.assertIsInstance(result, int)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 6)

    def test_shuffle(self):
        player_mech = Tank("player")
        deck = player_mech.create_starter_player_deck()
        original_deck = deck.copy()
        shuffled_deck = player_mech.shuffle_deck()
        self.assertEqual(len(shuffled_deck), 10)
        self.assertEqual(sum(c.card_type == CardType.SHOOT for c in shuffled_deck), 6)
        self.assertEqual(sum(c.card_type == CardType.SHIELD for c in shuffled_deck), 2)
        self.assertEqual(sum(c.card_type == CardType.REPAIR for c in shuffled_deck), 2)
        self.assertNotEqual([c.card_type for c in shuffled_deck],
                    [c.card_type for c in original_deck])
        self.assertEqual(len(deck), 0)




    

if __name__ == "__main__":
    unittest.main()

