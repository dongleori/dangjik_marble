

from playerInfo import Player
from diceRoller import rollDice
from marbleMap import gameMap


print("======== 당직 - 마블 ========")
playerNumber = input("플레이어 수를 입력하세요. (1~4) : ")


isGameStarted = True

gameMap = gameMap()

playerDice = rollDice()

cnt = 0

while (isGameStarted):
    while (playerDice != 0):
        gameMap.printMap()
        playerDice = 0
        cnt = cnt + 1
        print(cnt)
        
    ham = input("굴려~")
    if (ham == ""):
        playerDice = rollDice()
        print("dice : ", playerDice)

# 플레이어 초기화
p1 = Player()
p1.setNumber(1)
print(p1.playerNumber)
p1.printNumber()

# 게임 진행

