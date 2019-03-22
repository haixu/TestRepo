
class Card:
  def __init__(self, value, suite):
    self.__suite = suite
    self.__shown = False
    self.__discard = False
    if value > 10:
      self.__value = 10
    else:
      self.__value = value
    if value == 11:
      self.__face = "J"
    elif value == 12:
      self.__face = "Q"
    elif value == 13:
      self.__face = "K"
    elif value == 1:
      self.__face = "A"
    else:
      self.__face = str(value)

  def discard(self):
    self.__discard = True

  def getAll(self):
    return (self.__face, self.__suite)

  def getValue(self):
    return (self.__value)

  def getSuite(self):
    return (self.__suite)

  def getFace(self):
    return (self.__face)

  def display(self):
    self.__shown = True
    print("(", end="")
    self.displayFace()
    print(",", end="")
    self.displaySuite()
    print(")", end="")

  def displayFace(self):
    print(self.__face, end="")

  def displayValue(self):
    print(self.__value, end="")

  def displaySuite(self):
    print(self.__suite, end="")


if __name__ == "__main__":
  suite = ["Heart", "Diamond", "Club", "Spade"]
  cards = [Card(i % 13 + 1, suite[i // 13]) for i in range(52)]
  for i in range(52):
    print("getAll(): ", cards[i].getAll())
    print("display(): ", end="")
    cards[i].display()
    print("")
