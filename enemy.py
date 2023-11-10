import pygame as pg
from pygame.math import Vector2

class Enemy(pg.sprite.Sprite):
    def __init__(self, waypoints, images):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.animation_speed = 0.4

    def update(self):
        self.animate()
        self.move()

    def animate(self):
        self.index += self.animation_speed
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[int(self.index)]
    
    def move(self):
        #define a target waypoint
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
        self.pos += self.movement.normalize()
        self.rect.center = self.pos
