"""
Run this file to start the game.
"""
import pygame as pg

gain = 4

if __name__ == '__main__':
    pg.init()
    reso = (1200, 800)
    screen = pg.display.set_mode(reso)
    scrrect = screen.get_rect()
    bgcolor = (135, 206, 250)

    points = 4396
    font = pg.font.SysFont('timesnewroman', 15)
    text = font.render('Points: ' + str(points), True, (178, 34, 34), bgcolor)
    textRect = text.get_rect()
    textRect.center = (1150, 20)

    drone = pg.image.load("../images/sprites/drone.png")
    dronerect = drone.get_rect()
    dronerect.centerx = 100
    dronerect.centery = 100

    turbine = pg.image.load("../images/sprites/turbine.png")
    turbinerect = drone.get_rect()
    turbinerect.centerx = 500
    turbinerect.centery = 500

    fo1 = pg.image.load("../images/sprites/flyingobject1.png")
    fo1rect = drone.get_rect()
    fo1rect.centerx = 400
    fo1rect.centery = 200

    fo2 = pg.image.load("../images/sprites/flyingobject2.png")
    fo2rect = drone.get_rect()
    fo2rect.centerx = 500
    fo2rect.centery = 300

    fo3 = pg.image.load("../images/sprites/flyingobject3.png")
    fo3rect = drone.get_rect()
    fo3rect.centerx = 600
    fo3rect.centery = 400

    fo4 = pg.image.load("../images/sprites/flyingobject4.png")
    fo4rect = drone.get_rect()
    fo4rect.centerx = 800
    fo4rect.centery = 500

    start_time = pg.time.get_ticks() / 1000.
    previous_time = start_time

    start_x = 300
    start_x_1 = int(fo1rect.centerx)
    start_x_2 = int(fo2rect.centerx)
    start_x_3 = int(fo3rect.centerx)
    start_x_4 = int(fo4rect.centerx)
    velocity_x = -100.
    velocity_x_1 = -220.
    velocity_x_2 = -230.
    velocity_x_3 = -170.
    velocity_x_4 = -200.

    # Game Loop
    escape = False
    while not escape:
        pg.event.pump()
        keys = pg.key.get_pressed()
        escape = keys[pg.K_ESCAPE]  # cannot work alone?
        for event in pg.event.get():
            if event.type == pg.QUIT:
                escape = True

        # change drone position
        decrement = keys[pg.K_UP]
        if decrement:
            if dronerect.centery >= 31:
                dronerect.centery -= gain
            else:
                dronerect.centery = 30
        increment = keys[pg.K_DOWN]
        if increment:
            if dronerect.centery <= 769:
                dronerect.centery += gain
            else:
                dronerect.centery = 770  # why not 740?

        time = pg.time.get_ticks() / 1000. - start_time

        x = start_x + velocity_x * time
        x2 = start_x_1 + velocity_x * time
        turbinerect.centerx = int(x)
        fo1rect.centerx = start_x_1 + velocity_x_1 * time  # int(fo1rect.centerx) + velocity_x * time is wrong
        fo2rect.centerx = start_x_2 + velocity_x_2 * time
        fo3rect.centerx = start_x_3 + velocity_x_3 * time
        fo4rect.centerx = start_x_4 + velocity_x_4 * time
        pg.draw.rect(screen, bgcolor, scrrect)
        screen.blit(drone, dronerect)
        screen.blit(turbine, turbinerect)
        screen.blit(fo1, fo1rect)
        screen.blit(fo2, fo2rect)
        screen.blit(fo3, fo3rect)
        screen.blit(fo4, fo4rect)
        screen.blit(text, textRect)
        pg.display.flip()

        if x < -100:
            pass

    pg.quit()
    pass