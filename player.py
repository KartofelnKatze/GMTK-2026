import pygame

HEIGHT = 720
WIDTH = 1280

class Player :
    def __init__(self) :
        self.position = (0.5*WIDTH,0.8*WIDTH)
        self.image = ""

    def Draw(self, surface : pygame.Surface) :
        surface.blit(self.image,self.position)