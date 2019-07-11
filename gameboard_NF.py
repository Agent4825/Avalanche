import pygame


gameBoardWidth=12
gameBoardHeight=20
activeBoardSpot = [[0 for y in range(gameBoardHeight)]for x in range(gameBoardWidth)]
activeBoardColour=[[0 for y in range(gameBoardHeight)] for x in range(gameBoardWidth)]

pygame.init()
lineSound = pygame.mixer.Sound("clearBarSound.wav")

# colours
BLACK = (0, 0, 0)
GREY = (70, 70, 70)



class GameBoard():
    def __init__(self,colour,blocksize):
        self.bordercolour = colour
        self.multiplier = blocksize
        self.score = 0
        self.line = 0
        self.templeveltracker = 0
        self.level = 1
        self.slowtime = False
        self.swap = False
        self.numswap = 0
        self.numslowtime = 0
        for i in range(gameBoardWidth):
            for j in range(gameBoardHeight):
                activeBoardSpot[i][j]=False
                activeBoardColour[i][j]=(0,0,0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.bordercolour,[0, 0, gameBoardWidth * self.multiplier, gameBoardHeight * self.multiplier], 1)

        for i in range(gameBoardWidth):
            for j in range(gameBoardHeight):
                if activeBoardSpot[i][j]:
                    pygame.draw.rect(screen, activeBoardColour[i][j],[i * self.multiplier, j * self.multiplier, self.multiplier - 1,self.multiplier - 1], 0)

    def checkLoss(self):
        for i in range(gameBoardWidth):
            if activeBoardSpot[i][0]:
                return True
        return False

    def fullRow(self, rowNum):
        for i in range(gameBoardWidth):
            if activeBoardSpot[i][rowNum] == False:
                return False
        return True


    def clearFullRows(self):
        for j in range(gameBoardHeight):
            if self.fullRow(j):
                lineSound.play()
                self.score += 100
                self.line += 1
                self.templeveltracker += 1
                if self.templeveltracker == 5:
                    self.level += 1
                    self.numslowtime += 1
                    self.numswap += 1
                    self.templeveltracker = 0
                    
                for c in range(j,1,-1):
                    for i in range(gameBoardWidth):
                        activeBoardSpot[i][c] = activeBoardSpot[i][c-1]
                        activeBoardColour[i][c] = activeBoardColour[i][c-1]
                for r in range(gameBoardWidth):
                    activeBoardSpot[r][0] = False
                    activeBoardColour[r][0] = BLACK
                    
                    
    def drawgrid(self, screen):
        for i in range(gameBoardWidth):
            for j in range(gameBoardHeight):
                pygame.draw.rect(screen, GREY, [i * self.multiplier, j * self.multiplier, 25, 25], 1)
                
        