import pygame
import clock

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

class Level :
    def __init__(self) :
        self.background_images = [
            pygame.image.load("Asset/bg1.png"),
            pygame.image.load("Asset/bg1.png"),
            pygame.image.load("Asset/bg1.png")
        ]

        self.object_images = [

        ]
        self.day = 1
        self.max_day = 5
        self.countdown = None
        self.background1_coordinate = ()
        self.background2_coordinate = ()
        self.InitBackground()
        self.bg1_cursor = 0
        self.bg2_cursor = 1
        self.SelectCountDown()

        self.timer = clock.Timer()
        self.font = pygame.font.Font(None, 26)

    def InitBackground(self) :
        self.background1_coordinate = (0,0)
        self.background2_coordinate = (SCREEN_WIDTH,0)

    def level_end(self) : 
        if self.bg1_cursor >= len(self.background_images)-1 and self.bg2_cursor >= len(self.background_images)-1 :
            return True
        return False
    
    def TimerEnd(self) :
        if self.timer.time_passed > self.countdown and self.timer.run_state :
            return True
        return False
    
    def reset(self) :
        self.bg1_cursor = 0
        self.bg2_cursor = 1
        self.background1_coordinate = (0,0)
        self.background2_coordinate = (SCREEN_WIDTH,0)

    def NextDay(self) :
        self.reset()
        if self.day < self.max_day :
            self.day += 1

    def SelectCountDown(self) :
        match self.day :
            case 1 :
                self.countdown = 10
            case 2 :
                self.countdown = 90
            case 3 :
                self.countdown = 60
            case 4 :
                self.countdown = 30


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