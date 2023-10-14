import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, images):
        pg.sprite.Sprite.__init__(self)
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.animate()
        self.move()

    def animate(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
    
    def move(self):
        self.rect.x += 0.5
