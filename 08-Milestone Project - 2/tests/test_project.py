import milestone_project2


def test_card_value():
    assert milestone_project2.Card("Hearts", "Two").value == 2


def test_picture_card_value():
    assert milestone_project2.Card("Hearts", "King").value == 10


def test_player_add_one_card():
    player = milestone_project2.Player()
    player.add_cards(milestone_project2.Card("Hearts", "Two"))
    assert str(player.all_cards[0]) == "Two of Hearts"


def dealer_turn(dealer, player_value, new_card):
    dealer_win = False
    player_win = False
    dealer_turn = True
    while dealer_turn:
        if dealer.value < player_value:
            dealer.add_cards(new_card)
            dealer.aces()
            continue
        elif dealer.value > 21:
            player_win = True
            break
        elif dealer.value > player_value and dealer.value > 21:
            player_win = True
            break
        elif dealer.value > player_value:
            dealer_win = True
            break
    return dealer_win, player_win


def test_player_win():
    player_value = 19
    dealer = milestone_project2.Dealer()
    dealer.add_cards(
        [
            milestone_project2.Card("Hearts", "Two"),
            milestone_project2.Card("Hearts", "King"),
        ]
    )
    dealer_win, player_win = dealer_turn(
        dealer, player_value, milestone_project2.Card("Clubs", "Queen")
    )

    assert player_win == True


def test_dealer_win():
    player_value = 19
    dealer = milestone_project2.Dealer()
    dealer.add_cards(
        [
            milestone_project2.Card("Hearts", "Two"),
            milestone_project2.Card("Hearts", "King"),
        ]
    )
    dealer_win, player_win = dealer_turn(
        dealer, player_value, milestone_project2.Card("Clubs", "Eight")
    )

    assert dealer_win == True


def test_dealer_win_ace():
    player_value = 19
    dealer = milestone_project2.Dealer()
    dealer.add_cards(
        [
            milestone_project2.Card("Hearts", "Two"),
            milestone_project2.Card("Hearts", "Seven"),
        ]
    )
    dealer_win, player_win = dealer_turn(
        dealer, player_value, milestone_project2.Card("Clubs", "Ace")
    )

    assert dealer_win == True
