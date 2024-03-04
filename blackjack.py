import random
import os
import art

def deal_card():
    """Function to deal a random card from the deck."""
    # A can be 11 or 1 based on the situation while J, Q, K are valued as 10.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Function to calculate the score of a hand."""
    if sum(cards) == 21 and len(cards) == 2:  # Checking for blackjack (Ace + 10 value card)
        return 21
    elif 11 in cards and sum(cards) > 21:  # Handling Ace as 11 or 1
        cards.remove(11)
        cards.append(1)
    return sum(cards)

play_again = False

while not play_again:
    user_cards = []
    computer_cards = []
    game_end = False

    # Dealing initial cards to the player and the computer
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(art.logo)
        print("Welcome to Blackjack!")
        print(f"Your cards are: {user_cards}, with a sum of: {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")
        
        # Checking if the game should end based on current scores
        if user_score == 21 or computer_score == 21 or user_score > 21:
            game_end = True
        else:
            draw_card = input("Do you want to draw another card, type 'hit' or 'stand': ")
            if draw_card == "hit":
                user_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
                os.system('cls')  # Clearing the screen after drawing a card
            else:
                game_end = True

    # Computer's turn
    while computer_score != 21 and computer_score < 17:  # Computer draws cards until it reaches 17 or above
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    def compare(user_score, computer_score):
        """Function to compare the scores and determine the winner."""
        if computer_score == user_score:
            return "It's a DRAW😑"
        elif computer_score == 21 or computer_score == 21:
            return "Computer has Blackjack😱, YOU LOSE!"
        elif user_score == 21 or user_score == 21:
            return "You have Blackjack😲, YOU WIN!"
        elif user_score > 21:
            return "You have a bust card😓, YOU LOSE!"
        elif computer_score > 21:
            return "Computer has a bust card🤓, YOU WIN!"
        else:
            if user_score > computer_score:
                return "YOU WIN!🥳"
            else:
                return "YOU LOSE!😭"

    os.system('cls')  # Clearing the screen before displaying results
    print(art.logo)
    print(f"Your cards are: {user_cards}, sum = {user_score}")
    print(f"Computer's cards are: {computer_cards}, sum = {computer_score}")
    print(compare(user_score, computer_score))

    again = input("Do you want to play again, 'yes' or 'no': ")

    if again == "yes":
        os.system('cls')  # Clearing the screen for the next game
    else:
        play_again = True

input("Tap Enter to Exit!")  # Waiting for user input before exiting
