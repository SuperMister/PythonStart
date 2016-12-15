
import pygame
import time
import random

from pygame.locals import *


class Apple:
    """Drawing an apple to the board."""
    def __init__(self, thick, width, height):
        """Class constructor."""

        # Setting random coordinates for apple to appear (with boundaries)
        self.randx = round(random.choice(range(thick, width - thick)))
        self.randy = round(random.choice(range(thick, height - thick)))

    def apple_coordinates(self):
        """Return list of generated coordinates for an apple."""
        return list([self.randx, self.randy])

    def draw_apple(self, surf, body_color):
        """Drawing an apple."""
        pygame.draw.circle(surf, body_color, (self.randx, self.randy), 5)


class GameInterface:
    """Creating user interface to interact with."""

    def __init__(self):
        """Defining colors. RGB range."""
        self.colors = {"or": (255, 60, 0), "bl": (0, 0, 0), "wh": (255, 255, 255), "gr": (16, 104, 0),
                       "rd": (240, 0, 0,), "lgr": (37, 84, 42), "blue": (0, 0, 70), "drd": (148, 0, 44)}

    def color_choose(self, s_color):
        """Allows to fill smth with specific color."""
        return self.colors[s_color]

    def message(self, message, xy, surf, f_color):
        """Setting font size, quality and color for future messages."""
        font = pygame.font.SysFont(None, 35)

        screen_text = font.render(message, True, f_color)
        surf.blit(screen_text, xy)

    def start_menu(self, surf, s_color, f_color):
        """Creating start menu with user interface."""
        x = 50
        y = 130

        surf.fill(s_color)
        self.message("Select your difficulty: ", [x, y], surf, f_color)
        self.message("\'S\'     for slooooow", [x, y + 100], surf, f_color)
        self.message("\'E\'     for experienced", [x, y + 150], surf, f_color)
        self.message("\'N\'     for nightmare", [x, y + 200], surf, f_color)
        self.message("... or press Q to exit.", [x, y + 300], surf, f_color)
        pygame.display.update()

    def start_menu_colors(self, surf, s_color, f_color):
        """Setting user interface for choosing background colors."""
        x = 50
        y = 130
        surf.fill(s_color)
        self.message("Select your background color: ", [x, y], surf, f_color)
        self.message("G - for green", [x, y + 100], surf, f_color)
        self.message("B - for black", [x, y + 150], surf, f_color)
        self.message("L - for blue", [x, y + 200], surf, f_color)
        self.message("R - for red", [x, y + 250], surf, f_color)
        self.message("... or press Q to exit.", [x, y + 300], surf, f_color)
        pygame.display.update()

    def end_choice(self, surf, s_color, f_color):
        """End menu user interface."""
        x = 50
        y = 300
        game_st = Game()  # Creating game class object
        surf.fill(s_color)
        self.message("You lost!", [x, y - 150], surf, f_color)
        self.message("Press Space to try again! Or Q to quit.", [x, y], surf, f_color)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_q:
                    surf.fill(s_color)
                    self.message("Bye", [x, y], surf, f_color)
                    pygame.display.update()
                    time.sleep(0.2)
                    raise SystemExit
                elif event.key == pygame.K_SPACE:
                    game_st.game_loop()  # Starting over

    def excellent(self, surf, s_color, f_color):
        """For pros."""
        game_st = Game()
        surf.fill(s_color)
        image = pygame.image.load("img.jpg")
        surf.blit(image, (25, 200))
        self.message("Wow! You\'re a pro!", [50, 100], surf, f_color)
        self.message("Space - continue", [590, 300], surf, f_color)
        self.message("Q - exit", [590, 350], surf, f_color)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_q:
                    self.exit(surf, s_color, f_color)
                elif event.key == pygame.K_SPACE:
                    game_st.game_loop()

    def exit(self, surf, s_color, f_color):
        """Displays exit message (Bye)."""
        surf.fill(s_color)
        self.message("Bye", [50, 300], surf, f_color)
        pygame.display.update()
        time.sleep(0.2)
        raise SystemExit


class UserSettings:
    def __init__(self):
        # was forced to invert original dict due to pygame module ...
        self.inv_colors = {(255, 60, 0): "or", (0, 0, 0): "bl", (255, 255, 255): "wh", (16, 104, 0): "gr",
                           (240, 0, 0,): "rd", (37, 84, 42): "lgr", (0, 0, 70): "blue", (148, 0, 44): "drd"}

    def read_from_file(self):

        data = ""
        for i in open("back.txt"):
            data += i
        if len(data) >= 1:
            return data
        return None

    def write_to_file(self, s_color):
        open("back.txt", "w").write(s_color)


