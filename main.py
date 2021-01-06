import pygame
ids = []
grid = []
closed = []
open = []
path = []
class Node():
    end = (-1,-1)
    start = (-1,-1)
    def __init__(self, id, x, y, parent = None):
        global grid
        self.isObstacle = False
        self.id = id
        self.x = x
        self.y = y
        self.parent = parent
        self.hCost = 0
        self.gCost = None
        self.fCost = None
        grid[self.y].append(self)
    def addClosed(self):
        global closed
        closed.append(self)
    def addOpen(self):
        global open
        open.append(self)
    def getPath(self):
        global path
        if self.parent != None:
            path.append((self))
            self.parent.getPath()
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
def findAdjacent(x, y):
    for dx in range(-1, 2):
        for dy in range(-1,2):
            if dx != 0 or dy != 0:
                if (x + dx > -1) and (x+dx < int(len(grid[0]))) and (y+dy > -1) and (y+dy < int(len(grid))):
                    grid[y+dy][x+dx].hCost = grid[y+dy][x+dx].findHCost(Node.end)
                    if grid[y+dy][x+dx] not in closed and grid[y+dy][x+dx].isObstacle == False:
                        if (dx == -1 or dx == 1) and (dy == -1 or dy == 1):
                            gcost = grid[y][x].gCost + 14
                            fcost = gcost + grid[y+dy][x+dx].hCost

                        else:
                            gcost = grid[y][x].gCost + 10
                            fcost = gcost + grid[y+dy][x+dx].hCost
                        if grid[y+dy][x+dx].parent != None:
                            if fcost < grid[y+dy][x+dx].fCost:
                                grid[y+dy][x+dx].parent = grid[y][x]
                                grid[y+dy][x+dx].gCost = gcost
                                grid[y+dy][x+dx].fCost = fcost
                        else:
                            grid[y+dy][x+dx].parent = grid[y][x]
                            grid[y+dy][x+dx].gCost = gcost
                            grid[y+dy][x+dx].fCost = fcost
                            grid[y+dy][x + dx].addOpen()
def buildGrid():
    global grid
    idcount = 1
    for i in range(1, 51):
        grid.append([])
        for j in range(1, 51):
            Node(idcount, j - 1, i - 1)
            idcount += 1
def windowToBoardCoord(win_x, win_y):
    board_x = win_x // (WINWIDTH // 50)
    board_y = win_y // (WINWIDTH // 50)
    return board_x, board_y
def drawRect(color, row, column):
    pygame.draw.rect(win, (color),
                    (((column * (WINWIDTH) // 50)), ((row * (WINWIDTH) // 50))
                    , (WINWIDTH - 24) // 50, (WINHEIGHT - 24) // 50))
def bgupdategrid(visualizer):
    for row in range(0,50):
        for column in range(0,50):
            CHOSENCOLOR = WHITE
            if visualizer == True:
                if grid[row][column].isObstacle:
                    CHOSENCOLOR = BLACK
                elif grid[row][column] in path:
                    CHOSENCOLOR = BLUE
                elif (row == Node.start[1] and column == Node.start[0]) or (row == Node.end[1] and column == Node.end[0]): #(row == Node.start[0] or row == Node.end[0]) and (column == Node.end[1] or column == Node.start[1]):
                    CHOSENCOLOR = BLUE
                elif grid[row][column] in open:
                    CHOSENCOLOR = GREEN
                elif grid[row][column] in closed:
                    CHOSENCOLOR = RED
            else:
                if grid[row][column].isObstacle:
                    CHOSENCOLOR = BLACK
                elif grid[row][column] in path:
                    CHOSENCOLOR = BLUE
                elif (row == Node.start[1] and column == Node.start[0]) or (row == Node.end[1] and column == Node.end[0]): #(row == Node.start[0] or row == Node.end[0]) and (column == Node.end[1] or column == Node.start[1]):
                    CHOSENCOLOR = BLUE
                    
            drawRect(CHOSENCOLOR, row, column)

buildGrid()
WINWIDTH = 800
WINHEIGHT = 800
WHITE = (200,200,200)
BLACK = (100,100,100)
GREEN = 124,252,0
RED = (255,0,0)
BLUE = (0,0,255)
startset = False
endset = False
doPathFind = False
drawObstacle = False
visualizer = False
pygame.init()
win = pygame.display.set_mode((WINWIDTH,WINHEIGHT))
pygame.display.set_caption("A* Pathfinding Visualizer")
run = True
currentnode = None
end = None
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if startset == False and endset == False:
                mouse_x, mouse_y = event.pos
                board_x, board_y = windowToBoardCoord(mouse_x, mouse_y)
                Node.start = (board_x, board_y)
                currentnode = grid[Node.start[1]][Node.start[0]]
                closed.append(grid[Node.start[1]][Node.start[0]])
                grid[Node.start[1]][Node.start[0]].gCost = 0
                startset = True
            elif startset == True and endset == False:
                mouse_x, mouse_y = event.pos
                board_x, board_y = windowToBoardCoord(mouse_x, mouse_y)
                Node.end = (board_x, board_y)
                endset = True
                end = grid[Node.end[1]][Node.end[0]]
            elif startset == True and endset == True:
                drawObstacle = True
        elif pygame.mouse.get_pressed()[0] and drawObstacle == True:
            mouse_x, mouse_y = event.pos
            board_x, board_y = windowToBoardCoord(mouse_x, mouse_y)
            grid[board_y][board_x].isObstacle = True
            grid[board_y][board_x+1].isObstacle = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if startset == True and endset == True:
                    doPathFind = True
            elif event.key == pygame.K_v:
                visualizer = True
            elif event.key == pygame.K_c and doPathFind == False:
                open.clear()
                closed.clear()
                path.clear()
                grid.clear()
                startset = False
                endset = False
                Node.end = (-1,-1)
                Node.start = (-1,-1)
                buildGrid()
    if doPathFind == True:
        if end not in closed:
            findAdjacent(currentnode.x, currentnode.y)
            opendict = {}
            hdict = {}
            for i in open:
                opendict[i] = i.fCost
            fmin = min(opendict.values()) 
            fminlist = [key for key in opendict if opendict[key] == fmin]
            minlist = []
            for i in fminlist:
                hdict[i] = i.hCost
            hmin = min(hdict.values())
            if int(len(fminlist)) > 1:
                hminlist = [key for key in hdict if hdict[key] == hmin]
                minlist.append(hminlist[0])
            else:
                minlist.append(fminlist[0])
            open.remove(grid[minlist[0].y][minlist[0].x])
            closed.append(grid[minlist[0].y][minlist[0].x])
            currentnode = grid[minlist[0].y][minlist[0].x]
            bgupdategrid(visualizer)
        else:
            grid[currentnode.y][currentnode.x].getPath()
            doPathFind = False
    bgupdategrid(visualizer)
    pygame.display.flip()