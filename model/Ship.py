import pygame.draw

from model.Laser import Laser


class AllShips:
    COOLDOWN = 20

    def __init__(self, x, y, window, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cooldown_counter = 0
        self.window = window

    def draw(self):
        self.x = self.x % self.window.get_width()
        self.window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(self.window)

    def move_lasers(self, speed, obj):
        self.reload()
        for laser in self.lasers:
            laser.move_one_laser(speed)
            if laser.off_screen(self.window.get_height()):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def reload(self):
        if self.cooldown_counter >= self.COOLDOWN:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

    def shoot(self):
        if self.cooldown_counter == 0:
            laser = Laser(round(self.x-35), self.y, self.laser_img)
            self.lasers.append(laser)
            self.cooldown_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()