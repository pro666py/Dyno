import pygame as pg
import sys
from math import sqrt
from random import randint
from time import sleep

class Dino():
    def __init__(self):
        pg.init()
        self.W = 1200
        self.H = 720
        self.screen = pg.display.set_mode((self.W, self.H))

        self.image = pg.image.load('d1.png')
        self.image = pg.transform.scale(self.image, (150, 150))
        self.hb = self.image.get_rect(center=(self.W // 2, 575))

        self.file = open('record.txt', 'r')
        self.record = self.file.read()
        self.file.close()
        self.score = 0

        self.ship_image = pg.image.load('0012.png')
        self.ship1_hb = self.ship_image.get_rect(center=(100, 0))
        self.ship2_hb = self.ship_image.get_rect(center=(300, 0))
        self.ship3_hb = self.ship_image.get_rect(center=(500, 0))
        self.ship4_hb = self.ship_image.get_rect(center=(700, 0))
        self.ship5_hb = self.ship_image.get_rect(center=(900, 0))
        self.ship6_hb = self.ship_image.get_rect(center=(1100, 0))

        self.speed1 = randint(5, 15)
        self.speed2 = randint(5, 15)
        self.speed3 = randint(5, 15)
        self.speed4 = randint(5, 15)
        self.speed5 = randint(5, 15)
        self.speed6 = randint(5, 15)

        self.W1 = randint(20, 1180)
        self.W2 = randint(20, 1180)
        self.W3 = randint(20, 1180)
        self.W4 = randint(20, 1180)
        self.W5 = randint(20, 1180)
        self.W6 = randint(20, 1180)

        self.cimage = self.image
        self.rimage = pg.transform.flip(self.image.copy(), 1, 0)
        self.limage = self.image.copy()
        self.flag = None

        self.bg = pg.image.load('fon.png')
        self.bg = pg.transform.scale(self.bg, (1200, 720))
        self.bg_hb = self.bg.get_rect(center=(self.W // 2, self.H // 2))

        self.bg_music = pg.mixer.Sound('pixel-love-20240608-163925.mp3')
        self.bg_music.set_volume(0.1)
        self.bg_music.play(-1)
        self.gameover_sound = pg.mixer.Sound('jg-032316-sfx-video-game-game-over-3.mp3')
        self.gameover_sound.set_volume(0.2) 

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        return True

    def move(self):
        keys = pg.key.get_pressed()
        self.ship1_hb.move_ip((0, self.speed1))
        self.ship2_hb.move_ip((0, self.speed2))
        self.ship3_hb.move_ip((0, self.speed3))
        self.ship4_hb.move_ip((0, self.speed4))
        self.ship5_hb.move_ip((0, self.speed5))
        self.ship6_hb.move_ip((0, self.speed6))

        if keys[pg.K_RIGHT] and keys[pg.K_LSHIFT] and self.hb.centerx <= 1160:
            self.cimage = self.rimage
            self.hb.move_ip((15, 0))

        if keys[pg.K_LEFT] and keys[pg.K_LSHIFT] and self.hb.centerx >= 40:
            self.cimage = self.limage
            self.hb.move_ip((-15, 0))

        if keys[pg.K_RIGHT] and self.hb.centerx <= 1160:
            self.cimage = self.rimage
            self.hb.move_ip((10, 0))

        if keys[pg.K_LEFT] and self.hb.centerx >= 40:
            self.cimage = self.limage
            self.hb.move_ip((-10, 0))

        distance1 = sqrt((self.hb.centerx - self.ship1_hb.centerx) ** 2 + (self.hb.centery - self.ship1_hb.centery) ** 2)
        distance2 = sqrt((self.hb.centerx - self.ship2_hb.centerx) ** 2 + (self.hb.centery - self.ship2_hb.centery) ** 2)
        distance3 = sqrt((self.hb.centerx - self.ship3_hb.centerx) ** 2 + (self.hb.centery - self.ship3_hb.centery) ** 2)
        distance4 = sqrt((self.hb.centerx - self.ship4_hb.centerx) ** 2 + (self.hb.centery - self.ship4_hb.centery) ** 2)
        distance5 = sqrt((self.hb.centerx - self.ship5_hb.centerx) ** 2 + (self.hb.centery - self.ship5_hb.centery) ** 2)
        distance6 = sqrt((self.hb.centerx - self.ship6_hb.centerx) ** 2 + (self.hb.centery - self.ship6_hb.centery) ** 2)

        if distance1 < 40 or distance2 < 40 or distance3 < 40 or distance4 < 40 or distance5 < 40 or distance6 < 40:
            if self.score > int(self.record):
                self.file = open('record.txt', "w")
                self.file.write(str(self.score))
                self.file.close()
            self.bg_music.stop()
            self.gameover_sound.play()
            sleep(3)
            dino = Dino()
            dino.run()    

        if self.ship1_hb.centery > 700:
            self.speed1 = randint(5, 15)
            W1 = randint(20, 1180)
            self.ship1_hb = self.ship_image.get_rect(center=(W1, 0))
            self.score += 1

        if self.ship2_hb.centery > 700:
            self.speed2 = randint(5, 15)
            self.W2 = randint(20, 1180)
            self.ship2_hb = self.ship_image.get_rect(center=(self.W2, 0))
            self.score += 1

        if self.ship3_hb.centery > 700:
            self.speed3 = randint(5, 15)
            W3 = randint(20, 1180)
            self.ship3_hb = self.ship_image.get_rect(center=(W3, 0))
            self.score += 1

        if self.ship4_hb.centery > 700:
            self.speed4 = randint(5, 15)
            W4 = randint(20, 1180)
            self.ship4_hb = self.ship_image.get_rect(center=(W4, 0))
            self.score += 1

        if self.ship5_hb.centery > 700:
            self.speed5 = randint(5, 15)
            W5 = randint(20, 1180)
            self.ship5_hb = self.ship_image.get_rect(center=(W5, 0))
            self.score += 1

        if self.ship6_hb.centery > 700:
            self.speed6 = randint(5, 15)
            W6 = randint(20, 1180)
            self.ship6_hb = self.ship_image.get_rect(center=(W6, 0))
            self.score += 1

    def draw(self):
        self.score_font = pg.font.SysFont('arial', 20)
        self.score_text = self.score_font.render(f'score:{self.score}', 1, (0, 0, 0))
        self.screen.blit(self.bg, self.bg_hb)
        self.screen.blit(self.cimage, self.hb)
        self.screen.blit(self.ship_image, self.ship1_hb)
        self.screen.blit(self.ship_image, self.ship2_hb)
        self.screen.blit(self.ship_image, self.ship3_hb)
        self.screen.blit(self.ship_image, self.ship4_hb)
        self.screen.blit(self.ship_image, self.ship5_hb)
        self.screen.blit(self.ship_image, self.ship6_hb)
        self.screen.blit(self.score_text,(20, 20))

    def update(self):
        self.move()
        pg.display.flip()
        pg.time.Clock().tick(60)

    def run(self):
        while self.check_events():
            self.draw()
            self.update()

if __name__ == "__main__":
    dino = Dino()
    dino.run()

