# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:27:15 2020

@author: Antti
"""

import random

#Global definitions

#Creating a dictionary for ranks -> Values
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}       

#A set of suits
suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')

#A set of ranks 
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#Creating a card class

class Card():
    
    def __init__ (self, suit, rank):
        self.suit = suit
        self.rank = rank
        
        #After values are globally defined, we
        #can add the value attribute
        self.value = values[self.rank]
        
    #Use magic method for viewing cards
    #Assigns a string representation

    def __str__ (self):
        return self.rank+ ' of ' + self.suit
  
#Creating the deck class
    
class Deck():
    
    def __init__(self):
        
        # .all_cards is a list of all cards in deck
        self.all_cards = []
        
        #Recursively creating each card
        for suit in suits:
            for rank in ranks:
                #Create the card object 
                created_card = Card(suit, rank)
                #Append to all_cards list
                self.all_cards.append(created_card)
                
    #Shuffling the deck
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    #Dealing cards
    def deal_one(self):
        return self.all_cards.pop()
    
    
#Creating a player class

class Player():
    
    def __init__ (self, player_name):
        
        #Each players name
        self.player_name = player_name
        
        #Create a list of cards held by the player
        self.all_cards = []
    
     #Removing one card   
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def remove_three(self):
        removed_cards = []
        removed_cards.append(self.all_cards.pop(0))
        removed_cards.append(self.all_cards.pop(0))
        removed_cards.append(self.all_cards.pop(0))
        return removed_cards
    
    #Removing many cards
    
    def add_cards(self, new_cards):
        
        #If new cards are a list
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        
        #For a single card object
        else:
            self.all_cards.append(new_cards)

    #Creating a string to print out player info
    
    def __str__ (self):
        return f'Player {self.player_name} holds {len(self.all_cards)} cards!'

main_deck = Deck()
player1 = Player('A')
player2 = Player('B')

def first_deal():
    """
    This program deals the cards in main_deck to two players

    """
    for cards in main_deck.all_cards[0:26]:
        player1.add_cards(cards)
        
    for cards in main_deck.all_cards[26:53]:
        player2.add_cards(cards) 

##Game start


main_deck = Deck()
main_deck.shuffle()

player1 = Player('A')
player2 = Player('B')
first_deal()

game_on = True

while game_on == True:
        show_list = [player1.remove_one(), player2.remove_one()]

    #If player1 has a higher card
        if show_list[0].value > show_list[1].value:
            print(f'Player 1 draws a {show_list[0].value}')
            print(f'Player 2 draws a {show_list[1].value}')
            player1.add_cards(show_list)
            print('Player 1 wins')
            print(player1)
            print(player2)
        
            quest = input('Do you wish to continue? (Y/N')
        
            if quest in ['Y' , 'y']:
                pass
        
            if quest in ['N' , 'n']:
                print('Thanks for playing :)')
                game_on = False
        
    #If p2 has a higher card value    
        if show_list[0].value < show_list[1].value:
           print(f'Player 1 draws a {show_list[0].value}')
           print(f'Player 2 draws a {show_list[1].value}')
           player2.add_cards(show_list)
           print('Player 2 wins')
           print(player1)
           print(player2)
        
           quest = input('Do you wish to continue? (Y/N)')
        
           if quest in ['Y' , 'y']:
                pass
        
           if quest in ['N' , 'n']:
            print('Thanks for playing :)')
            game_on = False
        
        if show_list[0].value == show_list[1].value:
            print(f'Player 1 draws a {show_list[0].value}')
            print(f'Player 2 draws a {show_list[1].value}')
            print('WAR!')
            show_list.append(player1.remove_one())
            show_list.append(player2.remove_one())
            show_list.append(player1.remove_one())
            show_list.append(player2.remove_one())
        
            if show_list[4].value > show_list[5].value:
                player1.add_cards(show_list)
                print('There was a war and Player 1 wins')
                print(player1)
                print(player2)
            
                quest = input('Do you wish to continue? (Y/N)')
        
                if quest in ['Y' , 'y']:
                    pass
        
                if quest in ['N' , 'n']:
                    print('Thanks for playing :)')
                    game_on = False
            
            if show_list[5].value > show_list[4].value:
            
                    player2.add_cards(show_list)
                    print('There was a war and Player 2 wins')
                    print(player1)
                    print(player2)
            
                    quest = input('Do you wish to continue? (Y/N)')
        
                    if quest in ['Y' , 'y']:
                        continue
        
                    if quest in ['N' , 'n']:
                       print('Thanks for playing :)')
                       game_on = False
                    














