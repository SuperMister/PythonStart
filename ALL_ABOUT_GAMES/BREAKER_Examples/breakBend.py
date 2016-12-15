

import pygame
import random

from pygame.locals import *


class GameInterface:
    pass


class Ball:

    def __init__(self):
        pass

    def draw_a_ball(self, surf, xy, s_color):
        pygame.draw.circle(surf, s_color, xy, 8)

    def ball_move(self, surf, xy, changex, changey, width, height):
        pass

class Bricks:

    def __init__(self):
        pass

    def draw_bricks(self, surf, s_color, amount):
        x = 105
        y = 5
        step_x = 0
        step_y = 0
        for j in range(amount):
            if step_y >= 250:
                break
            for i in range(amount):
                pygame.draw.rect(surf, s_color, [x + step_x, y + step_y, 20, 10])

class Game:

    def __init__(self):
        pygame.init()

        self.width = 800
        self.height = 600

        self.thick = 75

        self.surf = pygame.display.set_mode((self.width, self.height), 0, 32)

        self.colors = {"or": (217, 97, 44), "bl": (0, 0, 0), "wh": (255, 255, 255), "gr": (0, 149, 70),
                       "rd": (240, 0, 0), "lgr": (37, 84, 42), "blue": (0, 0, 70)}

        pygame.display.set_caption("Break a Brick")
        self.exit = False
        self.clock = pygame.time.Clock()

    def choose_color(self, s_color):
        return self.colors[s_color]

    def draw_borders(self, s_color, width, height):
        pygame.draw.rect(self.surf, s_color, (0, 0, 100, height))
        pygame.draw.rect(self.surf, s_color, (width - 100, 0, 100, height))

    def game_run(self):

        ball = Ball()
        x = int(self.width / 2 - self.thick / 2)
        y = self.height - 20

        x_b = int(self.width / 2)
        y_b = self.height - 30

        change_x_b = 0
        change_y_b = 0

        change_x = 0
        change_y = 0
        ball_speed = 3
        speed = 4

        s_color = "or"
        start = False
        while not self.exit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    self.exit = True

                elif event.type == KEYDOWN:  # depending on a key pressed subtract or add points to x or y
                    if event.key == K_LEFT:
                        change_x = -speed
                        if not start:
                            change_x_b = -speed
                    elif event.key == K_RIGHT:
                        change_x = speed
                        if not start:
                            change_x_b = speed
                    elif event.key == K_SPACE:
                        change_y_b = -ball_speed
                        change_x_b = random.choice(range(-ball_speed, ball_speed))
                        start = True

                if event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        change_x = 0
                        if not start:
                            change_x_b = 0

            if x <= 100:
                change_x = 0
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        change_x = speed
            elif x >= self.width - 170:
                change_x = 0
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        change_x = -speed

            if x_b >= 700:
                change_x_b = -ball_speed
            elif x_b <= 100:
                change_x_b = ball_speed
            elif y_b <= 0:
                change_y_b = ball_speed
            if start:
                if x_b in range(x + 30, x + 70) and y_b in range(y - 10, y):
                    change_y_b = -ball_speed
                elif x_b in range(x, x + 30) and y_b in range(y - 10, y):
                    change_y_b = -ball_speed
                    change_x_b = -ball_speed
                elif x_b in range(x + 70, x + 100) and y_b in range(y - 10, y):
                    change_y_b = -ball_speed
                    change_x_b = ball_speed

            x += change_x
            y += change_y

            x_b += change_x_b
            y_b += change_y_b

            self.surf.fill(self.colors["bl"])  # re-filling the background, so rectangle stays as one piece
            ball.draw_a_ball(self.surf, [x_b, y_b], self.choose_color("rd"))

            pygame.draw.rect(self.surf, self.choose_color(s_color), (x, y, self.thick, 10))  # x, y, width, height

            self.draw_borders(self.choose_color(s_color), self.width, self.height)
            pygame.display.update()

            self.clock.tick(100)  # frames per second

game = Game()
game.game_run()