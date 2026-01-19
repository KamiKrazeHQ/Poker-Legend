import random

suits = ["Spades","Hearts","Clubs","Diamonds"]
ranks = [2,3,4,5,6,7,8,9,10,11,12,13,14]
deck = []


class Card:
    def __init__(self, suit, rank):
        self.suit = suit 
        self.rank = rank
    
    def cardinfo(self):
        rank_str = str(self.rank)
        if self.rank == 11:
            rank_str = "J"
        elif self.rank == 12:
            rank_str = "Q"
        elif self.rank == 13:
            rank_str = "K"
        elif self.rank == 14:
            rank_str = "A"
        return f"{rank_str} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def deck_shuffle(self):
        random.shuffle(self.deck)  

    def card_display(self):
        for card in self.deck:
            print(card.cardinfo())
    

    def card_display(self):
        for card in self.deck:
            print(card.cardinfo())



test_deck = Deck()
test_deck.card_display()
test_deck.deck_shuffle()
test_deck.card_display()



        

    





    
