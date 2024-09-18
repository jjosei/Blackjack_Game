import random
from art import logo

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def compare(user_score, computer_score ):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def calculate_score(cards):
    """Take a list of cards and returns the sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    # computer_score and user_score are set to -1 because that value can be used to properly test the code
    isGameOver = False

    for _ in range(2):
        user_cards.append(deal())
        computer_cards.append(deal())

    while not isGameOver:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are {user_cards}. Your current score is {user_score}.")
        print(f"Computer's hand is {computer_cards[0]}.")

        print("\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isGameOver = True
        else:
            another_card = input(print("Do you want to add another card(Yes) or pass(No)?")).lower()
            if another_card == "yes":
                user_cards.append(deal())
            elif another_card == "no":
                isGameOver = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards} and final score is {user_score}")
    print(f"Computer's final hand is {computer_cards} and it's score is {computer_score}")
    print(compare(user_score, computer_score))


while input(print("Click S to start playing Blackjack!!")).lower() == "s":
    print("\n" * 10)
    play_game()