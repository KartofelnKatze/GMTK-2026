import pygame

class Level :
    def __init__(self) :
        self.background_images = [
            pygame.image.load("Asset/lol.png"),
            pygame.image.load("Asset/lol.png"),
            pygame.image.load("Asset/lol.png")
        ]

        self.object_images = [

        ]
        self.day = 1
        self.max_day = 5
        self.bg1_cursor = 0
        self.bg2_cursor = 1

    def level_end(self) : 
        if self.bg1_cursor >= len(self.background_images)-1 and self.bg2_cursor >= len(self.background_images)-1 :
            return True
        return False

    def reset(self) :
        self.bg1_cursor = 0
        self.bg2_cursor = 1

    def NextDay(self) :
        self.reset()
        if self.day < self.max_day :
            self.day += 1