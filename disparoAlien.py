from config import *

class DisparoAlien():
    def __init__(self, x, y):
        self.posicionX = x
        self.posicionY = y
        self.speed = 2
        self.offsetX = 6
        self.offsetY = 9
        self.delete = False

    def mover(self):
        self.posicionY += self.speed

        if self.posicionX > 500:
            self.delete = True

    def blit(self):
        screen.blit(disparoAln, (self.posicionX - self.offsetX, self.posicionY - self.offsetY))

    def collide(self):
        rect1 = pygame.Rect(self.posicionX - self.offsetX, self.posicionY - self.offsetY, 8, 8)
       
        if self.delete == False:
            rect2 = ctrl.p1.getRecti()
            if rect2 != False:
                collide = rect1.colliderect(rect2)
                if collide:
                    ctrl.p1.setExplosion()
                    ctrl.score += 1
                    self.delete = True
                    