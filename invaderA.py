from config import *
from disparoAlien import *
import random

class invaderA():
    def __init__(self, tipo, x, y):        
        self.posicionX = x
        self.posicionY = y
        self.alientype = tipo
        self.offsetX = 0
        self.offsetY = 0
        self.alive = True
        self.delete = False
        self.deadCounter = 0
        
        if tipo == 1:
            self.offsetX = ctrl.offset_alien1
        elif tipo == 2:
            self.offsetX = ctrl.offset_alien2
        elif tipo == 3:
            self.offsetX = ctrl.offset_alien3
                
    def blit(self):
        numero_aleatorio = random.randint(1, ctrl.frecuenciaAtaque)
        if numero_aleatorio == 1:
            self.dispara()

        if not self.alive:
            screen.blit(explosion, (self.posicionX - 30, self.posicionY - self.offsetY))

            self.deadCounter += 1
            if self.deadCounter >= 15:
                self.delete = True

            return

        if ctrl.flagActualizaY:
            self.posicionY += ctrl.stepY
        
        if self.alientype == 1:
            if ctrl.flagAnimacion:
                screen.blit(alien_1a, (self.posicionX - self.offsetX, self.posicionY - self.offsetY))
            else:
                screen.blit(alien_1b, (self.posicionX - self.offsetX, self.posicionY - self.offsetY))

        if self.alientype == 2:
            if ctrl.flagAnimacion:
                screen.blit(alien_2a, (self.posicionX - self.offsetX, self.posicionY - self.offsetY))
            else:
                screen.blit(alien_2b, (self.posicionX - self.offsetX, self.posicionY - self.offsetY))

        if self.alientype == 3:
            if ctrl.flagAnimacion:
                screen.blit(alien_3a, (self.posicionX - self.offsetX, self.posicionY - self.offsetY))
            else:
                screen.blit(alien_3b, (self.posicionX - self.offsetX, self.posicionY - self.offsetY))
        
    def moveR(self):
        if ctrl.derrota:
            return

        if not self.alive:       
            return

        if ctrl.flagMoveRigth:
            self.posicionX += ctrl.velocidad
        else:
            self.posicionX -= ctrl.velocidad

        if ctrl.flagMoveRigth and self.posicionX > ctrl.limiteDrecha:               # comprueba el margen derecho unicamente si se mueve a la derecha
            ctrl.flagCambiarDireccion = True

        if not ctrl.flagMoveRigth and self.posicionX < ctrl.limiteIzquierda:        # comprueba el margen derecho unicamente si se mueve a la derecha
            ctrl.flagCambiarDireccion = True

    def getRecti(self):
        if self.alive: 
            return pygame.Rect(self.posicionX - self.offsetX, self.posicionY - self.offsetY, self.offsetX + self.offsetX, 32)
        else:
            return False

    def setExplosion(self):
            self.alive = False

    def dispara(self):                             
        d = DisparoAlien(self.posicionX, self.posicionY)         # instancia nuevo disparo
        ctrl.disparosAlien.append(d)                             # lo inserta en el array (list) de aliens
        