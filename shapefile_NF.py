from block_NF import Block
from gameboard_NF import gameBoardWidth
from gameboard_NF import gameBoardHeight
import random
from gameboard_NF import activeBoardSpot
from gameboard_NF import activeBoardColour
import pygame

#colours
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
MAGENTA=(255,0,255)
TURQUOISE=(0,206,209)

ALLCOLOURS = [WHITE, GREEN, RED, BLUE, YELLOW, MAGENTA, TURQUOISE, BLACK]

zShape = [[(gameBoardWidth/2)-1,0],[(gameBoardWidth/2)-2,0],[(gameBoardWidth/2)-1,1],[gameBoardWidth/2,1]]
sShape = [[(gameBoardWidth/2)-1,0],[gameBoardWidth/2,0],[(gameBoardWidth/2)-2,1],[(gameBoardWidth/2)-1,1]]
lineShape = [[(gameBoardWidth/2)-1,0],[(gameBoardWidth/2)-2,0],[(gameBoardWidth/2),0],[(gameBoardWidth/2)+1,0]]
squareShape = [[(gameBoardWidth/2)-1,0], [gameBoardWidth/2,0], [gameBoardWidth/2,1],[(gameBoardWidth/2)-1,1]]
lShape = [[(gameBoardWidth/2)-1,1], [(gameBoardWidth/2)-1,0],[(gameBoardWidth/2)-1,2],[gameBoardWidth/2,2]]
mlShape = [[(gameBoardWidth/2),1], [(gameBoardWidth/2),0],[(gameBoardWidth/2),2],[(gameBoardWidth/2)-1,2]]
tShape = [[(gameBoardWidth/2)-1,1],[(gameBoardWidth/2)-1,0],[(gameBoardWidth/2),1],[(gameBoardWidth/2)-2,1]]
ALLSHAPES = [zShape, sShape, lineShape, squareShape, lShape, mlShape, tShape]

class Shape():
    def __init__ (self):
        self.numblocks = 4
        randomNum = random.randrange(7)
        self.shape = ALLSHAPES[randomNum]
        randomNum = random.randrange(7)
        self.colour = ALLCOLOURS[randomNum]
        self.blocklist = []
        self.active = True
        for i in range(self.numblocks):
            self.blocklist.append(Block(self.colour, self.shape[i][0], self.shape[i][1]))
    def draw(self,screen):
        for i in range(self.numblocks):
            self.blocklist[i].draw(screen)

    def moveLeft(self):
        blocked = False
        for i in range(self.numblocks):
            if self.blocklist[i].gridxpos == 0 or activeBoardSpot [self.blocklist[i].gridxpos-1][self.blocklist[i].gridypos]== True:
                blocked = True
        if blocked == False:
            for i in range(self.numblocks):
                self.blocklist[i].gridxpos -=1

    def moveRight(self):
        blocked = False
        for i in range(self.numblocks):
            if self.blocklist[i].gridxpos == gameBoardWidth-1 or activeBoardSpot[self.blocklist[i].gridxpos+1] [self.blocklist[i].gridypos] == True:
                blocked = True
        if blocked == False:
            for i in range(self.numblocks):
                self.blocklist[i].gridxpos +=1

    def moveDown(self):
        blocked = False
        for i in range(self.numblocks):
            if self.blocklist[i].gridypos == gameBoardHeight-1 or activeBoardSpot[self.blocklist[i].gridxpos][self.blocklist[i].gridypos+1] == True:
                blocked = True
        if blocked == False:
            for i in range(self.numblocks):
                self.blocklist[i].gridypos +=1

    def moveClockwise(self):

        if self.shape != squareShape:
            newBlockX = [0,0,0,0]
            newBlockY = [0,0,0,0]
            canTurn = True
            for i in range(self.numblocks):

                newBlockX[i]=-(self.blocklist[i].gridypos-self.blocklist[0].gridypos)+self.blocklist[0].gridxpos
                newBlockY[i]=(self.blocklist[i].gridxpos-self.blocklist[0].gridxpos)+self.blocklist[0].gridypos

                if newBlockX[i] < 0 or newBlockX[i] == gameBoardWidth:
                    canTurn = False
                elif newBlockY[i] < 0 or newBlockY[i] == gameBoardHeight:
                    canTurn = False
                elif activeBoardSpot[newBlockX[i]][newBlockY[i]]:
                    canTurn = False


            if canTurn == True:
                for i in range(self.numblocks):
                    self.blocklist[i].gridxpos=newBlockX[i]
                    self.blocklist[i].gridypos=newBlockY[i]

    def moveNotClockwise(self):
        canTurn = True
        if self.shape != squareShape:
            newBlockX = [0,0,0,0]
            newBlockY = [0,0,0,0]
            for i in range(self.numblocks):

                newBlockX[i]=(self.blocklist[i].gridypos-self.blocklist[0].gridypos)+self.blocklist[0].gridxpos
                newBlockY[i]=-(self.blocklist[i].gridxpos-self.blocklist[0].gridxpos)+self.blocklist[0].gridypos

                if newBlockX[i] < 0 or newBlockX[i] == gameBoardWidth:
                    canTurn = False
                elif newBlockY[i] < 0 or newBlockY[i] == gameBoardHeight:
                    canTurn = False
                elif activeBoardSpot[newBlockX[i]][newBlockY[i]]:
                    canTurn = False

            if canTurn == True:
                for i in range(self.numblocks):
                    self.blocklist[i].gridxpos=newBlockX[i]
                    self.blocklist[i].gridypos=newBlockY[i]

    def Falling(self):
        for i in range(self.numblocks):
            if self.blocklist[i].gridypos == gameBoardHeight-1 or activeBoardSpot[self.blocklist[i].gridxpos][self.blocklist[i].gridypos+1]:
                self.hitBottom()
        for i in range(self.numblocks):
            if self.active:

                self.blocklist[i].gridypos += 1

    def hitBottom(self):
        for i in range(self.numblocks):
            activeBoardSpot[self.blocklist[i].gridxpos][self.blocklist[i].gridypos] = True
            activeBoardColour[self.blocklist[i].gridxpos][self.blocklist[i].gridypos] = self.blocklist[i].colour
        self.active = False

    def moveDrop(self):
        while self.active == True:
            for i in range(self.numblocks):
                if self.blocklist[i].gridypos == gameBoardHeight-1 or activeBoardSpot[self.blocklist[i].gridxpos][self.blocklist[i].gridypos+1] == True:
                    self.hitBottom()

            for i in range(self.numblocks):
                if self.active == True:
                    self.blocklist[i].gridypos += 1
                    
    def nextshape(self,screen):
        for i in range(self.numblocks):
            pygame.draw.rect(screen, self.blocklist[i].colour, [self.blocklist[i].gridxpos
                                                                * self.blocklist[i].size + 325, self.blocklist[i].gridypos * self.blocklist[i].size + 
                                                                150, self.blocklist[i].size - 1, self.blocklist[i].size - 1], 0)
