from config import *

class Disparo():
    def __init__(self, x, y):
        self.posicionX = x
        self.posicionY = y
        self.speed = 8
        self.offsetX = 3
        self.offsetY = 10
        self.delete = False

    def mover(self):
        self.posicionY -= self.speed

        if self.posicionX < -20:
            self.delete = True

    def blit(self):
        screen.blit(disparo, (self.posicionX - self.offsetX, self.posicionY - self.offsetY))

    def collide(self):
        rect1 = pygame.Rect(self.posicionX - self.offsetX, self.posicionY - self.offsetY, 6, 20)
        for alien in ctrl.aliens:
            if self.delete == False:
                rect2 = alien.getRecti()
                if rect2 != False:
                    collide = rect1.colliderect(rect2)
                    if collide:
                        alien.setExplosion()
                        ctrl.score += 1
                        self.delete = True