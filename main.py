def getCardFromIndexNum(game, handNumber, i):
  if(i < 5):
    return game.communityCards[i];
  elif (i == 5):
    return game.hands[handNumber][0];
  return game.hands[handNumber][1];

def checkNotFoundYetPair(num, alreadyFoundPairNumbers):
  for x in alreadyFoundPairNumbers:
    if(x == num):
      return 0;
  return 1;

def checkNumSame(game, handNumber, alreadyFoundPairNumbers):
  retNum = 0
  retTot = 0
  for i in range (6):
    carda = getCardFromIndexNum(game, handNumber, i)
    print(carda.num)
    for j in range(i, 6):
      cardb = getCardFromIndexNum(game, handNumber, j)
      if(carda.num == cardb.num & checkNotFoundYetPair(carda.num, alreadyFoundPairNumbers)):
        retTot += 1
        retNum = carda.num
        alreadyFoundPairNumbers.append(carda.num)

  
  return retTot, retNum;

def analyzeSingleHand(game, handNumber):
  alreadyFoundPairNumbers = []

  if (checkNumSame(game, handNumber, alreadyFoundPairNumbers)):
    return 1;
  return 0;

class Game:
  def __init__(self):
    self.communityCards = [Card(0,0), Card(0,0), Card(0,0), Card(0,0), Card(0,0)]
    self.hands = []
  
  def addCardToCommunity(self, card, index):
    self.communityCards[index].suit = card.suit
    self.communityCards[index].num = card.num
  
  def addHand(self, card1, card2):
    toAdd = [card1, card2]
    self.hands.append(toAdd)

class Card:
  def __init__(self, suit, num):
    self.suit = suit
    self.num = num

g = Game()
h1 = Card(1, 13)
h2 = Card(1, 13)
c1 = Card(2, 11)
c2 = Card(2, 11)
c3 = Card(2, 11)
c4 = Card(2, 13)
c5 = Card(2, 13)

g.addCardToCommunity(c1, 0)
g.addCardToCommunity(c2, 0)
g.addCardToCommunity(c3, 0)
g.addCardToCommunity(c4, 0)
g.addCardToCommunity(c5, 0)
g.addHand(h1, h2)

print(checkNumSame(g, 0, []))