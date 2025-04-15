#********** THE BLACKJACK CAPSTONE PROJECT: A python program that simulates the game of BlackJack **********#
import  random
from art import logo
# Function that deals both user and computer a random card.
def deal_card():
    # List of cards to be dealt
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Pick any two items from teh list and assign them to the list hand
    card = random.choice(cards)
    # Return the picked cards
    return card

# Function that calculates the score of each player
# Parameter: List of cards
def calculate_score(cards):
    # Detect when computer or user has a blackjack. (Ace + 10 value card)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead
    if sum(cards) > 21 and 11 in cards:
        # Remove the 11 and replace it with a 1
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Compare user and computer scores and see if it's a win, loss, or draw
def compare (u_score, c_score):
    if u_score == c_score:
       return "You draw"
    elif c_score == 0:
        return "You lose. Dealer has a blackjack"
    elif u_score == 0:
        return "You win. You have a blackjack"
    elif u_score > 21:
        return "You lose."
    elif c_score > 21:
        return "You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

# Function that defines the game
def play_game():
    print(logo)
    # Lists to hold each players cards
    user_cards = []
    computer_cards = []
    # Variable to test edge cases of while loops not running
    computer_score = -1
    user_score = -1
    # Boolean that holds game state
    is_game_over = False

    # Assign two cards to the player and dealer
    # NOTE: When you want to add a single item to a list, use append()
    # NOTE: When you want to add a list to a list, use extend()
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User while loop
    while not is_game_over:
        # Calculate user final score
        user_score = calculate_score(user_cards)
        # Calculate computer final score
        computer_score = calculate_score(computer_cards)

        # Print the player's cards and the computer's first card only
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # If computer gets blackjack, then the user loses (even if the user also has a blackjack)
        # Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
        if computer_score == 0 or user_score == 0 or user_score > 21:
            # Set game end boolean to ture
            is_game_over = True
        # Ask the user if they want to get another card.
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            # Hit
            if user_should_deal == "y":
                user_cards.append(deal_card())
            # Stand
            else:
                is_game_over = True

    # Computer Game while loop: Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16
    while computer_score != 0 and computer_score < 17:
        # Draw cards to the computer's hand
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Print out the player's and computer's final hand and their scores at the end of the game.
    print(f"Your final hand: {user_cards}, Final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Final score: {computer_score}")
    print(compare(user_score, computer_score))

# After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
while input("Do you want to play a game of Blackjack? If 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()