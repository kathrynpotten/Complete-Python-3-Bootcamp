import milestone_project2

def test_card_value():
    assert milestone_project2.Card("Hearts","Two").value == 2
    
def test_picture_card_value():
    assert milestone_project2.Card("Hearts","King").value == 10

def test_player_add_one_card():
    player = milestone_project2.Player()
    player.add_cards(milestone_project2.Card("Hearts","Two"))
    assert str(player.all_cards[0]) == 'Two of Hearts'


def test_player_win():
    dealer_win = False
    player_win = False
    player_value = 19
    dealer = milestone_project2.Dealer()
    dealer.add_cards([milestone_project2.Card("Hearts","Two"),milestone_project2.Card("Hearts","King")])
    dealer_turn = True
    while dealer_turn:
        if dealer.value < player_value:
            new_card = milestone_project2.Card("Clubs","Queen")
            dealer.add_cards(new_card)
            if dealer.has_ace() > 0:
                if dealer.value_with_aces > player_value:
                    dealer_win = 'aces'
                    break
                break
        elif dealer.value > 21:
            player_win = True
            break
        elif dealer.value > player_value and dealer.value > 21:
            player_win = True
            break
        elif dealer.value > player_value:
            dealer_win = True
            break
    assert player_win == True

def test_dealer_win():
    dealer_win = False
    player_value = 19
    dealer = milestone_project2.Dealer()
    dealer.add_cards([milestone_project2.Card("Hearts","Two"),milestone_project2.Card("Hearts","King")])
    dealer_turn = True
    while dealer_turn:
        if dealer.value < player_value:
            new_card = milestone_project2.Card("Clubs","Eight")
            dealer.add_cards(new_card)
            if dealer.has_ace() > 0:
                if dealer.value_with_aces > player_value:
                    dealer_win = 'aces'
                    break
                break
        elif dealer.value > 21:
            player_win = True
            break
        elif dealer.value > player_value and dealer.value > 21:
            player_win = True
            break
        elif dealer.value > player_value:
            dealer_win = True
            break
    assert dealer_win == True

def test_dealer_win_ace():
    dealer_win = False
    player_value = 19
    dealer = milestone_project2.Dealer()
    dealer.add_cards([milestone_project2.Card("Hearts","Two"),milestone_project2.Card("Hearts","Eight")])
    dealer_turn = True
    while dealer_turn:
        if dealer.value < player_value:
            new_card = milestone_project2.Card("Clubs","Ace")
            dealer.add_cards(new_card)
            if dealer.has_ace() > 0:
                if dealer.value_with_aces > player_value:
                    dealer_win = 'aces'
                    break
                break
        elif dealer.value > 21:
            player_win = True
            break
        elif dealer.value > player_value and dealer.value > 21:
            player_win = True
            break
        elif dealer.value > player_value:
            dealer_win = True
            break
    assert dealer_win == 'aces'