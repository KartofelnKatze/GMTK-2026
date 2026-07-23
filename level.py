import pygame
import clock

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
        self.countdown = None
        self.bg1_cursor = 0
        self.bg2_cursor = 1
        self.SelectCountDown()

        self.timer = clock.Timer()
        self.font = pygame.font.Font(None, 26)

    def level_end(self) : 
        if self.bg1_cursor >= len(self.background_images)-1 and self.bg2_cursor >= len(self.background_images)-1 :
            return True
        return False
    
    def TimerEnd(self) :
        if self.timer.time_passed > 60 and self.timer.run_state :
            return True
        return False
    
    def reset(self) :
        self.bg1_cursor = 0
        self.bg2_cursor = 1

    def NextDay(self) :
        self.reset()
        if self.day < self.max_day :
            self.day += 1

    def SelectCountDown(self) :
        if self.day == 1 :
            self.countdown = 60

    def Draw(self, surface : pygame.Surface) : 
        time_remaining = self.countdown - self.timer.time_passed
        if time_remaining < 0 :
            time_remaining = 0
        f_string = f"Time remaining : {time_remaining}"
        text_surface = self.font.render(f_string, True, (0, 0, 0))
        surface.blit(text_surface, (25,25))
        f_string2 = f"Day : {self.day}"
        text_surface = self.font.render(f_string2, True, (0, 0, 0))
        surface.blit(text_surface, (25,50))