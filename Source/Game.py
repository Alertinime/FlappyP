import pygame
from Player import Player
class Game:
    def __init__(self,windows,res):
        self.res = res
        self.windows = windows
        self.running = True
        self.player = Player(self.windows,res) 
        self.wall = pygame.image.load("../img/background.png").convert_alpha()
        self.sol = pygame.image.load("../img/sol.png").convert_alpha()
        self.sol_x_pos = 0

    def render(self):
        self.windows.blit(self.wall, (0,0))
        self.windows.blit(self.sol, (self.sol_x_pos,900))
        self.windows.blit(self.sol, (self.sol_x_pos + 576,900))
        self.sol_x_pos -= 1
        if self.sol_x_pos <= -576:
            self.sol_x_pos=0
        self.player.render()
        
        pygame.display.flip() 

    def event(self):
        for event in pygame.event.get(): #Quiter le jeu
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.asjump = True #saut quand la touche est pressée
            while self.player.asjump == True:
                self.player.jumping()
                self.windows.blit(self.wall, (0,0))
                self.player.render()
                pygame.display.flip()
            #self.player.rect.center=(self.image.get_width(),self.image.get_height()) #mouvement du rectangle

    def check_collision(): #tentative de colison
        if self.player.hitbox.top <= -100 or self.player.hitbox.bottom >= 900:
            print("Mayonaise")

    

