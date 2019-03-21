from player import Player
from deck import Deck


class Game:
    def __init__(self):
        self.__dealer = Player()
        self.__player = Player()
        self.__deck = Deck()
        self.__playerTurn = 0
        self.__end = False

    def start(self):
        self.__end = False
        self.__deck.reset()
        self.__deck.shuffle()
        self.__dealer.reset()
        self.__player.reset()
        self.__dealer.hit(self.__deck.getTopCard())
        self.__playerTurn = 1
        self.__player.hit(self.__deck.getTopCard())
        self.__playerTurn = 0
        self.__dealer.hit(self.__deck.getTopCard())
        self.__playerTurn = 1
        self.__player.hit(self.__deck.getTopCard())
        self.status()

    def update(self,action):
        if self.__playerTurn == 1:
            if action == "h" and self.__player.getTotalCards() < 5:
                self.__player.hit(self.__deck.getTopCard())
            if action == "s" or self.__player.getTotalCards() == 5:
                self.__player.stand()
                self.__playerTurn = 0
        elif self.__dealer.getTotalCards() < 5:
            self.__dealer.hit(self.__deck.getTopCard())
        else:
            self.__dealer.stand()
        self.status()

    def status(self):
        print("Dealer:")
        self.__dealer.showHand()
        print("Player:")
        self.__player.showHand()
        if self.__playerTurn == 0 and self.__dealer.getPoint() >= 16:
            self.__dealer.stand()
        if self.__dealer.done():
            self.__end = True
            dealerPoint = self.__dealer.getPoint()
            playerPoint = self.__player.getPoint()
            if (dealerPoint > 21 and playerPoint > 21) or (dealerPoint == playerPoint):
                print("Push")
            elif (dealerPoint <= 21 and playerPoint > 21) or (dealerPoint <= 21 and dealerPoint > playerPoint):
                print("Dealer Win")
                self.__dealer.incScore()
            elif (playerPoint <= 21 and dealerPoint > 21) or (playerPoint <= 21 and playerPoint > dealerPoint):
                print("Player Win")
                self.__player.incScore()
            self.showScore()

    def showScore(self):
        print("Dealer Score:%d\tPlayer Score:%d"%(self.__dealer.getScore(),self.__player.getScore()))

    def end(self):
        return (self.__end)

    def dealerTurn(self):
        if self.__playerTurn == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    game = Game()
    game.start()
    again = True
    while again:
        while not game.end():
            if not game.dealerTurn():
                action = input("What Do You Want To Do (hit/stand)?")
            game.update(action)
        yesno = input("Do You Want To Play Again (yes/no)?")
        if yesno == "y":
            again = True
            game.start()
        else:
            again = False
