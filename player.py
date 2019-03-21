
class Player:
    def __init__(self):
        self.__score = 0
        self.reset()

    def reset(self):
        self.__totalCards = 0
        self.__totalPoint = 0
        self.__stand = False
        self.__hand = []

    def hit(self, card):
        if self.__totalCards <5 and (not self.__stand):
            self.__hand.append(card)
            self.__totalCards += 1
            self.__totalPoint += card.getValue()
        else:
            self.__stand = True

    def stand(self):
        self.__stand = True

    def split(self):
        pass

    def surrender(self):
        self.__stand = True

    def showHand(self):
        for i in range(self.__totalCards):
            self.__hand[i].display()
        print("\nHand Value = %d" % self.__totalPoint)

    def done(self):
        return(self.__stand)

    def getTotalCards(self):
        return(self.__totalCards)

    def getPoint(self):
        return(self.__totalPoint)

    def incScore(self):
        self.__score += 1

    def getScore(self):
        return(self.__score)

if __name__ == "__main__":
    p = Player()
    p.showHand()
