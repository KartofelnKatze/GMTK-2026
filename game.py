import pygame
import level
import menu
import player

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

class RestartMenu :
    def __init__(self) :
        button = menu.Button(552.5,322.5,"Next Day")
        button.width = 175
        button.height = 75
        self.buttons = [
            button
        ]
        self.active = False

    def update(self, events, level) :
        if self.active :
            for button in self.buttons :
                if(button.clicked(events)) :
                    if button.label == "Next Day" :
                        level.NextDay()
                        self.active = False

    def Draw(self, surface : pygame.Surface) :
        if self.active :
            rect = pygame.Rect(SCREEN_WIDTH/2-200,SCREEN_HEIGHT/2-100,400,200)
            pygame.draw.rect(surface, (0,0,0,145),rect)
            for button in self.buttons :
                button.Draw(surface)

class AnnoyanceBar :
    def __init__(self) :
        self.font = pygame.font.Font(None, 26)
        self.string = "Annoyance Bar"
        self.max_width = 200
        self.percentage = 0.0
        self.height = 35
        self.position = (SCREEN_WIDTH - self.max_width-25,self.height+20)

    def Draw(self,surface : pygame.Surface) :
        rect_white = pygame.Rect(self.position[0], self.position[1], self.max_width, self.height)
        rect_red = pygame.Rect(self.position[0], self.position[1], self.percentage*self.max_width, self.height)
        rect_border = pygame.Rect(self.position[0], self.position[1], self.max_width, self.height)
        pygame.draw.rect(surface,(255,255,255,255),rect_white)
        pygame.draw.rect(surface,(255,0,0,255),rect_red)
        pygame.draw.rect(surface, (0,0,0,255), rect_border,5)
        text_surface = self.font.render(self.string, True, (0, 0, 0))
        text_height = text_surface.get_height()
        surface.blit(text_surface, (self.position[0],
                                    self.position[1]-text_height))

class Game :
    def __init__(self, width : float, height : float) :
        self.width = width
        self.height = height

        self.level = level.Level()
        self.restart_menu = RestartMenu()
        self.annoyance_bar = AnnoyanceBar()

        self.InitBackground()
        self.background_speed = 50

        self.player = player.Player()

        self.clock = pygame.time.Clock()

        self.dt = self.clock.tick(60) / 1000

        self.font = pygame.font.Font(None, 26)

    def Scrolling(self) :
        self.background1_coordinate = (
            self.background1_coordinate[0] - self.background_speed*self.dt,
            self.background1_coordinate[1]
        )
        self.background2_coordinate = (
            self.background2_coordinate[0] - self.background_speed*self.dt,
            self.background2_coordinate[1]
        )

    def UpdateBackground(self) :
        if(self.background1_coordinate[0] + self.width < 0) :
            self.level.bg1_cursor += 1
            self.background1_image = self.level.background_images[self.level.bg1_cursor]
            self.background1_coordinate = (self.width,0)
        if(self.background2_coordinate[0] + self.width < 0) :
            self.level.bg2_cursor += 1
            self.background2_image = self.level.background_images[self.level.bg2_cursor]
            self.background2_coordinate = (self.width,0)

    def update(self, events) :
        self.dt = self.clock.tick(60) / 1000
        self.level.timer.update()
        self.UpdateBackground()
        self.player.update(self.dt)
        self.restart_menu.update(events, self.level)
        if not self.level.level_end() :
            if self.player.MaxReached() and not self.level.TimerEnd():
                self.Scrolling()
                if not self.level.timer.run_state :
                    self.level.timer.start()
        else :
            self.restart_menu.active = True

    def InitBackground(self) :
        self.background1_image = self.level.background_images[self.level.bg1_cursor]
        self.background2_image = self.level.background_images[self.level.bg2_cursor]
        self.background1_coordinate = (0,0)
        self.background2_coordinate = (self.width,0)

    def Draw(self, surface : pygame.Surface) :
        surface.blit(self.background1_image,self.background1_coordinate)
        surface.blit(self.background2_image,self.background2_coordinate)
        self.restart_menu.Draw(surface)
        self.player.Draw(surface)
        self.annoyance_bar.Draw(surface)
        self.level.Draw(surface)
