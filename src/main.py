# This is for my learning, so there may be a lot of comments

import sys
import pygame   as pg
from   settings import *
from   map      import *

class Game:
    def __init__(self):
        pg.init()
        self.screen     = pg.display.set_mode(resolution)
        self.clock      = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
    
    def new_game(self):
        self.map = Map(self)

    def update(self):
        pg.display.flip()
        self.delta_time = self.clock.tick(frames_per_second)
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")

    def draw(self):
        self.screen.fill("black")
        self.map.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
