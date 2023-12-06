import os
import cv2
import pygame
import mediapipe as mp

from model.Player import Player


class ViewGame:
    def __init__(self):
        pygame.init()
        # self.width = 1000
        # self.height = 650
        self.cap = cv2.VideoCapture(1)

        self.width = int(self.cap.get(3))
        self.height = int(self.cap.get(4))
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(False)
        self.npDraw = mp.solutions.drawing_utils
        self.sound_laser = pygame.mixer.Sound((os.path.join('audio', 'laser.wav')))
        self.sound_laser.set_volume(0.3)
        self.sound_menu = pygame.mixer.Sound((os.path.join('audio', 'menu.mp3')))
        self.sound_death = pygame.mixer.Sound((os.path.join('audio', 'death.mp3')))
        # Загружаю изображение
        self.RED_ENEMY_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
        self.BLUE_ENEMY_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
        self.GREEN_ENEMY_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))

        self.YELLOW_MAIN_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")), (30, 30))

        # Lasers
        self.RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
        self.GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
        self.BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
        self.YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
        self.COLOR_OF_ENEMY = {"red": (self.RED_ENEMY_SHIP, self.RED_LASER),
                               "green": (self.GREEN_ENEMY_SHIP, self.GREEN_LASER),
                               "blue": (self.BLUE_ENEMY_SHIP, self.BLUE_LASER)}
        pygame.font.init()
        self.main_font = pygame.font.SysFont('arial', 20)
        self.dead = pygame.font.SysFont('comicsans', 30)


        # Настройка Pygame окна
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Hand Tracking with Pygame and OpenCV')
        # self.window = pygame.display.set_mode((self.width, self.height))
        # pygame.display.set_caption(("Space-Invaders"))
        self.ship = Player(self.width / 2 - 30, self.height - 40, self.window,
                           self.YELLOW_MAIN_SHIP, self.YELLOW_LASER)
        pygame.mixer_music.load(os.path.join('audio', 'back.mp3'))
        pygame.mixer_music.play(20)

    def redraw_window(self, lives, level, enemies, lost, scores):


        # рисуем
        lives_label = self.main_font.render(f"Жизни: {lives}", 1, (255, 255, 255))
        scores_label = self.main_font.render(f"Очки: {scores}", 1 ,(255, 255, 255))
        level_label = self.main_font.render(f"Уровень: {level}", 1, (255, 255, 255))
        self.window.blit(lives_label, (10, 25))
        self.window.blit(level_label, (self.width - level_label.get_width() - 10, 25))
        self.window.blit(scores_label, (self.width - scores_label.get_width() - 10, 25+ level_label.get_height() + 10))
        self.ship.draw()
        self.ship.health_bar()
        for enemy in enemies:
            enemy.draw()
        if lost:
            dead = self.dead.render("YOU DIED", 1, (255, 0, 0))
            self.window.blit(dead, (round(self.width/2 - dead.get_width()/2), round(self.height/3 - dead.get_height()/2)))
        pygame.display.update()

    def one_string_of_menu(self, x, y, text):
        pygame.draw.rect(self.window, (255, 255, 255), (x, y,
                                                    self.width/3, self.height/6))
        pygame.draw.rect(self.window, (0, 0, 0), (x+10, y+5 ,
                                                    self.width/3-40, self.height/6 - 20))
        self.window.blit(text, (x+10, y+5))
    def redraw_window_menu(self):

        self.one_string_of_menu(self.width/3, self.height/4, self.main_font.render("PLAY", 1, (255, 255, 255)))
        self.one_string_of_menu(self.width / 3, self.height / 4+self.height/6, self.main_font.render("TABLESCORE", 1, (255, 255, 255)))
        self.one_string_of_menu(self.width/3, self.height/4+(2*self.height/6), self.main_font.render("QUIT", 1, (255, 255, 255)))
        pygame.display.update()
