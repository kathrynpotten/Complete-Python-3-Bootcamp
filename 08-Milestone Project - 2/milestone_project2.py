""" Milestone Project 2 - Blackjack Game """


import random
from collections import Counter

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def __str__(self):
        return "\n".join(str(card) for card in self.all_cards)

    def __iter__(self):
        return iter(self.all_cards)

    def __len__(self):
        return len(self.all_cards)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name="One", money=0):
        self.name = name
        self.all_cards = []
        self.value = 0
        self.money = money

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

    def __len__(self):
        return len(self.all_cards)

    def hand(self):
        return ", ".join(str(card) for card in self.all_cards)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
            for card in new_cards:
                self.value += card.value
        else:
            self.all_cards.append(new_cards)
            self.value += new_cards.value

    def remove_hand(self):
        self.all_cards = []
        self.value = 0

    def add_money(self, amount):
        self.money += amount

    def lose_money(self, amount):
        self.money -= amount

    def initial_money_pot(self):
        while True:
            try:
                self.add_money(int(input("How much money do you have for the game? ")))
            except TypeError:
                print("Please input a number")
                continue
            else:
                break

    def place_bet(self):
        while True:
            try:
                self.bet = input("Place a bet: ")
                if self.bet.isdigit() == False:
                    raise ValueError("Please input a number for your bet")
                else:
                    self.bet = int(self.bet)
                if self.bet > self.money:
                    raise ValueError("You don't have enough money left!")
            except ValueError as error:
                print(repr(error))
            else:
                break

    def aces(self):
        ranks = [card.rank for card in self.all_cards]
        counts = Counter(ranks)
        aces = counts["Ace"]
        while self.value > 21 and aces:
            self.value -= 10
            aces -= 1
        return counts["Ace"]


class Dealer(Player):
    def __init__(self, name="Dealer"):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards."


def player_turn(player, deck, round_end=False):
    """function to run the player's turn in a Blackjack game"""
    player_turn = True
    print(f"Player {player.name} to play")
    while player_turn:
        player_choice = input("Would you like to hit or stand? ")
        if player_choice.lower() == "hit":
            player.add_cards(deck.deal_one())
            print(f"Your hand is {player.hand()}")
            player.aces()
            if player.value > 21:
                print(f"Bust! Player {player.name} loses")
                player.lose_money(player.bet)
                round_end = True
                player_turn = False
                break
            else:
                print(f"Your current total is {player.value}")
        elif player_choice.lower() == "stand":
            player_turn = False
            break
        else:
            print("Invalid choice, please choose again.")
    return round_end, player


def dealer_turn(dealer, player, deck, round_end=False):
    """function to run the automated dealer's turn in a Blackjack game"""
    dealer_turn = True
    print(f"Dealer to play")
    while dealer_turn:
        if dealer.value < player.value:
            dealer.add_cards(deck.deal_one())
            dealer.aces()
            continue
        elif dealer.value > 21:
            print(f"Bust! Player {player.name} wins")
            player.add_money(2 * player.bet)
            round_end = True
            dealer_turn = False
            break
        elif dealer.value > player.value and dealer.value > 21:
            print(f"Bust! Player {player.name} wins")
            player.add_money(2 * player.bet)
            round_end = True
            dealer_turn = False
            break
        elif dealer.value > player.value and dealer.value <= 21:
            print(f"Dealer has {dealer.value}, dealer wins")
            player.lose_money(player.bet)
            round_end = True
            dealer_turn = False
            break
    return round_end, dealer, player


if __name__ == "__main__":
    # define dealer and player
    dealer = Dealer()
    player_name = input("Choose a name: ")
    player = Player(player_name)

    # get player total money pot
    player.initial_money_pot()

    round_number = 0
    game_on = True

    while game_on:
        round_number += 1
        round_end = False

        new_deck = Deck()
        new_deck.shuffle()

        print(f"\nRound {round_number}\n")

        # deal initial cards
        for _ in range(2):
            print("Dealing cards...")
            player.add_cards(new_deck.deal_one())
            dealer.add_cards(new_deck.deal_one())

        print("Initial hand dealt")
        print(f"Your hand is {player.hand()}")

        # inform player of current hand value, including any aces present
        if player.has_ace():
            print(f"You have an Ace!")
            print(
                f"Your current total is {player.value}, or {player.value_with_aces} with aces as eleven"
            )
            player.choose_aces()
        else:
            print(f"Your current total is {player.value}")

        # place bet
        player.place_bet()

        while round_end == False:
            # player turn
            round_end, player = player_turn(player, new_deck)

            if round_end:
                break

            # dealer turn
            round_end, dealer, player = dealer_turn(dealer, player, new_deck)

        player.remove_hand()
        dealer.remove_hand()

        if player.money <= 0:
            print("You're bankrupt! Game over")
            game_on = False
        else:
            print(f"Your current bankroll is {player.money}")
            game = input("Do you want to continue? (yes/no) ")
            if game.lower() in ["y", "yes"]:
                pass
            else:
                game_on = False
