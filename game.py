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
        self.__deck.shuffle()
        self.__dealer.hit(self.__deck.getTopCard())
        self.__playerTurn = 1
        self.__player.hit(self.__deck.getTopCard())
        self.__playerTurn = 0
        self.__dealer.hit(self.__deck.getTopCard())
        self.__playerTurn = 1
        self.__player.hit(self.__deck.getTopCard())
        self.status()

    def update(self,action):
        if(action == "H"):
            if self.__playerTurn == 0:
                self.__dealer.hit(self.__deck.getTopCard())
            else:
                self.__player.hit(self.__deck.getTopCard())
        elif(action == "S"):
            if self.__playerTurn == 0:
                self.__dealer.stand(self.__deck.getTopCard())
            else:
                self.__player.stand(self.__deck.getTopCard())
        self.status()

    def status(self):
        print("Dealer:")
        self.__dealer.showHand()
        print("Player:")
        self.__player.showHand()
        if self.__dealer.getScore() > self.__player.getScore():
            self.__end = True
        if self.__player.getScore() > self.__dealer.getScore():
            self.__end = True

    def end(self):
        return (self.__end)


if __name__ == "__main__":
    game = Game()
    game.start()
    while not game.end():
        action = input("What Do You Want To Do (Hit/Stand/Surrender)?")
        game.update(action)
