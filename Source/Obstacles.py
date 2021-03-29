import pygame,sys
import random
class Obstacles:
    def __init__(self,window : pygame.Surface,res):
        self.window = window
        self.image = pygame.image.load("../img/tuyau.png").convert_alpha()
        self.Ltuyau = []
        self.placetuyau = []
    def genetuyau(self):
        newtuyau = []
        lockzero = False
        for i in range(5):
            if i == 0 or i == 4:
                newtuyau.append(1)
            gene = random.randint(0,1)
            if gene == 0 and lockzero == False and i != 1 and i != 3: 
                newtuyau.append(0)
                newtuyau.append(0)
                lockzero = True
            else:
                newtuyau.append(1)
        if not 0 in newtuyau:
            gene = random.randint(1,4)
            newtuyau[gene] = 0
            newtuyau[gene+1] = 0
            newtuyau.append(1)
        self.Ltuyau.append(newtuyau)

    def render(self):
        if self.Ltuyau == [] and self.placetuyau == []:
            self.genetuyau()
            self.placetuyau = self.Ltuyau
            self.placetuyau.append(0)
        else:
            pos_x = 800 - self.placetuyau[1]
            self.placetuyau[1] += 5
            detail = self.placetuyau[0]
            number = len(detail)
            print(detail)
            x = 0
            for i in detail:
                if i != 0:
                    if x != number:
                        pos_y = x * 80
                        x += 1

                        self.window.blit(self.image,(pos_x,pos_y))
                        pygame.display.flip()
                else:
                    x += 1
            if pos_x < - 80:
                self.placetuyau = []
                self.Ltuyau = []