map = """
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| 출발           | 타이베이       | 황금열쇠        | 마닐라         | 제주도         | 사회복지       | 싱가포르       | 방콕           | 카이로         | 이스탄불       | 무인도            |
|                | 5만원          |                 | 8만원          | 9만원          | 기금접수       | 10만원         | 10만원         | 12만원         | 13만원         |             |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-
| 하와이         |                                                                                                                                                | 스톡홀름          |
| 28만원        |                                                                                                                                                 | 16만원           |
+-----------------+                                                                                                                                             +-----------------+
| 무인도         |                                                                                                                                                | 코펜하겐          |
|                |                                                                                                                                                | 16만원           |
+-----------------+                                                                                                                                                +-----------------+
| 아테네         |                                                                                                                                                | 사회복지          |
| 14만원        |                                                                                                                                                | 기금수령           |
+-----------------+                                                                                                                                                +-----------------+
| 황금열쇠        |                                                                                                                                                | 베른             |
|                |                                                                                                                                                | 18만원           |
+-----------------+                                                                                                                                                +-----------------+
| 시드니         |                                                                                                                                                | 도쿄              |
| 26만원        |                                                                                                                                                | 30만원            |
+-----------------+                                                                                                                                                +-----------------+
| 상파울루       |                                                                                                                                                | 파리              |
| 24만원        |                                                                                                                                                | 32만원            |
+-----------------+                                                                                                                                                +-----------------+
| 부에노스       |                                                                                                                                                | 런던              |
| 아이레스       |                                                                                                                                                | 36만원             |
+-----------------+-------------------------------------------------------------------------+-----------------++------------------------------------------------------------------+
| 오타와         | 부에노스       | 황금열쇠        | 상파울루       | 시드니         | 무인도탈출     | 런던           | 뉴욕           | 서울           | 파리           | 로마               |
| 20만원        | 아이레스       |                 | 24만원        | 26만원        |                 | 36만원        | 38만원        | 40만원        | 32만원        | 34만원              |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+

"""

"""
1. f-strings (Python 3.6 이상)

name = "Alice"
age = 30
message = f"Hello, my name is {name} and I am {age} years old."
print(message)
2. str.format() 메서드

name = "Alice"
age = 30
message = "Hello, my name is {} and I am {} years old.".format(name, age)
print(message)
3. 퍼센트(%) 포맷팅

name = "Alice"
age = 30
message = "Hello, my name is %s and I am %d years old." % (name, age)
print(message)
이 세 가지 방법 중에서 f-strings가 가장 최신의 방법이며, 가독성이 좋고 사용하기 편리합니다. 필요에 따라 적절한 방법을 선택하여 사용하시면 됩니다.

+-----------------++-----------------++-----------------+
| 하와이   <1>    |  | 하와이   <1>    | | 하와이   <1>    |
| 28만원 ★■▲   | | 28만원 ★■▲   | | 28만원 ★■▲   |
| [2] [3]  (20만원) | | [2] [3]  (20만원) | | [2] [3]  (20만원) |
+-----------------++-----------------++-----------------+
| 하와이   <1>    |                         | 하와이   <1>    |
| 28만원 ★■▲   |                         | 28만원 ★■▲   |
| [2] [3]  (20만원) |                         | [2] [3]  (20만원) |
+-----------------++-----------------++-----------------+
| 하와이   <1>    |  | 하와이   <1>    | | 하와이   <1>    |
| 28만원 ★■▲   | | 28만원 ★■▲   | | 28만원 ★■▲   |
| [2] [3]  (20만원) | | [2] [3]  (20만원) | | [2] [3]  (20만원) |
+-----------------++-----------------++-----------------+


"""

mapInfo = [
    {'areaName' : 'a1', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a2', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a3', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a4', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a5', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a6', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a7', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a8', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a9', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a10', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a11', 'visitedPlayer' : [], 'areaOwner' : 'none'},
    {'areaName' : 'a12', 'visitedPlayer' : [], 'areaOwner' : 'none'}
]

class gameMap():
    currentMap = ""
    currentMapInfo = ""
    
    def __init__(self, totalPlayerNumber):
        self.currentMap = map
        self.currentMapInfo = mapInfo
        
        for i in range(int(totalPlayerNumber)):
            self.currentMapInfo[0]['visitedPlayer'].append(i)

    def printMap(self):
        print(self.currentMap)
        
    def loadMap(self):
        return self.currentMapInfo
    
    def setVisitedPlayer(self, previousPlayerLocation, currentPlayerLocation, playerNumber):
        self.currentMapInfo[previousPlayerLocation]['visitedPlayer'].remove(playerNumber)
        self.currentMapInfo[currentPlayerLocation]['visitedPlayer'].append(playerNumber)
        