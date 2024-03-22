from config import *

# inicializa
dt = 1
clock = pygame.time.Clock()
reiniciaTodo()                                              # inicializa
acumuladorA = 0
acumuladorB = 0
moverAliens = False

# ciclo principal/ main loop
while running:
    # --- escucha eventos ---
    for event in pygame.event.get():                    # poll for events
        if event.type == pygame.QUIT:                   # pygame.QUIT event means the user clicked X to close your window
            running = False
        
    # --- logic ---
    acumuladorA += 1
    if acumuladorA > ctrl.retrasoMovimiento:
        acumuladorA = 0
        moverAliens = True
        ctrl.flagAnimacion = not ctrl.flagAnimacion
            
    # --- reset screen ---    
    screen.fill("black")                                # fill the screen with a color to wipe away anything from last frame    

    img1 = font1.render(f'score {ctrl.score}', True, (255, 255, 255))
    screen.blit(img1, (10, 10))

    img1 = font1.render(f'level {ctrl.level}', True, (255, 255, 255))
    screen.blit(img1, (510, 10))

    # --- render sprites ---
    ctrl.flagActualizaY = False                             # desactiva bandera
    if ctrl.flagCambiarDireccion:
        ctrl.flagCambiarDireccion = False                   # desactiva bandera
        ctrl.flagActualizaY = True                          # indica a todos los aliens bajar un escalon
        ctrl.flagMoveRigth = not ctrl.flagMoveRigth         # cambia la direccion del movimiento

    # dibuja aliens        
    for alien in ctrl.aliens:
        if moverAliens:
            alien.moveR()
        alien.blit()
    moverAliens = False
        
    # dibuja disparos player
    for disparo in ctrl.disparos:
        disparo.collide()               # maneja colisiones
        disparo.mover()
        disparo.blit()

    # dibuja disparos alien
    for disparo in ctrl.disparosAlien:
        disparo.collide()               # maneja colisiones
        disparo.mover()
        disparo.blit()

    # elimina disparos
    ctrl.disparos = [disparo for disparo in ctrl.disparos if disparo.delete == False]

    # elimina disparos alien
    ctrl.disparosAlien = [disparo for disparo in ctrl.disparosAlien if disparo.delete == False]

    # elimina aliens destruidos
    ctrl.aliens = [alien for alien in ctrl.aliens if alien.delete == False]
    
    # dibuja player
    ctrl.p1.control()
    ctrl.p1.blit()

    # controla dificultad
    if len(ctrl.aliens) == 1:
        ctrl.retrasoMovimiento = 1
    elif len(ctrl.aliens) < 4:
        ctrl.retrasoMovimiento = 3
    elif len(ctrl.aliens) < 10:
        ctrl.retrasoMovimiento = 8
    elif len(ctrl.aliens) < 15:
        ctrl.retrasoMovimiento = 16
    elif len(ctrl.aliens) < 20:
        ctrl.retrasoMovimiento = 30

    # controla nuevo nivel
    if len(ctrl.aliens) == 0:
        reiniciaNivel()
        ctrl.level += 1             # aumenta contador de nivel
        ctrl.stepY += 5             # baja mas rapido
        ctrl.frecuenciaAtaque -= 100

    # controla derrota
    for alien in ctrl.aliens:
        if alien.posicionY > 455:
            ctrl.derrota = True

    if ctrl.derrota:
        img1 = font2.render(f"IT'S GAME OVER MAN!", True, (255, 0, 0))
        screen.blit(img1, (30, 200))

    # reinicia juego
    keys = pygame.key.get_pressed()
    if keys[pygame.K_F1]:
            reiniciaTodo()

    if keys[pygame.K_ESCAPE]:
            running = False

    # --- fin del fotograma ---
    pygame.display.flip()                               # flip() the display to put your work on screen
    clock.tick(60)                                      # limits FPS to 60
    
# --- cierre ---
pygame.quit()
