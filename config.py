import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()
running = True

# fonts
font1 = pygame.font.SysFont('consolas.ttf', 30)
font2 = pygame.font.SysFont('consolas.ttf', 70)

# carga sprites
alien_1a = pygame.image.load("1a.png")
alien_1b = pygame.image.load("1b.png")
alien_2a = pygame.image.load("2a.png")
alien_2b = pygame.image.load("2b.png")
alien_3a = pygame.image.load("3a.png")
alien_3b = pygame.image.load("3b.png")
player = pygame.image.load("player.png")
disparo = pygame.image.load("disparo.png")
disparoAln = pygame.image.load("disparoAlien.png")
explosion = pygame.image.load("explosion.png")

# optimizacion??
alien_1a.convert()
alien_1b.convert()
alien_2a.convert()
alien_2b.convert()
alien_3a.convert()
alien_3b.convert()
player.convert()
disparo.convert()
disparoAln.convert()
explosion.convert()

class Control:
    flagAnimacion = False
    flagCambiarDireccion = False
    flagActualizaY = False    
    flagMoveRigth = True                # indica si se mueve a la derecha o la izquierda

    velocidad = 15                      # avance del sprite
    stepY = 20                          # altura que desciende en cada rebote
    retrasoMovimiento = 45              # frames de intervalo entre cada paso
    limiteDrecha = 555
    limiteIzquierda = 50

    offset_alien1 = 16
    offset_alien2 = 22
    offset_alien3 = 24
    score = 0
    level = 0
    playerCooldown = 40
    frecuenciaAtaque = 0

    disparos = []
    aliens = []
    disparosAlien = []

    derrota = False                     # game over man!
    p1 = None

ctrl = Control()

from invaderA import *
from disparo import *
from player import *

ctrl.p1 = Player(300, 470)

def reiniciaTodo():
    ctrl.score = 0
    ctrl.level = 1
    ctrl.stepY = 20
    ctrl.frecuenciaAtaque = 1100
    ctrl.derrota = False
    ctrl.p1.defeated = False
    ctrl.p1.alive = True
    ctrl.p1.deadCounter = 0
    ctrl.p1.posicionX = 300
    reiniciaNivel()

def reiniciaNivel():
    ctrl.retrasoMovimiento = 45
    ctrl.disparos.clear()                    # elimina disparos anteriores
    ctrl.aliens.clear()                      # elimina aliens anteriores
    ctrl.disparosAlien.clear()
    
    playerPosX = 0
    playerPosY = 0
    
    inicialX = 120
    inicialY = 50
    espacioX = 60
    espacioY = 50
    x = inicialX
    y = inicialY
    for _ in range(7):
        al = invaderA(3, x, y)              # instancia 1 alien
        ctrl.aliens.append(al)              # lo inserta en el array (list) de aliens
        x += espacioX

    x = inicialX
    y += espacioY
    for _ in range(7):
        al = invaderA(1, x, y)              # instancia 1 alien
        ctrl.aliens.append(al)              # lo inserta en el array (list) de aliens
        x += espacioX      

    x = inicialX
    y += espacioY
    for _ in range(7):
        al = invaderA(2, x, y)              # instancia 1 alien
        ctrl.aliens.append(al)              # lo inserta en el array (list) de aliens
        x += espacioX                
    