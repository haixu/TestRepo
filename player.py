
class Player:
    def __init__(self):
        self.__score = 0
        self.__totalCards = 0
        self.__hand = []

    def addCard(self,card):
        self.__hand.append(card)

    def hit(self):
        pass

    def stand(self):
        pass

    def split(self):
        pass

    def surrender(self):
        pass

class House(Player):
    def __init__(self):
        super.__init__(self)

if __name__ == "__main__":
    p = Player()
