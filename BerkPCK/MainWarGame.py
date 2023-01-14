from Card import Card
from Player import Player
from CardGame import CardGame
from Deck_of_Cards import Deck_of_Cards

if __name__ == '__main__':
  #  """THE MAIN GAME"""
  player1=Player("eyal", 26)
  player2=Player("ben-mosh", 26)
  points1 = 0
  points2 = 0
  num_cards = int(input("enter number of cards:"))
  cg = CardGame(player1 ,player2, num_cards)
  print(f"player 1 {player1.num_of_cards}")
  print(f"player 2 {player2.num_of_cards}")

  for i in range (10):
   #   """create 10 rounds of War of Cards"""
    card1 = player1.get_card()
    card2 = player2.get_card()
    if card1.__gt__(card2):
        """PLAYER 1 WIN"""
        print("==============NEW MATCH=====================")
        player1.add_card(card2)
        print(f"{player1.name}'s: {card1.__repr__()}")
        print(f"{player2.name}'s: {card2.__repr__()}")
        points1 +=1
        print(f"PLAYER 1 ({player1.name}) IS THE WINNER (Points: {player1.name} {points1}:{points2} {player2.name})\n")
    if card2.__gt__(card1):
        """PLAYER 2 WIN"""
        print("==============NEW MATCH=====================")
        player2.add_card(card1)
        print(f"{player1.name}'s: {card1.__repr__()}")
        print(f"{player2.name}'s: {card2.__repr__()}")
        points2 += 1
        print(f"PLAYER 2 ({player2.name}) IS THE WINNER (Points: {player1.name} {points1}:{points2} {player2.name})\n")
    else:
        print("============TIE================\n")
  print("================END OF GAME ======================")
  print(f"THE WINNER IS {cg.get_winner()}!!")