class Game:
    """Executing game and putting it all together."""
    def __init__(self):
        """Class constructor."""
        pygame.init()
        self.interface = GameInterface()
        self.clock = pygame.time.Clock()
        self.width = 800
        self.height = 600
        self.thick = 20
        self.surf = pygame.display.set_mode((self.width, self.height), 0, 32)

        pygame.display.set_caption("Get early access now!")

    def game_loop(self):
        """Putting all together."""
        x = self.width / 2
        y = self.height / 2
        change_x = 0
        change_y = 0

        apple = Apple(self.thick, self.width, self.height)
        background = UserSettings()

        speed = 0
        start = True
        start2 = True
        over = False
        g_exit = False
        snake_body = []
        snake_len = 1
        if background.read_from_file() is not None:
            c = background.read_from_file().split('\t')[0]
            s_color = self.interface.color_choose(c)
            f = background.read_from_file().split('\t')[1]
            f_color = self.interface.color_choose(f)
        else:
            s_color = self.interface.color_choose("lgr")
            f_color = self.interface.color_choose("or")

        while not g_exit:

            while start2:
                self.interface.start_menu_colors(self.surf, s_color, f_color)
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_g:
                            s_color = self.interface.color_choose("lgr")
                            f_color = self.interface.color_choose("or")
                        elif event.key == K_b:
                            s_color = self.interface.color_choose("bl")
                            f_color = self.interface.color_choose("wh")
                        elif event.key == K_r:
                            s_color = self.interface.color_choose("drd")
                            f_color = self.interface.color_choose("bl")
                        elif event.key == K_l:
                            s_color = self.interface.color_choose("blue")
                            f_color = self.interface.color_choose("or")
                        elif event.key == K_q:
                            self.interface.exit(self.surf, s_color, f_color)

                        else:
                            continue
                        background.write_to_file(background.inv_colors[s_color] + '\t' + background.inv_colors[f_color])

                        start2 = False

            while start:
                self.interface.start_menu(self.surf, s_color, f_color)  # displaying start choice and message
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_s:
                            speed = 2
                        elif event.key == K_e:
                            speed = 4
                        elif event.key == K_n:
                            speed = 6
                        elif event.key == K_q:
                            self.interface.exit(self.surf, s_color, f_color)

                        else:
                            continue
                        start = False

            while over:
                if snake_len > 50 and 6 > speed == 4 or snake_len > 70 and speed == 6:
                    self.interface.excellent(self.surf, s_color, f_color)  # displaying game over message
                    pygame.display.update()

                else:
                    self.interface.end_choice(self.surf, s_color, f_color)

            for event in pygame.event.get():  # quit option
                if event.type == QUIT:
                    pygame.quit()
                    g_exit = True

                elif event.type == KEYDOWN:  # adjusting controls
                    if event.key == K_UP and change_y != speed:
                        change_y = -speed
                        change_x = 0
                    elif event.key == K_DOWN and change_y != -speed:
                        change_y = speed
                        change_x = 0
                    elif event.key == K_LEFT and change_x != speed:
                        change_x = -speed
                        change_y = 0
                    elif event.key == K_RIGHT and change_x != -speed:
                        change_x = speed
                        change_y = 0
                    elif event.key == K_q:
                        self.interface.exit(self.surf, s_color, f_color)

            # setting borders around rhe screen, i.e. collision case
            if x < 0 or x >= self.width - self.thick or y < 0 or y >= self.height - self.thick:
                over = True

            x += change_x  # incrementing speed to coordinates
            y += change_y

            snake_head = list([x, y])  # point, at which current rectangle is located

            snake_body.append(snake_head)  # appending point to snakegame list

            self.surf.fill(s_color)  # re-filling background every time, so rectangle stays in desired size
            if s_color == self.interface.color_choose("drd"):
                apple.draw_apple(self.surf, self.interface.color_choose("bl"))  # drawing an apple at the board
            elif s_color == self.interface.color_choose("bl"):
                apple.draw_apple(self.surf, self.interface.color_choose("wh"))
            else:
                apple.draw_apple(self.surf, self.interface.color_choose("rd"))

            if len(snake_body) > snake_len:  # a limit, so snakegame doesn't grow by itself
                snake_body.remove(snake_body[0])

            for segment in snake_body[1:len(snake_body) - 1]:  # collision with snakegame itself
                if segment == snake_head:
                    over = True
            if s_color == self.interface.color_choose("drd"):
                self.snake_segments(snake_body, self.thick, self.interface.colors["bl"])  # draw a snakegame
            elif s_color == self.interface.color_choose("bl"):
                self.snake_segments(snake_body, self.thick, self.interface.colors["wh"])
            else:
                self.snake_segments(snake_body, self.thick, self.interface.colors["rd"])
            pygame.display.update()

            # re-setting the apple coordinates if snakegame eats previous one, thus drawing new apple
            if x in range(apple.randx - 18, apple.randx + 18) and y in range(apple.randy - 18, apple.randy + 18):
                apple.randx = round(random.choice(range(self.thick, self.width - self.thick)))
                apple.randy = round(random.choice(range(self.thick, self.height - self.thick)))
                # adjusting new limit, thus drawing 1 additional segment when snakegame eats an apple
                snake_len += 3


            # frequency of screen update, i.e. main while-loop repeating speed
            self.clock.tick(90)  # fps

    def snake_segments(self, snake_body, thick, body_color):
        """Adding segments to the snakegame."""
        for xy in snake_body:  # adding segments
            pygame.draw.rect(self.surf, body_color, (xy[0], xy[1], thick, thick))

game = Game()
game.game_loop()
