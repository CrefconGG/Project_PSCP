import pygame as pg
import json
from enemy import Enemy
from world import World
from turret import Turret
import constants as c

#initialise pygame
pg.init()

#create clock
clock = pg.time.Clock()

#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("การเอาคืนของป้อม DEMO")

#load images
#map
map_image = pg.image.load('levels/level.png').convert_alpha()
#individual turret image for mouse cursor
cursor_turret = pg.image.load("assets/images/turrets/cursor_turret.png").convert_alpha()
#enemies
enemy_image = pg.image.load("assets/images/enemies/enemy_1.png").convert_alpha()

#load json data for level
with open('levels/level.tmj') as file:
    world_data = json.load(file)

#create world
world = World(world_data, map_image)
world.process_data()

#create groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

enemy = Enemy(world.waypoints, enemy_image)
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

    #draw map
    world.draw(screen)

    #draw groups
    enemy_group.draw(screen)
    turret_group.draw(screen)

    #event control
    for event in pg.event.get():
        #exit game
        if event.type == pg.QUIT:
            run = False
        #mouse click
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            turret = Turret(cursor_turret, mouse_pos)
            turret_group.add(turret)

    #update display
    pg.display.flip()

pg.quit()
