
class Card:
    def __init__(self,value,suite):
        self.__value = value
        self.__suite = suite
        self.__shown = false

    def getAll(self):
        return (self.__value,self.__suite)

    def getValue(self):
        return (self.__value)

    def getSuite(self):
        return (self.__suite)

    def display(self):
        self.__shown = true
        print("(",end="")
        self.displayValue()
        print(",",end="")
        self.displaySuite()
        print(")",end="")

    def displayValue(self):
        if self.__value == 1:
            print("A",end="")
        elif self.__value == 11:
            print("J",end="")
        elif self.__value == 12:
            print("Q",end="")
        elif self.__value == 13:
            print("K",end="")
        else:
            print(self.__value,end="")

    def displaySuite(self):
        print(self.__suite,end="")

if __name__ == "__main__":
    suite = ["Heart","Diamond","Club","Spade"]
    cards = [Card(i%13 + 1, suite[i//13]) for i in range(52)]
    for i in range(52):
        print("getAll(): ",cards[i].getAll())
        print("display(): ",end="")
        cards[i].display()
        print("")
