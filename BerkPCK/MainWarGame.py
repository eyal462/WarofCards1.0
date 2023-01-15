from CardGame import CardGame

if __name__ == '__main__':
    """THE MAIN GAME"""
    points1 = 0
    points2 = 0
    num_cards = int(input("enter number of cards:"))
    player1 = "eyal"
    player2 = "lior"
    CardGame1 = CardGame(player1, player2, num_cards)

    for i in range(10):
        #   """create 10 rounds of War of Cards"""
        card1 = CardGame1.player1.get_card()
        card2 = CardGame1.player2.get_card()
        if card1.__gt__(card2):
            """PLAYER 1 WIN"""
            print("==============NEW MATCH=====================")
            CardGame1.player1.add_card(card2)
            CardGame1.player1.add_card(card1)
            print(f"{CardGame1.player1.name}'s: {card1.__repr__()}")
            print(f"{CardGame1.player2.name}'s: {card2.__repr__()}")
            points1 += 1
            print(
                f"PLAYER 1 ({CardGame1.player1.name}) IS THE WINNER (Points: {CardGame1.player1.name} {points1}:{points2} {CardGame1.player2.name})\n")
        if card2.__gt__(card1):
            """PLAYER 2 WIN"""
            print("==============NEW MATCH=====================")
            CardGame1.player2.add_card(card1)
            CardGame1.player2.add_card(card2)
            print(f"{CardGame1.player1.name}'s: {card1.__repr__()}")
            print(f"{CardGame1.player2.name}'s: {card2.__repr__()}")
            points2 += 1
            print(
                f"PLAYER 2 ({CardGame1.player2.name}) IS THE WINNER (Points: {CardGame1.player1.name} {points1}:{points2} {CardGame1.player2.name})\n")
        else:
            print("============TIE================\n")
    print("================END OF GAME ======================\n")
    if CardGame1.get_winner() == None:
        print("===========================TIE=============================\n")
    else:
        print(f"=================THE WINNER IS {CardGame1.get_winner()}!!======================")
