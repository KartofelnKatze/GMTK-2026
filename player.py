import pygame

HEIGHT = 720
WIDTH = 1280

class Player :
    def __init__(self) :
        self.position = (-100,0.8*HEIGHT)
        self.x_max = 0.5*WIDTH-25
        self.speed = 100
        self.image = pygame.image.load("Asset/player_face.png")

    def update(self, delta_time) :
        if not self.MaxReached() :
            self.position = (
                self.position[0] + self.speed*delta_time,
                self.position[1]
            )
    def MaxReached(self) :
        if self.position[0] >= self.x_max :
            return True
        return False

    def Reset(self) :
        self.__init__()
    def Draw(self, surface : pygame.Surface) :
        #rect = pygame.Rect(self.position[0],self.position[1],50,50)
        #pygame.draw.rect(surface,(255,0,0,255),rect)
        surface.blit(self.image, self.position)