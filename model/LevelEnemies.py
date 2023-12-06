import random

from model.Enemy import Enemy


class AllEnemies:
    def __init__(self, view1, level):
        self.view1 = view1
        self.level = level
        self.wave_length = 3
        self.enemies = self.make_level_enemies()


    def make_level_enemies(self):
        enemies = []
        self.wave_length += 3
        for i in range(self.wave_length):
            rand_color = random.choice(["red", "blue", "green"])
            enemy = Enemy(random.randrange(50, self.view1.width - 50),
                          random.randrange(round((-1300 * self.level) * 0.7), -100),
                          self.view1.window, self.view1.COLOR_OF_ENEMY[rand_color], rand_color)
            enemies.append(enemy)
        return enemies
