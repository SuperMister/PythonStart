"""Snake game."""

import pygame


class GameInterface():
    def __init__(self):
        self.all_colours = {"wh": (255, 255, 255), "bl": (0, 0, 0), "pn": (150, 0, 100)}# range of colours in 5D game


class Game:
    def __init__(self):
        pygame.init()
        self.inter = GameInterface()
        self.width = 800
        self.height = 600
        self.disp = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake 5D")


    def colour_choose(self):
        """Choose colour"""
    def game_process(self):
        game_exit = False

        while not game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
            self.disp.fill(self.inter.all_colours["pn"])
            pygame.draw.rect(self.disp, self.inter.all_colours["wh"], [400, 300, 50, 50])
            self.disp.fill(self.inter.all_colours["bl"], rect=(100, 100, 50, 50))
            pygame.display.update()
        pygame.quit()
        quit()


a = Game()
a.game_process()