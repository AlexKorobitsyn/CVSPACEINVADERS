import unittest

import pygame

from model.Laser import Laser


class TestLaser(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.img = pygame.Surface((10, 20))
        self.laser = Laser(0, 0, self.img)

    def tearDown(self):
        pygame.quit()


    def test_laser_move_one_laser(self):
        initial_y = self.laser.y
        speed = 1
        self.laser.move_one_laser(speed)
        self.assertEqual(self.laser.y, initial_y + speed)

    def test_laser_off_screen(self):
        height = 600
        self.assertFalse(self.laser.off_screen(height))

        self.laser.y = -10
        self.assertTrue(self.laser.off_screen(height))

        self.laser.y = height + 10
        self.assertTrue(self.laser.off_screen(height))

    def test_laser_collision(self):
        class Obj:
            def __init__(self, x, y, mask):
                self.x = x
                self.y = y
                self.mask = mask

        obj = Obj(0, 0, pygame.mask.from_surface(pygame.Surface((10, 10))))
        self.assertTrue(self.laser.collision(obj))

        obj = Obj(100, 100, pygame.mask.from_surface(pygame.Surface((10, 10))))
        self.assertFalse(self.laser.collision(obj))