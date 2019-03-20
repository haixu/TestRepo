from player import Player
from deck import Deck

class Game:
    def __init__(self):
        self.__dealer = Player()
        self.__player = Player()
        self.__deck = Deck()

    def start(self):
        self.__deck.shuffle()
        self.__dealer.hit(self.__deck.getTopCard())
        self.__player.hit(self.__deck.getTopCard())
        self.__dealer.hit(self.__deck.getTopCard())
        self.__player.hit(self.__deck.getTopCard())
        self.status()

    def status(self):
        print("Dealer:")
        self.__dealer.showHand()
        print("Player:")
        self.__player.showHand()

if __name__ == "__main__":
    game = Game()
    game.start()
