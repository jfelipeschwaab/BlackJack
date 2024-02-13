from entities.card import Cards
from entities.card import cards_values
import random
import sys



player_name = input('Hello, Welcome to the terminal blackjack game. please, enter your Player name: ')
print('''
      Hello {player_name} The BlackJack Game consists as a try to have 21 points or less at the end of the game to win the House, which one has points too.
      if you ultrapass the value of 21 points, you've already lost.
      Each card Has your value, the number has the value itself, and Letters are 10 valuable, in exception for the Ace, which one has the 11 value
      '''.format(player_name = player_name ))
input('''Press enter to continue 


''')

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
        
      
    
        
        
      
    
      print('your total is {player_total}'.format(player_total = self.player_total))
        
  def house_points(self):
        for card in house_deck:
            soma_house = cards_values.get(card)
            self.house_total += soma_house

        print('The house total is:  {house_total}'.format(house_total = self.house_total)) 
      
      
      
      
  def buy_cards(self):
      buy = input('Do you want to buy another card? If so, type Buy, if not, type No: ')
      while buy != 'Buy' and buy != 'No':
          buy = input('Whoops, seems that you have mistaken the spell, please, type Buy or No, as written in the terminal: ')
      if buy == 'Buy':
          global after_buy
          after_buy = []
          another_card = random.choice(Cards)
          player_deck.append(another_card)
          after_buy.append(another_card)
          print(player_deck)
          another_buy = input('Do you  want another card?, if so, type Buy, if not, tipe No: ')
          
          
          while another_buy != 'Buy' and another_buy != 'No':
            another_buy = input('Whoops, seems that you have mistaken the spell, please, ty Buy or No, as written in the terminal: ')
          
          while another_buy == 'Buy':
              if len(player_deck) < 20:
                card2 = random.choice(Cards)
                player_deck.append(card2)
                after_buy.append(card2)
                print(player_deck)
            
                another_buy = input('Do you want another card? if so, type Buy, if not, type No: ')
              
                  
            
            
          if another_buy == 'No': 
                          
              for card in after_buy:                
                  after_buy = cards_values.get(card)
                  if after_buy is not None:                     
                      self.player_total += after_buy
              print('Your total is {player_total}'.format(player_total = self.player_total))
      
         
      else:
          print('Your total is {player_total}'.format(player_total = self.player_total))       
               

  def BlackJack_player(self):
      if self.player_total == 21:
          print("You've already won, you have a BlackJack")
          sys.exit()
      elif self.player_total > 21:
          print("You've already lost, you ultrapassed the limit of 21 ")
          sys.exit() 
          
    
    
      else:
          pass
           
  def BlackJack_house(self):
      if self.house_total == 21 and self.player_total ==21:
          print("Whoops, seems that you and the House have the same amount, that's a draw")
    
      elif self.house_total == 21 and not self.player_total >= 21:
          print("The house has a blackjack, you've already lost partner")
    
      elif self.house_total == 21 and self.player_total > 21:
          print("You are in a bad day, seems that the house has a BlackJack and you've ultrapassed the limit of 21") 
      else:
          pass   
          
          
          
          
  def Winner(self):
      if self.player_total > self.house_total and self.player_total <= 21:
          print('Congratulations, you are the winner')       
    
      elif self.player_total < self.house_total and self.house_total <= 21:
          print('Seems that the House have won, lucky next time')
      elif self.player_total == self.house_total:
          print('You and the house have the same points, that is a Draw')
      elif self.player_total > 21:
          print('You have ultrapassed the 21 limit, you have lost, Good lucky next time')
      else:         
          pass


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
Game_one.BlackJack_player()

input('''Press enter to continue 


''')
Game_one.buy_cards()



input('''Press enter to continue 


''')



Game_one.house_cards()
Game_one.house_points()
Game_one.BlackJack_house()
Game_one.Winner()





    