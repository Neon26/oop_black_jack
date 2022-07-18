import random


#Black Jack Game:

    #Players:
        #Dealer
#dealer_cards = []
        #Player
#player_cards = []
    #Deck: 
#card_deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] *4
        # 52 cards
            #4 suits:
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
                #Clubs: 1-13 Ace = 1 or 11, J=11, Q=12, K=13. Clubs are green
                #Diamonds: 1-13 Ace = 1 or 11, J=11, Q=12, K=13. Diamonds are blue
                #Hearts: 1-13 Ace = 1 or 11, J=11, Q=12, K=13. Hearts are red
                #Spades: 1-13 Ace = 1 or 11, J=11, Q=12, K=13. Spades are white
playing = True

# CLASSES


class Card:  # Creates all the cards

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

    # Winner: 
        # When player or dealer get 21
        # When player or dealer get more than 21
class Deck:  # creates a deck of cards

    def __init__(self):
        self.deck = []  # haven't created a deck yet
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    
    #Game begins with a deck shuffle. Use Randomizer. Shuffle. Read the docs
    def shuffle(self):  # shuffle all the cards in the deck
        random.shuffle(self.deck)

    #Dealer deals:
    def deal(self):  # pick out a card from the deck
        single_card = self.deck.pop()
        return single_card
        
        
        
        
        # 2 cards to player face up
            #Display 2 cards to player

        # 2 cards to dealer. 1 card face up            
            #Display 1 card to dealer
class Hand:   # show all the cards that the dealer and player have

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # keep track of aces

    def add_card(self, card):  # add a card to the player's or dealer's hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

    #Count and display the toal of the players hand

def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)
        # if the total is less than 21 give the player options:
            #"Hit"= Get another card
            #"Stand"= Stay with current total and end your turn.
        #Player can "Hit" as often as they want.
            #if player goes over 21 the lose("Bust")

def player_busts(player, dealer):
    print("PLAYER BUSTS!")
    


def player_wins(player, dealer):
    print("PLAYER WINS!")
    


def dealer_busts(player, dealer):
    print("DEALER BUSTS!")
    


def dealer_wins(player, dealer):
    print("DEALER WINS!")
    


def push(player, dealer):
    print("Its a tie! DEALER WINS! ")




    #Player can only see both of Dealers hand when they chose to "Stand".

    #Dealer will "Hit" until their hand is 17 or higher.

def hit_or_stand(deck, hand):   # hit or stand
    global playing

    while True:
        ask = input("\nWould you like to Hit or Stand? Please enter 'Hit' or 'Stand': ")

        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print("Player stands, Dealer is playing.")
            playing = False
        else:
            print("Sorry! I did not understand that! Please try again!")
            continue
        break

    
    #Dealer ad player can go over 21 and "Bust" and lose the game
    #Tie goes to the dealer
# Gameplay!

while True:
    print("----------Welcome-------------")
    print("------------To----------------")
    print("---------BlackJack!-----------")

    # create an shuffle deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    


    # show cards
    show_some(player_hand, dealer_hand)
    #Player and dealer compare hands
    #Who ever has the higher hand wins.
    while playing:

        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand,)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand,)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand,)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand,)

    

    new_game = input("\nWould you like to play again? Enter 'Yes' or 'No': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break