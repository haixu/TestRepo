from datetime import datetime
import random
from card import Card


class Deck:
  __suite = ["heart", "diamond", "club", "spade"]
  __suiteSize = 13
  __deckSize = 52

  def __init__(self):
    self.__cards = [Card(i % Deck.__suiteSize + 1, Deck.__suite[i
                                                                // Deck.__suiteSize]) for i in range(Deck.__deckSize)]
    self.__topCard = 0
    self.__bottomCard = Deck.__deckSize - 1

  def getAll(self):
    for i in range(self.__deckSize):
      self.__cards[i].getAll()

  def getValue(self):
    for i in range(self.__deckSize):
      self.__cards[i].getValue()

  def getSuite(self):
    for i in range(self.__deckSize):
      self.__cards[i].getSuite()

  def display(self):
    for i in range(self.__deckSize):
      self.__cards[i].display()

  def displayValue(self):
    for i in range(self.__deckSize):
      self.__cards[i].displayValue()

  def displaySuite(self):
    for i in range(self.__deckSize):
      self.__cards[i].displayValue()

  def shuffle(self):
    random.seed(datetime.now())
    for i in range(51, -1, -1):
      index = random.randint(0, i)
#            print("%d picked" % index,end=":")
#            print("cards[%s]=" % index,end="")
#            print(self.__cards[index].getAll(),end=";")
#            print("%s cards[%s]=" %(i,i),end="")
#            print(self.__cards[i].getAll())

      card = self.__cards[index]
      self.__cards[index] = self.__cards[i]
      self.__cards[i] = card

#            print("Swapped:cards[%s]="%index,end="")
#            print(self.__cards[index].getAll(),end=";")
#            print("cards[%s]="%i,end="")
#            print(self.__cards[i].getAll())
      # input("")

  def reset(self):
    self.__topCard = 0
    self.__bottomCard = Deck.__deckSize

  def getTopCard(self):
    if self.__topCard <= self.__bottomCard:
      self.__topCard += 1
      return(self.__cards[self.__topCard - 1])
    else:
      return

  def getBottomCard(self):
    if self.__bottomCard >= self.__topCard:
      self.__bottomCard -= 1
      return(self.__cards[self.__bottomCard + 1])
    else:
      return


if __name__ == "__main__":
  d = Deck()
  d.display()
  print("")
  d.shuffle()
  d.display()
  print("")
  d.reshuffle()
  d.display()
