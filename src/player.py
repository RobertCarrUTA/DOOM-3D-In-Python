from   settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = player_position
        self.angle = player_angle

    def movement(self):
        sin_a  = math.sin(self.angle)
        cos_a  = math.cos(self.angle)
        dx, dy = 0, 0
        speed  = player_speed * self.game.delta_time
        
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx +=  speed_cos
            dy += -speed_cos


    def update(self):
        self.movement()

    @property
    def position(self):
        return self.x, self.y

    @property
    def map_position(self):
        return int(self.x), int(self.y)
