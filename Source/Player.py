import pygame,sys

class Player:
    def __init__(self,window : pygame.Surface,res):
        self.window = window        
        self.window_large = self.window.get_width()
        self.window_haut = self.window.get_height()
        self.image = pygame.image.load("../img/Perso_D.png").convert_alpha()
        self.pos = [(self.window_large - self.image.get_width()) // 2, (self.window_haut - self.image.get_height()) // 2]
        self.jump = 0
        self.jump_up = 0
        self.asjump = False
        self.fallspeed = 1
    def render(self):
        if self.pos[1] + 48 < 620:
            self.pos[1] = self.pos[1] + (2*self.fallspeed)
            self.fallspeed += 1
        else:
            self.pos[1] = 600
        self.window.blit(self.image,self.pos)
    def jumping(self):
        self.fallspeed = 1
        if self.asjump:
            if self.jump_up <=5:
                self.jump_up +=1
                self.jump = self.jump_up
                if self.pos[1] - (3 *self.jump) > 0:
                    self.pos[1] = self.pos[1] - (3 *self.jump)
            else:
                self.jump_up = 0
                self.jump = 0
                self.asjump = False