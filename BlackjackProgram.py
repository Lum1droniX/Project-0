# Hayden Fillmore

    # This program aims to faithfully recreate the famous card game Blackjack (minus the betting of course).
    # It contains all face cards and non face cards, converting them to their respective worths in-game.
    # Along with the cards, I've done my best to recreate the ruleset and gameplay based mostly off what I learned in lecture.
    # After some personal research though, I found that using 'while True:' was crucial for the turn cycle.
    # Learning how to define the PlayerDraw function was the hardest part, although it played the biggest role for this program.

# =====

import random   # This allows access to the random.choice() feature.

print("==================================================================================")
print("")
print("The following code was made to replicate a game of Blackjack:")
print("")

# =====

# This is where I defined the lists used throughout the project
CardList = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
PlayerHand = []
DealerHand = []

# This PlayerDraw function pulls a random card from the CardList and appends them to whatever list variable is assigned.
# All the if, elif, and else statements are doing is providing proper verbage and letting the user determine what value an Ace has.
def PlayerDraw(Hand):
    Card = random.choice(CardList)
    if Card == "Ace":
        print("You drew an Ace!")
        while True:
            CardValue = input("Should the Ace be worth 1 or 11? ")
            if CardValue in ["1","11"]:
                Card = int(CardValue)
                break
            print("Invalid input.")

    elif Card == "King":
        print("You drew a King!")
        Card = 10

    elif Card == "Queen":
        print("You drew a Queen!")
        Card = 10

    elif Card == "Jack":
        print("You drew a Jack!")
        Card = 10
        
    elif Card == 8:
        print(f"You drew an {Card}")
    else:

        print(f"You drew a {Card}")

    Hand.append(Card)

# Most of the differences in the DealerDraw function are grammatical, but it also automatically assigns the Ace value to the optimal choice.
def DealerDraw(Hand):
    Card = random.choice(CardList)
    if Card == "Ace":
        print("Dealer drew an Ace!")
        if sum(DealerHand) + 11 > 21:
            Card = 1
        else:
            Card = 11

    elif Card == "King":
        print("The Dealer drew a King!")
        Card = 10

    elif Card == "Queen":
        print("The Dealer drew a Queen!")
        Card = 10

    elif Card == "Jack":
        print("The Dealer drew a Jack!")
        Card = 10

    elif Card == 8:
        print(f"The Dealer drew an {Card}")

    else:
        print(f"The Dealer drew a {Card}")

    Hand.append(Card)

# =====

# This halts the code with an input to introduce the game and let the player prepare themselves.
print("------------------------------------------------------------------")
input("Welcome to the table! Press [ENTER] to draw your first two cards. ")
print("------------------------------------------------------------------")
print("")

# Pressing Enter allows the previously defined PlayerDraw function to select the two starting cards.
PlayerDraw(PlayerHand)
PlayerDraw(PlayerHand)

# By including 'while True:' in this block, the code will repeat until it crosses a break.
# These breaks will only occur when the if and elif conditions are met.
# This allows me to repeat the CardTotal calculations, blackjack/lose condition, and further course of action.
# It also prevents users from responding with an invalid input.
while True:
    CardTotal = sum(PlayerHand)
    print(f"Your current hand is worth {CardTotal}")

    if CardTotal > 21:
        print("")
        print("----------------")
        print("BUST! YOU LOSE!")
        print("----------------")
        print("")
        break

    elif CardTotal == 21:
        print("")
        print("-----------------------")
        print("BLACKJACK! You hit 21!")
        print("-----------------------")
        break

    print("")
    HitStand = input("Would you like to [HIT] or [STAND]? ").upper()
    print("")

    if HitStand == "HIT":
        PlayerDraw(PlayerHand)

    elif HitStand == "STAND":
        print("-------------------------------------")
        print(f"Your final hand is worth {CardTotal}")
        print("-------------------------------------")
        break

    else:
        print("Invalid input.")

# By assigning the total to <= 21, it allows the previous 'while True:' to run until bust, blackjack, or stand.
# Once a break is reached in the previous block, it switches to The Dealer's inputless side of the code.
# It's very similar to the player's side, just with different verbage and creating a 17 minimum total as per the rules.
if CardTotal <= 21:
    print("")
    print("It is now the dealer's turn.")
    print("")

# This is how The Dealer draws their two starting cards.
    DealerDraw(DealerHand)
    DealerDraw(DealerHand)

# By once again including 'while True:' in this block, the code will repeat until it crosses a break.
# These breaks will also only occur when the if and elif conditions are met.
# This allows me to repeat the DealerTotal calculations, along with how The Dealer handles the 17 total minimum.
    while True:
        DealerTotal = sum(DealerHand)
        print(f"The Dealer's current hand is worth {DealerTotal}")

        if DealerTotal < 17:
            print("")
            print("Dealer hits...")
            print("")
            DealerDraw(DealerHand)

        elif 17 <= DealerTotal <= 21:
            print("")
            print("Dealer stands.")
            print("")
            break

        else:
            print("")
            print("-----------------------")
            print("Dealer BUSTS! YOU WIN!")
            print("-----------------------")
            print("")
            break

# Here is where the both totals are compared and a winner is determined.
if CardTotal <= 21 and DealerTotal <= 21:
    print(f"Your final hand was worth {CardTotal}...")
    print(f"The Dealer's final hand was worth {DealerTotal}...")

    if CardTotal > DealerTotal:
        print("")
        print("-------------------------------")
        print("Your hand is greater! YOU WIN!")
        print("-------------------------------")
        print("")
        print("==================================================================================")

    elif CardTotal < DealerTotal:
        print("")
        print("------------------------------------")
        print("Dealer's hand is greater! YOU LOSE!")
        print("------------------------------------")
        print("")
        print("==================================================================================")

    else:
        print("")
        print("--------------------------")
        print("It's a push! NOBODY WINS!")
        print("--------------------------")
        print("")
        print("==================================================================================")