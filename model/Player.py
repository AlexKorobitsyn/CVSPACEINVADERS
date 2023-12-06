import pygame.mask

from model.Ship import AllShips


class Player(AllShips):
    def __init__(self, x, y, window, ship_img, laser_img, health=100):
        super().__init__(x, y, window, health)
        self.ship_img = ship_img
        self.laser_img = laser_img
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, speed, objs):
        self.reload()
        for laser in self.lasers:
            laser.move_one_laser(-speed)
            if laser.off_screen(self.window.get_height()):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        obj.health -= 100
                        self.lasers.remove(laser)

    def health_bar(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y+self.ship_img.get_height()+10,
                                                    self.ship_img.get_width(), 10))
        pygame.draw.rect(self.window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10,
                                                    self.ship_img.get_width()*(self.health/self.max_health), 10))
