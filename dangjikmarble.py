

from playerInfo import Player
from diceRoller import rollDice
from marbleMap import gameMap


print("======== 당직 - 마블 ========")
totalPlayerNumber = input("플레이어 수를 입력하세요. (1~4) : ")

playerList = []
isGameStarted = True
gameMap = gameMap(totalPlayerNumber)

# 플레이어 초기화
for i in range(int(totalPlayerNumber)):
    player = Player()
    player.setPlayerNumber(i)
    playerList.append(player)

# 게임 진행

mapInfo = gameMap.loadMap()
print(mapInfo[1])

#test case
# for i in range(5):
#     diceAmount = rollDice()
#     print(diceAmount)
#     playerList[0].setPlayerLocation(diceAmount)

# print(playerList[0].getPlayerLocation())
# money = playerList[0].getTotalIncome()
# print(money)

testinput = input("주사위를 굴려주세요. (ENTER)")


if testinput == "":
    
    currentLocation = playerList[0].getPlayerLocation()
    
    myDice = rollDice()
    playerList[0].setPlayerLocation(myDice)
    diceResultMessage = f"{myDice} 이 나왔습니다."
    print(diceResultMessage)

    gameMap.setVisitedPlayer(currentLocation, playerList[0].getPlayerLocation(), 0)
    print(mapInfo)
