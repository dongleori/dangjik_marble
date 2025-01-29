class Player:

    money = 0
    playerNumber = 0
    playerLocation = 0


    def __init__(self):
        pass

    def setPlayerNumber(self, num):
        self.playerNumber = num

    def printNumber(self):
        print(self.playerNumber)
        
    def setPlayerLocation(self, diceAmount):
        self.playerLocation += diceAmount
        if self.playerLocation > 40:
            self.playerLocation -= 40
            self.getSalary()

    def getPlayerLocation(self):
        return self.playerLocation
    
    def getSalary(self):
        self.money += 20
        
    def getTotalIncome(self):
        return self.money