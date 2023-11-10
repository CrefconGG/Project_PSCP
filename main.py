import pygame as pg
from enemy import Enemy
import constants as c

#initialise pygame
pg.init()

#create clock
clock = pg.time.Clock()

#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("การเอาคืนของป้อม DEMO")

#load images
enemy_image = pg.image.load("assets/images/enemies/enemy_1.png").convert_alpha()

#create groups
enemy_group = pg.sprite.Group()

waypoint = [
    (100, 100),
    (400, 200),
    (400, 100),
    (200, 300)
]

enemy = Enemy(waypoint, enemy_image)
enemy_group.add(enemy)

#new icon
icon = pg.image.load("assets/images/icons/icon.png")
pg.display.set_icon(icon)

#game loop
run = True
while run:

    clock.tick(c.FPS)

    #update groups
    enemy_group.update()

    screen.fill("white")

    #draw enemy path
    pg.draw.lines(screen, "Black", False, waypoint)

    #draw groups
    enemy_group.draw(screen)

    #event control
    for event in pg.event.get():
        #exit game
        if event.type == pg.QUIT:
            run = False
    #update display
    pg.display.flip()

pg.quit()
