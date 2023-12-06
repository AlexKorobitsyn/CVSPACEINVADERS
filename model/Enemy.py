import pygame.mask

from model.Laser import Laser
from model.Ship import AllShips


class Enemy(AllShips):
    def __init__(self, x, y, window, img_with_color, color, health=100):
        super().__init__(x, y, window, health)
        self.ship_img = img_with_color[0]
        self.laser_img = img_with_color[1]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.speed = 1
        if color == "blue":
            self.speed = 1.5
        if color == "red":
            self.health = 200

    def move(self):
        self.y += self.speed
    def shoot(self):
        if self.cooldown_counter == 0:
            laser = Laser(round(self.x-20), self.y, self.laser_img)
            self.lasers.append(laser)
            self.cooldown_counter = 1
