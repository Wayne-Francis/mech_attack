import unittest
from card_type import Card, CardType
from mech_type import *
from utility_functions import dice_roll
import random
import io
from unittest.mock import patch

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

    def test_new_cout_mech(self):
        ai_mech = Scout("ai")
        self.assertEqual(repr(ai_mech), "Mech=MechType.SCOUT,name='ai'")
        self.assertEqual(ai_mech.mech_type, MechType.SCOUT)

    def test_show_stats(self):
        player_mech = Gunner("player")
        self.assertEqual(player_mech.show_stats(), "HP = 12\nCurrent Attack Power = 1\nCurrent Speed = 3")

    def test_show_stats(self):
        ai_mech = Scout("ai")
        self.assertEqual(ai_mech.show_stats(), "HP = 8\nCurrent Attack Power = 1\nCurrent Speed = 1")    

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
        deck = player_mech.create_starter_player_deck()  # already shuffled
        # Check total number of cards
        self.assertEqual(len(deck), 10)
        # Check card type counts
        self.assertEqual(sum(c.card_type == CardType.SHOOT for c in deck), 6)
        self.assertEqual(sum(c.card_type == CardType.SHIELD for c in deck), 2)
        self.assertEqual(sum(c.card_type == CardType.REPAIR for c in deck), 2)
        # Optional: ensure all cards from original deck are present
        original_deck = [
            Card("Shoot", CardType.SHOOT)] * 6 + \
            [Card("Shield", CardType.SHIELD)] * 2 + \
            [Card("Repair", CardType.REPAIR)] * 2
        # Compare ignoring order
        self.assertCountEqual([c.card_type for c in deck],
                          [c.card_type for c in original_deck])


    def test_hand_display(self):
        player_mech = Tank("player")
        player_mech.create_starter_player_deck()
        player_mech.create_starter_hand()
        player_mech.show_hand()


    def test_show_hand(self):
        player_mech = Tank("player")
        player_mech.create_starter_player_deck()
        player_mech.create_starter_hand()

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            player_mech.show_hand()
            output = fake_out.getvalue()

        
        self.assertIn("There are 3 cards in your hand", output)

    def test_show_hand_with_draw(self):
        player_mech = Tank("player")
        player_mech.create_starter_player_deck()
        player_mech.create_starter_hand()
        player_mech.draw_card()

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            player_mech.show_hand()
            output = fake_out.getvalue()

        self.assertIn("There are 4 cards in your hand", output)

    def test_play_card(self):
        player_mech = Tank("player")
        player_mech.create_starter_player_deck()
        player_mech.create_starter_hand()  # Hand has 3 cards

        # Store the card we expect to pick
        expected_card = player_mech.hand[1]  # second card in hand

        # Mock input: first an invalid option "5", then valid "2"
        with patch('builtins.input', side_effect=['5', '2']):
            chosen_card = player_mech.play_card()

        # Check that the chosen card is the expected one
        self.assertEqual(chosen_card, expected_card)

        # Hand should now have 2 cards (one removed)
        self.assertEqual(len(player_mech.hand), 2)

        # The removed card should no longer be in hand
        self.assertNotIn(chosen_card, player_mech.hand)


if __name__ == "__main__":
    unittest.main()

