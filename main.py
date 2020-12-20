ids = []
null = []
closed = []
open = []
def buildGrid():
    idcount = 1
    for i in range(1, 11):
        null.append([])
        for j in range(1, 11):
            null[i - 1].append(Node(idcount, j - 1, i - 1))
            idcount += 1
class Node():
    end = (7,2)
    start = (2,7)
    def __init__(self, id, x, y, parent = None):
        self.id = id
        self.x = x
        self.y = y
        self.parent = parent
        self.hCost = self.findHCost(Node.end)
        self.gCost = self.findHCost(Node.start)
    def findHCost(self, end):
        endx = end[0]
        endy = end[1]
        if self.y == endy:
            return ((max(endx, self.x)) - (min(endx, self.x))) * 10
        elif self.x == endx:
            return ((max(endy, self.y)) - (min(endy,self.y)))* 10
        elif self.x < endx:
            junctionx = (max(endy, self.y) - min(endy, self.y))+self.x
            junctiony = endy
            if junctionx > endx:
                junctionx = endx
                if self.y < endy:
                    junctiony = self.y+(max(endx, self.x) - min(endx, self.x))
                    return (((max(junctionx, self.x)) - (min(junctionx, self.x))) * 14) - ((junctiony - endy)*10)
                else:
                    junctiony = self.y-(max(endx, self.x) - min(endx, self.x))
                    return (((max(junctionx, self.x)) - (min(junctionx, self.x))) * 14) + ((junctiony - endy) * 10)
            else:
                return ((junctionx-self.x)*14)+((endx-junctionx)*10)

        elif self.x > endx:
            junctionx = self.x-(max(endy, self.y) - min(endy, self.y))
            junctiony = endy
            if junctionx < endx:
                junctionx = endx
                if self.y < endy:
                    junctiony = self.y + (max(endx, self.x) - min(endx, self.x))
                    return (((max(junctionx, self.x)) - (min(junctionx, self.x))) * 14) - ((junctiony - endy) * 10)
                else:
                    junctiony = self.y - (max(endx, self.x) - min(endx, self.x))
                    return (((max(junctionx, self.x)) - (min(junctionx, self.x))) * 14) + ((junctiony - endy) * 10)
            else:
                return ((self.x-junctionx)*14)+((junctionx - endx)*10)
buildGrid()
for i in range(0,10):
    for j in range(0,10):
        print(null[i][j].fCost, ":", null[i][j].x, null[i][j].y)
