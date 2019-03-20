
class Player:
    def __init__(self):
        self.__score = 0
        self.__totalCards = 0
        self.__hand = []
        self.__totalPoint = 0

    def hit(self,card):
        if self.__totalCards <= 4:
            self.__hand.append(card)
            self.__totalCards += 1
            self.__totalPoint += card.getValue()
        else:
            return

    def stand(self):
        pass

    def split(self):
        pass

    def surrender(self):
        pass

    def showHand(self):
        for i in range(self.__totalCards):
            self.__hand[i].display()
        print("\nHand Value = %d" %self.__totalPoint)

if __name__ == "__main__":
    p = Player()
