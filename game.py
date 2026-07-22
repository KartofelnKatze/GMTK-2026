import pygame

class Game :
    def __init__(self, width : float, height : float) :
        self.width = width
        self.height = height

        self.background = pygame.image.load("Asset/lol.png")
        self.background1_coordinate = (0,0)
        self.background2_coordinate = (-width,0)
        self.background_speed = 20

        self.clock = pygame.time.Clock()

        self.dt = self.clock.tick(60) / 1000

    def Scrolling(self) :
        if(self.background1_coordinate[0] > self.width) :
            self.background1_coordinate = (-self.width,0)
        if(self.background2_coordinate[0] > self.width) :
            self.background2_coordinate = (-self.width,0)
        self.background1_coordinate = (
            self.background1_coordinate[0] + self.background_speed*self.dt,
            self.background1_coordinate[1]
        )
        self.background2_coordinate = (
            self.background2_coordinate[0] + self.background_speed*self.dt,
            self.background2_coordinate[1]
        )

    def update(self) :
        self.Scrolling()
        self.dt = self.clock.tick(60) / 1000

    def Draw(self, surface : pygame.Surface) :
        surface.blit(self.background,self.background1_coordinate)
        surface.blit(self.background,self.background2_coordinate)