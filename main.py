# BlackJack Game

# import module
import random
from art import logo
from os import clear

# deal card function
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# calculate score of cards
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # if in deck is 21 score this is a blackjack and return 0.
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    # if in deck is ACE(11,1) and score over 21 that mean ACE must be 1 . this operation will remove 11 and replace it with a 1 .
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    #return sum of card's value
    return sum(cards)
# make a list of cards for user and computer where will be insert random
# randomly card type from deal_card() function. 
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose , Computer has BlackJack!"
    elif user_score == 0:
        return "Congrats! You win with a BlackJack!"
    elif user_score > 21:
        return "You went Over. You lose!"
    elif computer_score > 21:
        return "Opponent went Over. You win!" 
    elif user_score > computer_score:
        return "You Wins!"
    else:
        return "You Lose!"
    
def play_blackjack():    
    print(logo)
    
    user_cards = []
    computer_cards = []
    # boolean var for game is over or not 
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    # print(user_cards, computer_cards)
    
    
    # if computer or user has blackjack or if the user card's score over 21, the game ends.
    # this two variable calculated score  of user and computer cards.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"    user cards: {user_cards}, current score: {user_score}")
        print(f"    computer cards: {computer_cards[0]}")
        if user_score == 0  or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        # there is a operation where dealer ask user if they want to draw another card.
        # if answer is YES , then use the deal_card function to add another card .
        # if answer is NO , then the is_game_over True and end the game !. 
    
    # after the user is done , its time to computer's turn.
    # The computer should keep drawing cards as long as it has s score les then 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"    Your Final hand: {user_cards}, Final score: {user_score}")
    print(f"    Computer's Final hand: {computer_cards}, Final score: {computer_score}")
    print(compare(user_score, computer_score))
# ask the user if they want to restart the game.
while input("Do you want play BlackJack ? Type 'y' or 'n':  ").lower() == 'y':
    clear()
    play_blackjack()