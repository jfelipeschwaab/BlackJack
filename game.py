from entities.card import Cards
from entities.card import Numbers
from entities.card import Nipes
import random
from itertools import repeat


for number in Numbers:
    for nipe in Nipes:
        Cards.append('{number} de {nipe}'.format(nipe = nipe, number = number))



numbers = list(range(2, 14))  
values = [num for num in numbers for _ in repeat(None, 4)]

for number in range(4):
  values.append(11)
  
  
cards_values = {key:value for key,value in zip(Cards, values)}


player_name = input('Hello, Welcome to the terminal blackjack game. please, enter your Player name: ')

player_deck = [] 
first_card = []
second_card = []
house_deck = []
player_total = []
class Game:


  
  def __init__(self, player = player_name, cards = Cards):
      self.player = player 
      self.cards = cards
        
        
        
        
  def first_round(self):
    random_first_card = random.choice(Cards)
    first_card.append(random_first_card)
        

    print('Your first card is {first_card}'.format(first_card=first_card))

  def second_round(self):
    random_second_card = random.choice(Cards)
    second_card.append(random_second_card)
    
    

    print('Your second card is {second_card}'.format(second_card = second_card))
    

  def house_cards(self):
    for _ in range(2):
        random_two_cards = random.choice(Cards)
        house_deck.append(random_two_cards)
          
          
  def player_cards(self):
    player_deck.append(first_card)
    player_deck.append(second_card)
    print('This is your cards: ' + str(player_deck))        
          
  def player_points(self):
    global player_total
    for card in player_deck:
        soma = cards_values.get(card)
        player_total += soma
      
    
    print('And your total is {player_total}'.format(player_total = player_total))
        
    
    
          

  


Game_one = Game()

Game_one.first_round()
input('''Press enter to continue 


''')
print('Now the House is getting their card')
input('''Press enter to continue 


''')

Game_one.second_round()

input('''Press enter to continue 


''')

Game_one.player_cards()


input('''Press enter to continue 


''')

Game_one.player_points()
    