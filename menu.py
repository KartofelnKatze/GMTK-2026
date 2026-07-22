import pygame

class Button :
    def __init__(self,x : float,y : float, label : str) :
        self.coordinate = (x,y)
        self.width = 250
        self.height = 100
        self.label = label 
        self.font = pygame.font.Font(None, 26)

    def hover(self) :
        mouse_pos = pygame.mouse.get_pos()
        if(self.coordinate[0] < mouse_pos[0] and self.coordinate[0]+self.width > mouse_pos[0]) :
            if(self.coordinate[1] < mouse_pos[1] and self.coordinate[1]+self.height > mouse_pos[1]) :
                return True
        return False

    def clicked(self, events) :
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.hover():
                if event.button == 1 :
                    return True
        return False             

    def Draw(self, surface : pygame.Surface) :
        text_surface = self.font.render(self.label, True, (255, 255, 255))
        rect = pygame.Rect(self.coordinate[0],self.coordinate[1],self.width,self.height)
        pygame.draw.rect(surface,(255,0,0),rect)
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()
        surface.blit(text_surface, (self.coordinate[0] + rect.width/2-text_width/2,
                                    self.coordinate[1] + rect.height/2-text_height/2))

class OptionsMenu :
    def __init__(self) :
            self.buttons = [
                Button(495,500,"Back")
            ]
            self.active = False

    def update(self, events) :
            for button in self.buttons :
                if(button.clicked(events)) :
                    if(button.label == "Back") :
                        self.active = False

    def Draw(self, surface : pygame.Surface) :
        for button in self.buttons :
            button.Draw(surface)
    
class Menu : 
    def __init__(self) :
        self.buttons = [
            Button(495,200,"Play"),
            Button(495,350,"Options"),
            Button(495,500,"Quit")
        ]
        self.game_start = False
        self.options = OptionsMenu()

    def update(self, events) :
        for button in self.buttons :
            if(button.clicked(events)) :
                if(button.label == "Play") :
                    self.game_start = True
                elif(button.label == "Options") :
                    self.options.active = True
                elif(button.label == "Quit") :
                    pygame.quit()
        self.options.update(events)

    def Draw(self, surface : pygame.Surface) :
        if not self.game_start and not self.options.active:
            for button in self.buttons :
                button.Draw(surface)
        elif(self.options.active):
            self.options.Draw(surface)