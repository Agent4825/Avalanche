import pygame

class Block():
    def __init__(self,colour,gridxpos,gridypos):
        self.colour=colour
        self.gridxpos=int(gridxpos)
        self.gridypos=int(gridypos)
        self.size=25

    def draw(self,screen):
        #draw a red rect on the screen
        pygame.draw.rect(screen,self.colour, [self.gridxpos*self.size, self.gridypos*self.size, self.size-1, self.size-1], 0)
