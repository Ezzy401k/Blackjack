import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
             return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

user_cards = []
computer_cards = []
game_over = False
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"computer's first card : {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        draw = input("Do you want draw another card, 'y' or 'n': ")
        if draw == "y":
            user_cards.append(deal_card())
        else:
            game_over = True

while computer_score != 0 or computer_score < 17:
     computer_cards.append(deal_card())
     computer_score = calculate_score(computer_cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Its a draw!")
    elif computer_score == 0:
        print("You lose!")
    elif user_score == 0:
        print("You Win!")
    elif user_score > 21:
        print("bust!")
    elif computer_score > 21:
        print("You win!")
    else:
        if user_score > computer_score:
            print("You Win!")
        else:
            print("You Lose!")

compare(user_score, computer_score)