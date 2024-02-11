from entities.card import Cards
from entities.card import cards_values
import random



player_name = input('Hello, Welcome to the terminal blackjack game. please, enter your Player name: ')

player_deck = [] 
house_deck = []
class Game:


  
  def __init__(self, player = player_name, cards = Cards):
      self.player = player 
      self.cards = cards
      self.player_total = 0
      self.house_total = 0
        
        
        
        
  def first_round(self):
      global first_card 
      first_card = []
      random_first_card = random.choice(Cards)
      first_card.append(random_first_card)
        

      print('Your first card is {first_card}'.format(first_card=first_card))

  def second_round(self):
      global second_card
      second_card = []
      random_second_card = random.choice(Cards)
      second_card.append(random_second_card)
    
    

      print('Your second card is {second_card}'.format(second_card = second_card))
    

  def house_cards(self):
      
      first_house_card = random.choice(Cards)
      second_house_card = random.choice(Cards)
    
      house_deck.append(first_house_card)
      house_deck.append(second_house_card)
      
      print('The house cards are {first} and {second}'.format(first = first_house_card, second = second_house_card))
          
          
  def player_cards(self):
      player_deck.extend(first_card)
      player_deck.extend(second_card)
      print('This is your cards: ' + str(player_deck))        
          
  def player_points(self):
      for card in player_deck:
        soma = cards_values.get(card)
        self.player_total += soma
      
    
      print('And your total is {player_total}'.format(player_total = self.player_total))
        
  def house_points(self):
      for card in house_deck:
          soma_house = cards_values.get(card)
          self.house_total += soma_house
    
      print('O total da casa é {house_total}'.format(house_total = self.house_total))    

  


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


input('''Press enter to continue 


''')


Game_one.house_cards()
Game_one.house_points()




    