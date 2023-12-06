import unittest
import pygame

from model.Enemy import Enemy
from model.Laser import Laser
from model.Ship import AllShips

class TestEnemy(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.ship_img = pygame.Surface((50, 50))
        self.laser_img = pygame.Surface((10, 10))
        self.color = "blue"
        self.enemy = Enemy(0, 0, self.window, (self.ship_img, self.laser_img), self.color)

    def tearDown(self):
        pygame.quit()

    def test_enemy_initialization(self):
        self.assertEqual(self.enemy.x, 0)
        self.assertEqual(self.enemy.y, 0)
        self.assertEqual(self.enemy.window, self.window)
        self.assertEqual(self.enemy.ship_img, self.ship_img)
        self.assertEqual(self.enemy.laser_img, self.laser_img)
        self.assertEqual(self.enemy.speed, 1.5)
        self.assertEqual(self.enemy.health, 100)

    def test_enemy_move(self):
        initial_y = self.enemy.y
        self.enemy.move()
        self.assertEqual(self.enemy.y, initial_y + self.enemy.speed)

    def test_enemy_shoot(self):
        self.assertEqual(len(self.enemy.lasers), 0)
        self.assertEqual(self.enemy.cooldown_counter, 0)

        self.enemy.shoot()

        self.assertEqual(len(self.enemy.lasers), 1)
        self.assertEqual(self.enemy.lasers[0].x, -20)
        self.assertEqual(self.enemy.lasers[0].y, self.enemy.y)
        self.assertEqual(self.enemy.cooldown_counter, 1)


if __name__ == '__main__':
    unittest.main()