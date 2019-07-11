#GREETINGS FROM DYLAN COX 
#HEY I ADDED A BUNCH OF SOUND HOPE THIS WORKS
#YEET 

import pygame
import time
from block_NF import Block
from gameboard_NF import GameBoard
from shapefile_NF import Shape
from gameboard_NF import gameBoardHeight

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
TURQUOISE = (0, 206, 209)

ALLCOLOURS = [WHITE, GREEN, RED, BLUE, YELLOW, MAGENTA, TURQUOISE, BLACK]

def drawScreen():
    screen.fill(BLACK)
    # pygame.drwa.rect(screen,RED[block.xpos,block.ypos,block.size,block.size],0)
    shape.draw(screen)
    nextshape.nextshape(screen)
    gameboard.draw(screen)
    scoretext = myFont.render("Score: " + str(gameboard.score),1,WHITE)
    screen.blit(scoretext,(400,400))
    linetext = myFont.render("Lines: " + str(gameboard.line),1, WHITE)
    screen.blit(linetext, (400, 450))
    leveltext = myFont.render("Level: " + str(gameboard.level), 1, WHITE)
    screen.blit(leveltext, (400, 350))
    nexttext = myFont.render("Next: ", 1, WHITE)
    screen.blit(nexttext, (400, 50))
    pygame.draw.rect(screen, WHITE, [400, 100, 6 * shape.blocklist[0].size, 6 * shape.blocklist[0].size], 1)
    gameboard.drawgrid(screen)
    powerup = myFont.render("P.U.Time: ", 1, WHITE)
    screen.blit(powerup, (400, 500))
    clockimage = pygame.image.load("clock.jpg")
    screen.blit(clockimage, (550, 495))
    powerupnum = myFont.render("X " + str(gameboard.numslowtime), 1, WHITE)
    screen.blit(powerupnum, (610, 500))
    swap = myFont.render("P.U.Swap: ", 1, WHITE)
    screen.blit(swap, (400, 550))
    swapimage = pygame.image.load("swapimage.jpg")
    screen.blit(swapimage, (550, 550))
    timenum = myFont.render("X " + str(gameboard.numswap), 1, WHITE)
    screen.blit(timenum, (600, 550))
    pygame.display.flip()

def playmainsong():
    pygame.mixer.music.load('TetrisSong.wav')
    pygame.mixer.music.play(-1)



def keyCheck():
    if shape.active == True:
        if event.key == pygame.K_LEFT:
            shape.moveLeft()
        elif event.key == pygame.K_UP:
            shape.moveClockwise()
        elif event.key == pygame.K_RIGHT:
            shape.moveRight()
        elif event.key == pygame.K_b:
            shape.moveDown()
        elif event.key == pygame.K_DOWN:
            shape.moveNotClockwise()
        elif event.key == pygame.K_SPACE:
            shape.moveDrop()
            gameboard.score += (gameBoardHeight-shape.blocklist[0].gridypos)
            dropSound.play()
        elif event.key == pygame.K_x and gameboard.numslowtime >0:
            gameboard.slowtime = True
            gameboard.numslowtime -=1
        elif event.key == pygame.K_z and gameboard.numswap >0:
            gameboard.swap = True
            gameboard.numswap -=1


if __name__ == "__main__":
    pygame.init
    size = (800, 600)

    blocksize = 25
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Avalanche-by NF")
    shape = Shape()
    nextshape = Shape()
    gameboard = GameBoard(WHITE, shape.blocklist[0].size)

    slowtimedelay = 0

    myFont = pygame.font.Font('freesansbold.ttf',30)

    delay = 0
    delaylimit = 28

    dropSound = pygame.mixer.Sound("Drop.wav")



    pygame.mixer.init()

    done = False

    started = False


    pygame.mixer.music.load('titlesong2.wav')
    pygame.mixer.music.play(-1)



while not started:
    titlescreen = pygame.image.load("titlescreen.jpg")

    pygame.display.flip()
    screen.blit(titlescreen,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            started = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                started = True
                playmainsong()



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            keyCheck()
    delay += 1

    if delay > (delaylimit-(gameboard.level * 3 )):
        shape.Falling()
        delay = 0
    if shape.active == False:

        gameboard.clearFullRows()
        shape=nextshape
        nextshape = Shape()

    if gameboard.checkLoss():
        gameboard = GameBoard(WHITE, shape.blocklist[0].size)
        nextshape = Shape()

    if gameboard.slowtime == True:
        slowtimedelay += 1
        if slowtimedelay >50:
            slowtimedelay = 0
            gameboard.slowtime = False

    if gameboard.swap == True:
        shape = nextshape
        nextshape = Shape()
        gameboard.swap = False



    drawScreen()
    time.sleep(0.01 + gameboard.slowtime*0.1)






