# Hayden Fillmore

    # 

import random

print("==================================================================================")
print("")
print("The following code was made to replicate a game of Blackjack:")
print("")

# =====

CardList = ["Ace"]
FirstCard = random.choice(CardList)
SecondCard = random.choice(CardList)
ThirdCard = random.choice(CardList)
FourthCard = random.choice(CardList)
InPlay = False

# =====

Entry = input("Welcome to the table! Press [ENTER] to draw your cards. ")

if Entry == "":
    InPlay = True

if FirstCard == "Ace":
    print(f"You drew an Ace and {SecondCard}.")
    while True:
        FirstAce = input("Would you like the Ace to be worth 1 or 11? ")
        if FirstAce == "1":
            FirstCard = 1
            StartingHand = FirstCard + SecondCard
            print(f"Your starting hand is now {StartingHand}.")
            break
        elif FirstAce == "11":
            FirstCard = 11
            StartingHand = FirstCard + SecondCard
            print(f"Your starting hand is now {StartingHand}.")
            break
        else:
            print("Invalid Value.")

elif SecondCard == "Ace":
    print(f"You drew {FirstCard} and an Ace.")
    while True:
        SecondAce = input("Would you like the Ace to be worth 1 or 11? ")
        if SecondAce == "1":
            SecondCard = 1
            StartingHand = FirstCard + SecondCard
            print(f"Your starting hand is now {StartingHand}.")
            break
        elif SecondAce == "11":
            SecondCard = 11
            StartingHand = FirstCard + SecondCard
            print(f"Your starting hand is now {StartingHand}.")
            break
        else:
            print("Invalid Value.")

elif FirstCard == "Ace" and SecondCard == "Ace":
    print("You drew two Aces.")
    while True:
        DoubleAce1 = input("Would you like the first Ace to be worth 1 or 11? ")
        if DoubleAce1 == "1":
            FirstCard = 1
            DoubleAce2 = input("Would you like the second Ace to be worth 1 or 11? ")
            if DoubleAce2 == "1":
                SecondCard = 1
                StartingHand = FirstCard + SecondCard
                print(f"Your starting hand is now {StartingHand}.")
            elif DoubleAce2 == "11":
                SecondCard = 11
                StartingHand = FirstCard + SecondCard
                print(f"Your starting hand is now {StartingHand}.")
            else:
                print("Invalid Value.")
            break
        elif DoubleAce1 == "11":
            FirstCard = 11
            DoubleAce2 = input("Would you like the second Ace to be worth 1 or 11? ")
            if DoubleAce2 == "1":
                SecondCard = 1
                StartingHand = FirstCard + SecondCard
                print(f"Your starting hand is now {StartingHand}.")
            elif DoubleAce2 == "11":
                SecondCard = 11
                StartingHand = FirstCard + SecondCard
                print(f"Your starting hand is now {StartingHand}.")    
            else:
                print("Invalid Value.")        
            break
        else:
            print("Invalid Value.")

else:
    StartingHand = FirstCard + SecondCard
    print(f"You drew a {FirstCard} and a {SecondCard}. Your starting hand is now {StartingHand}.")

