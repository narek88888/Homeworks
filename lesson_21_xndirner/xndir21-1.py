
# class PlayingCard:
# def __init__(self, rank, suit):
# self.rank = rank
# self.suit = suit
# # TODO: Implement the __str__ magic method to return a string representation of the card.
# # TODO: Implement the __eq__ magic method to check if two cards are equal.
# # TODO: Implement the __ne__ magic method to check if two cards are not equal.
# # TODO: Implement the __lt__ magic method to check if a card is less than another card based on rank.
# # TODO: Implement the __le__ magic method to check if a card is less than or equal to another card based on rank.
# # TODO: Implement the __gt__ magic method to check if a card is greater than another card based on rank.
# # TODO: Implement the __ge__ magic method to check if a card is greater than or equal to another card based on rank.
# # Test your PlayingCard class
# card1 = PlayingCard("Ace", "Hearts")
# card2 = PlayingCard("King", "Spades")
# card3 = PlayingCard("Ace", "Hearts")
# # Test string representation
# print("Card 1:", card1)
# print("Card 2:", card2)
# # Test equality
# print("Card 1 == Card 2:", card1 == card2)
# print("Card 1 == Card 3:", card1 == card3)
# # Test less than
# print("Card 1 < Card 2:", card1 < card2)
# # Test less than or equal to
# print("Card 1 <= Card 2:", card1 <= card2)
# # Test greater than
# print("Card 2 > Card 1:", card2 > card1)
# # Test greater than or equal to
# print("Card 2 >= Card 1:", card2 >= card1)



class PlayingCard:
    x = ("Jack", "Queen", "King", "Ace")


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} {self.suit}"
    
    def __eq__(self, other):
        return PlayingCard.x.index(self.rank) == PlayingCard.x.index(other.rank)
    
    def __ne__(self, other):
        return PlayingCard.x.index(self.rank) != PlayingCard.x.index(other.rank)
               
    def __lt__(self,other):
        return PlayingCard.x.index(self.rank) < PlayingCard.x.index(other.rank)
    
    def __le__(self,other):
        return  PlayingCard.x.index(self.rank) <= PlayingCard.x.index(other.rank)
    
    def __gt__(self,other):
        return PlayingCard.x.index(self.rank) > PlayingCard.x.index(other.rank)
    
    def __ge__(self,other):
        return PlayingCard.x.index(self.rank) >= PlayingCard.x.index(other.rank)

    
card1 = PlayingCard("Ace", "searts")
card2 = PlayingCard("King", "speads")
card3 = PlayingCard("Ace", "searts")   

print(card1 >= card2)



