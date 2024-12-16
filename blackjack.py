import random

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit 
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"   

class Deck:
    def __init__(self):
        self.suits = ['Hearts','Diamonds','Clubs','Spades']
        self.values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
        self.cards = [Card(value,suit) for value in self.values for suit in self.suits]

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards
    
    def deal(self):
        return self.cards.pop()
    

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.points = 0
        self.turn = False

    def draw(self,deck):
        card = deck.deal()
        self.hand.append(card)
        return card

    def score(self):
        Aces = 0
        self.points = 0
        for card in self.hand:
            self.points += Deck().values[card.value]
            if card.value == "A":
                Aces += 1  
        while Aces > 0 and self.points > 21:
            self.points -= 10
            Aces -= 1
        return self.points

    def __str__(self):
        return f"{self.name} has {self.points} points with {self.hand}"

def blackjack():
    deck = Deck()
    deck.shuffle()
    player = Player('Player')
    dealer = Player('Dealer')
    player.turn = True

    player.draw(deck)
    dealer.draw(deck)
    
    print(player.hand)

    while player.turn:
        option = input("Do you want to hit or stand? (h/s): ") 

        if option == 'h' or option == 'hit':
            player.draw(deck)
            print(f"{player.hand}  Score: {player.score()}")
            if player.score() > 21:
                print("You Lose")
                break
            if player.score() == 21:
                print("Blackjack, player wins!")
                break
        elif option == 's' or option == 'stand':
            player.turn = False
            
    while not player.turn:

        if dealer.score() < 17 and player.score() < 21:
            dealer.draw(deck)
            print(f"{dealer.hand} Score: {dealer.score()}" )
        else:
            break

    if dealer.score() == player.score():
        print("It's a draw, bets refunded")
    elif dealer.score() > 21:
        print("Player wins!")
    elif player.score() > 21:
        print("Dealer wins!")
    elif dealer.score == 21:
        print("Blackjack, Dealer wins!")
    elif player.score() < 21 and dealer.score() < 21:
        if player.score() > dealer.score():
            print("Player wins!")
        else:
            print("Dealer wins")
blackjack()