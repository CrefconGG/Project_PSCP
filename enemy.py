import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, waypoints, images):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = self.waypoints[0]
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 0.5
        self.animation_speed = 1

    def update(self):
        self.animate()
        self.move()

    def animate(self):
        self.index += self.animation_speed
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
    
    def move(self):
        self.rect.x += self.speed
