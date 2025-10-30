import unittest
from card_type import Card, CardType
from deck import create_starter_player_deck

class TestDeckCreation(unittest.TestCase):
    def test_deck_counts(self):
        deck = create_starter_player_deck()
        self.assertEqual(len(deck), 10)
        self.assertEqual(sum(c.card_type == CardType.SHOOT for c in deck), 6)
        self.assertEqual(sum(c.card_type == CardType.SHIELD for c in deck), 2)
        self.assertEqual(sum(c.card_type == CardType.REPAIR for c in deck), 2)

if __name__ == "__main__":
    unittest.main()