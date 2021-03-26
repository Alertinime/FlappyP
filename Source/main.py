import pygame,sys
from Game import Game
res = (576,1024)
clock = pygame.time.Clock()
frame = 0
pygame.init()
window = pygame.display.set_mode(res)
game = Game(window,res)
while game.running:
    if (frame % 5) == 0:
        game.event()
        game.render()
    clock.tick(60)
    if frame == 1000000:
        frame = 0
    else:
        frame += 1
