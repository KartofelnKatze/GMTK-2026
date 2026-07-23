import pygame
import clock

class qte:
    def init(self, lst, timelapse):
        self.lst = lst
        self.dico = {key : False for key in self.lst}
        self.timelapse = timelapse
        self.dico_lettres = {"a" : pygame.K_a , "z" : pygame.K_z , "e" : pygame.K_e ,
                      "q" : pygame.K_q, "s": pygame.K_s , "d" : pygame.K_d}
        self.font = pygame.font.Font(None, 26)
        self.internal_clock = clock.Timer()
        self.active = False

    def Check(self, events):
        self.compteur = 0
        for v in self.dico.keys():
            if self.dico[v] == False :
                for event in events :
                    if event.type == pygame.KEYDOWN :
                        if event.key == self.dico_lettres[v] :
                            self.dico[v] = True
                            return self.dico[v]
                        
    def IsValid(self) :
        return self.dico.valeus() == [True for i in range(3)] 

    def TimeEnd(self) :
        if self.internal_clock.current > self.timelapse :
            return True
        return False
    
    def activate(self) :
        if not self.internal_clock.run_state :
            self.internal_clock.start()
            self.active = True

    def Update(self,events) :
        if self.activate :
            self.Check(events)
            if self.TimeEnd() :
                self.internal_clock.stop()
                self.active = False

    def Draw(self, surface : pygame.Surface, position : tuple) :
        if self.active :
            text_surface = self.font.render("Press !", True, (255, 255, 255))
            surface.blit(text_surface,(position[0],position[1]))
