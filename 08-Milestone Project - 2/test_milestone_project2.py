import unittest
import milestone_project2

class TestProject(unittest.TestCase):

    def test_card_value(self):
        card = milestone_project2.Card("Hearts","Two")
        self.assertEqual(card.value, 2)
    
    def test_picture_card_value(self):
        card = milestone_project2.Card("Hearts","King")
        self.assertEqual(card.value, 10)

    def test_player_add_one_card(self):
        player = milestone_project2.Player('One')
        card = milestone_project2.Card("Hearts","Two")
        player.add_cards(card)
        self.assertEqual(str(player.all_cards[0]), 'Two of Hearts')
    
    def test_player_add_multiple_cards(self):
        player = milestone_project2.Player('One')
        card_1 = milestone_project2.Card("Hearts","Two")
        card_2 = milestone_project2.Card("Diamonds","King")
        player.add_cards([card_1, card_2])
        self.assertEqual(', '.join(str(card) for card in player.all_cards), 'Two of Hearts, King of Diamonds')                                  

    def test_player_value(self):
        player = milestone_project2.Player('One')
        card_1 = milestone_project2.Card("Hearts","Two")
        card_2 = milestone_project2.Card("Diamonds","King")
        player.add_cards([card_1, card_2])
        self.assertEqual(player.value, 12)
    
    def test_has_one_ace(self):
        player = milestone_project2.Player('One')
        card_1 = milestone_project2.Card("Hearts","Ace")
        card_2 = milestone_project2.Card("Diamonds","King")
        player.add_cards([card_1, card_2])
        self.assertEqual(player.has_ace(),1)

    def test_val_one_ace(self):
        player = milestone_project2.Player('One')
        card_1 = milestone_project2.Card("Hearts","Ace")
        card_2 = milestone_project2.Card("Diamonds","King")
        player.add_cards([card_1, card_2])
        player.has_ace()
        self.assertEqual(player.value_with_aces,21)

    def test_val_one_ace2(self):
        player = milestone_project2.Player('One')
        card_1 = milestone_project2.Card("Hearts","Ace")
        card_2 = milestone_project2.Card("Diamonds","Two")
        player.add_cards([card_1, card_2])
        player.has_ace()
        self.assertEqual(player.value_with_aces,13)

if __name__ == '__main__':
    unittest.main()