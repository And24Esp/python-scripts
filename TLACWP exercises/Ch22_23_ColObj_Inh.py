class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same... check if either card is an Ace (EXERCISE 1)
        if self.suit == other.suit and self.rank == other.rank: return 0
        if self.rank == 1: return 1
        if other.rank == 1: return -1
        # Suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # Ranks are the same... it's a tie
        # Return 0 (this statement is unreachable after including EX1 statements)

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0

'''
card1 = Card(2, 5)
card2 = Card(2, 1)
card3 = Card(2, 5)
print(card1 < card2)
print(card1 == card3)
'''

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random
        rng = random.Random()        # Create a random generator
        rng.shuffle(self.cards)      # Use its shuffle method
    
    def remove(self, card):     #not sure how to express the card parameter when calling the method (hopefully ch23 gives me an answer to this)
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False    

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break                    # Break if out of cards
            card = self.pop()            # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)               # Add the card to the hand

'''
red_deck = Deck()
blue_deck = Deck()
print(red_deck)
'''

class Hand(Deck):

    def __init__(self, name=""):
       self.cards = []
       self.name = name

    def __str__(self):
        s = self.name + "'s hand"
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)

    def add(self, card):
        self.cards.append(card)

'''
deck = Deck()
deck.shuffle()
hand1 = Hand("Frank")
hand2 = Hand("Joe")
deck.deal([hand1, hand2], 10)
print(hand1, hand2)
'''

class CardGame:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

class OldMaidHand(Hand):

    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}"
                        .format(self.name, card, match))
                count += 1
        return count

# Me quedé en la mitad del punto 23.6 del libro. El concepto de Inheritance lo tengo claro.
# Los puntos 23.6 y 23.7 al parecer no introducen ningun nuevo concepto de computer science.
# Los ejercicios 2 y 3 no creo que los haga de momento, ya que son del tipo "Aliens" (Ch17).
# Entender la mecánica del juego (Old Maid) me va a tomar un poco de tiempo y enfoque.
# CONCLUSIÓN: Voy a continuar con los siguientes capitulos, y cuando termine el libro, 
# sobretodo si deseo hacer un juego de cartas, retomo los puntos que quedaron pendientes.