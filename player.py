from config import *

class Player():
    def __init__(self, x, y):
        self.posicionX = x
        self.posicionY = y
        self.speed = 4
        self.offsetX = 21
        self.offsetY = 21
        self.cooldown = 0
        self.alive = True
        self.delete = False
        self.deadCounter = 0
        self.defeated = False

    def control(self):
        if ctrl.derrota:
            return

        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.posicionX -= self.speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.posicionX += self.speed            

        if self.posicionX > ctrl.limiteDrecha:
            self.posicionX = ctrl.limiteDrecha

        if self.posicionX < ctrl.limiteIzquierda:
            self.posicionX = ctrl.limiteIzquierda

        if keys[pygame.K_SPACE] or keys[pygame.K_q] :
            self.nuevoDisparo()

    def blit(self):
        if self.defeated:
            return
        if self.cooldown > 0:
            self.cooldown -=1

        if not self.alive:
            screen.blit(explosion, (self.posicionX - 30, self.posicionY - self.offsetY))

            self.deadCounter += 1
            if self.deadCounter >= 15:
                self.defeated = True
                ctrl.derrota = True

            return

        screen.blit(player, (self.posicionX - self.offsetX, self.posicionY - self.offsetY))

    def nuevoDisparo(self):
        if self.cooldown <= 0:
            self.cooldown = ctrl.playerCooldown
            d = Disparo(self.posicionX, self.posicionY)         # instancia nuevo disparo
            ctrl.disparos.append(d)                             # lo inserta en el array (list) de aliens

    def getRecti(self):
        return pygame.Rect(self.posicionX - self.offsetX, self.posicionY - self.offsetY, 42, 42)

    def setExplosion(self):
            self.alive = False        
