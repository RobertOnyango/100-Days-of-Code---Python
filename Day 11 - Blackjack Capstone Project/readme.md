## THE BLACKJACK CAPSTONE PROJECT
https://www.247blackjack.com/

### BlackJack Objectives:
Add up the cards in your hand to the largest number before 21 or equal to 21.

Bust: If the cards in hand add up to more than 21. YOU LOSE immediately.

#### Counting cards 
Cards 2-10 are counted as their face value.

Cards Jake, Queen and King = 10 each.

Ace = 1 or 11: You decide which each represents depending on your game state/decision.

#### Game play sample and rules:
ROUND 1 (1st cards dealt / 1st hand): You (The Player) and the dealer each have one card (one card per player is dealt), which are both revealed.

2ND HAND: Both you and the dealer each get a 2nd card. But this time you can't see the dealer's 2nd card.

Based on your cards, you can ask for a 3rd card.

After this game state, you may reveal your cards so does the dealer.

#### Game WIN or LOSE rules:
                  1. If your cards add up to more than 21. YOU LOSE immediately i.e. BUST.
                  2. If your cards add up to <= 21 but more than what the dealer has, YOU WIN.
                  3. If your cards and the dealer's card add up to the same sum then YOU DRAW.
                  4. If the dealer's sum is more than yours but <= 21 YOU LOSE.
                  5. If the dealer's sum (hand) adds up to <17, they must take another card.

NB: At any point if your cards are less than 21, i.e. even after your 3rd card, you can ask for more cards.
    The game stops when you say you don't want any more hands dealt and then proceed to reveal your cards.

#### Game Vocabulary: 
DEAL = Place bet amount,

HIT = Add a card to my hand,

STAND = Maintain your hand i.e. End your hand or no more hits for me.

SPILT = Dividing a pair of identical cards (like two 8s or two 6s) into two separate hands. This allows you to play two hands instead of one, effectively doubling your potential wins and losses. You will need to place an additional bet equal to your original wager for each split hand

#### Project Assumptions 
For our code to be simple, the following are some of the accommodations we will have to make:
1. List of cards will be: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]:
2. The Ace can count as 11 or 1.
3. We have an infinite deck: When a card is drawn, it is not removed form the deck.




