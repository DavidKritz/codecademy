import random
import enum

money = 100

#Write your game of chance functions here
def headsOrTails(call, bet) : # call = Heads || Tails
    call = call.lower()
    if bet > money or bet < 0:
        return ("Bet cannot be greater than your pot or less than zero!")
    result = random.randint(1, 2) # 1 = true, 2 = false
    if result == 1:
      headOrTail = "heads"
    elif result == 2:
       headOrTail = "tails"
    if call == headOrTail:
        return bet
    else: 
        return bet*-1

def choHan(oddOrEven, bet) :
    oddOrEven = oddOrEven.lower()
    if bet > money or bet < 0:
        return ("Bet cannot be greater than your pot or less than zero!")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    totDice = dice1 + dice2
    oddsOrEvens = totDice % 2
    if (oddsOrEvens == 0 and oddOrEven == "Even") :
        return bet
    elif (oddsOrEvens != 0 and oddOrEven == "Odd") :
        return bet
    else: 
        return bet*-1

def randomCard():
    rank = random.choice( ('01:A','02:2','03:3','04:4','05:5','06:6','07:7','08:8','09:9','10:10','11:J','12:Q','13:K') )
    suit = random.choice( ('c','d','h','s') )
    suite = suitCheck(suit)
    card = rank + suite
    return card

def betRandomCard(bet):
    if bet > money or bet < 0:
        return ("Bet cannot be greater than your pot or less than zero!")
    player1 = randomCard()
    score1 = int(player1[:2])
    player2 = randomCard()
    score2 = int(player2[:2])
    if score1 > score2 :
        return bet
    elif score1 < score2 :
        return bet*-1
    else: return bet

    
def suitCheck(c):
        switcher={
                "c":'Clubs',
                "h":'Hearts',
                "d":'Diamonds',
                "s":'Spades',
             }
        return switcher.get(c,"Invalid Suit")

def roulette(bet, number = 0, ask=""):
    if bet > money or bet < 0:
        return ("Bet cannot be greater than your pot or less than zero!")
    numSpin = random.randint(1, 36)
    redColors = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    blackColors = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    result = numSpin % 2
    winning = 0
    if ask != "":
        ask = ask.lower()
        if result == 0:
            oddOrEven = "true"
        else: oddOrEven = "false"
        if ask == oddOrEven:
            winning = winning = bet*2
        elif ask != oddOrEven:
            return bet*-1
    if number == numSpin:
        winning = winning = bet*35
    else: winning = winning + bet*-1
    if (number < 13 and numSpin < 13):
        winning = winning = bet*3
    elif (number > 12 and number < 25) and (numSpin > 12 and numSpin < 25):
        winning = winning = bet*3
    elif (number > 24 and number <= 36) and (numSpin > 24 and numSpin <= 36):
        winning = winning = bet*3
    if number in redColors and numSpin in redColors:
        winning = winning = bet*2
    elif number in blackColors and numSpin in blackColors:
        winning = winning = bet*2
    return winning


#Call your game of chance functions here
money += headsOrTails("Tails", 50)
print(money)
money += choHan("Odd", 20)
print(money)
money += betRandomCard(10)
print(money)
money += roulette(20, 10)
print(money)


