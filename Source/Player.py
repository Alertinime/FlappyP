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
        self.hitbox = self.image.get_rect(center=(self.image.get_width(),self.image.get_height())) #création du rectangle (fonctionne pas trop)
    def render(self):
        self.window.blit(self.image,self.pos) 
        self.pos[1] = self.pos[1] + (5*self.fallspeed)
        #self.hitbox.centerer += self.fallspeed  #rendu du rectangle (utile ?)
        self.fallspeed += 1
    def jumping(self):
        self.fallspeed = 1
        if self.asjump:
            if self.jump_up <=5:
                self.jump_up +=1
                self.jump = self.jump_up
                self.pos[1] = self.pos[1] - (5 *self.jump)
            else:
                self.jump_up = 0
                self.jump = 0
                self.asjump = False
            print(self.jump)