from   settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = player_position
        self.angle = player_angle

    def movement(self):
        pass

    def update(self):
        self.movement()

    @property
    def position(self):
        return self.x, self.y

    @property
    def map_position(self):
        return int(self.x), int(self.y)
