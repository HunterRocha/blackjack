import random 


print("Welcome to the first CS110 Blackjack Tournamnet! ")



def main():
    userHand = 0 
    opponentHand = 0
    dealerHand = 0
    i = 1
    while i == 1:
        play = int(input("Do you want to 1.Hit 2.Exit or 3.Fold"))
        if play == 1:
            userHand += getCard(userHand)
            opponentHand += getCard(opponentHand)
            dealerHand += getCard(dealerHand)
            print("Your Hand: ", userHand)
            compareHands(userHand,opponentHand,dealerHand)
        elif play == 2:
            print("you are exiting. Have a great day :)")
            i +=1
        elif play == 3:
            print("You folded. Thanks for playing :-) ")
            i +=1





def getCard(userHand):
    random_card = random.randint(1,13)
    for card in range(14):
        if card == random_card:
            return card
            
        


def compareHands(userHand, opponentHand,dealerHand):
    if dealerHand >= 17: 
        if dealerHand < 21 and userHand < dealerHand or opponentHand > dealerHand:
            print("you lose")
            print("Opponent Hand: ", opponentHand)
            print("Your Hand: ", userHand)
            print("Dealer Hand: ", dealerHand)
        elif dealerHand > 21 and opponentHand < userHand and userHand < 21:
            print("you win")
            print("Opponent Hand: ", opponentHand)
            print("Your Hand: ", userHand)
            print("Dealer Hand: ", dealerHand)
        elif dealerHand < 21 and userHand > dealerHand and userHand < userHand:
            print("you win")
            print("Opponent Hand: ", opponentHand)
            print("Your Hand: ", userHand)
            print("Dealer Hand: ", dealerHand)
            exit()
        exit()
    elif opponentHand > 21:
        print("you win!")
        print("Opponent Hand: ", opponentHand)
        print("Dealer Hand", dealerHand)
        exit()
    elif userHand > 21:
        print("you lose!")
        print("Opponent Hand: ", opponentHand)
        print("Dealer Hand", dealerHand)
        exit()
    elif opponentHand == 21:
        print("you lose")
        print("Opponent Hand: ", opponentHand)
        print("Dealer Hand", dealerHand)
        exit()
    elif opponentHand > 21 and userHand > 21:
        print("you lose")
        print("Opponent Hand: ", opponentHand)
        print("Dealer Hand", dealerHand)
        exit()
    elif userHand == 21:
        print("BLACKJACK!")
        print("Opponent Hand: ", opponentHand)
        print("Dealer Hand", dealerHand)
        exit()
    elif userHand == 21 or dealerHand == 21:
        print("you lose")
        print("your hand: ", userHand)
        print("Opponent Hand: ", opponentHand)
        print("Dealer Hand", dealerHand)
        exit()



main()
    