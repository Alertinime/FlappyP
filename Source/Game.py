import pygame
from Player import Player
class Game:
    def __init__(self,windows,res):
        self.res = res
        self.windows = windows
        self.running = True
        self.player = Player(self.windows,res)
        self.wall = pygame.image.load("../img/wall.jpg").convert_alpha()

    def render(self):
        self.windows.blit(self.wall, (0,0))
        self.player.render()
        pygame.display.flip() 

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.asjump = True
            while self.player.asjump == True:
                self.player.jumping()
                self.windows.blit(self.wall, (0,0))
                self.player.render()
                pygame.display.flip()    
