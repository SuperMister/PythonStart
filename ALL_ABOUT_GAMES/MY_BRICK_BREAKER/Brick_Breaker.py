"""BRICK BREAKER GAME."""

import pygame
import random


from pygame.locals import *


class GameInterface:
    """User interface."""

    def __init__(self):
        pass

    @staticmethod
    def message(message, xy, surf, f_color):
        """Add text to the surface. Big font."""
        font = pygame.font.SysFont(None, 50)  # choose font
        screen_text = font.render(message, True, f_color)  # add text to the surface
        surf.blit(screen_text, xy)  # draw text onto surface

    @staticmethod
    def text_in_game(message, xy, surf, f_color):
        """Add text to the surface. Small font."""
        font = pygame.font.SysFont(None, 30)
        screen_text = font.render(message, True, f_color)
        surf.blit(screen_text, xy)

    def start_menu_colors(self, surf, s_color, f_color):
        """Asking user for choosing background colors."""
        x = 50
        y = 90
        surf.fill(s_color)  # First filling, then putting text to use
        self.message("Select your favourite colors:", [x, y], surf, f_color)
        self.message("G - for green theme.", [x, y + 75], surf, f_color)
        self.message("L - for blue theme.", [x, y + 150], surf, f_color)
        self.message("R - for red theme.", [x, y + 225], surf, f_color)
        self.message("B - for girl theme.", [x, y + 300], surf, (148, 0, 211))
        self.message("Q - exit", [x, y + 375], surf, f_color)
        pygame.display.update()

    def game_info(self, surf, f_color):
        """Show user info about game controls."""
        x = 200
        y = 250
        self.text_in_game("Use arrows  <=  and  =>  to move platform", [x, y + 125], surf, f_color)
        self.text_in_game("Press SPACE to launch the ball", [x, y + 175], surf, f_color)

    def difficulty_choice(self, surf, s_color, f_color):
        """Asking user for the difficulty level."""
        x = 50
        y = 90

        surf.fill(s_color)  # First filling, then putting text to use
        self.message("Select your difficulty: ", [x, y], surf, f_color)
        self.message("\'E\' - easy level", [x, y + 100], surf, f_color)
        self.message("\'M\' - medium level", [x, y + 175], surf, f_color)
        self.message("\'I\' - INSANE, think twice!", [x, y + 250], surf, f_color)
        self.message("\'X\' - HARDCORE! 5 lives but it won't help you!", [x, y + 325], surf, f_color)
        self.message("Q - EXIT", [x, y + 425], surf, f_color)
        pygame.display.update()

    def end_choice(self, surf, s_color, f_color):
        """User menu after game end."""
        x = 50
        y = 100
        game_st = Game()  # Creating game class object
        surf.fill(s_color)
        self.message("GAME OVER!!!", [x, y], surf, f_color)
        self.text_in_game("Press Q to exit the game! Or SPACE to play again!", [x, y + 300], surf, f_color)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:  # If the key is pressed
                if event.key == pygame.K_q:
                    raise SystemExit
                elif event.key == pygame.K_SPACE:
                    game_st.game_run()  # Starting game again

    def lives_left(self, surf, f_color, lives):
        """Adding info about lives left to the gaming screen."""
        x = 330
        y = 5
        self.text_in_game("Your lives: " + str(lives), [x, y], surf, f_color)


class Ball:
    """Drawing a ball."""

    def __init__(self):
        """Defining radius."""
        self.rad = 8

    def draw_a_ball(self, surf, xy, s_color):
        """Drawing the ball."""
        pygame.draw.circle(surf, s_color, xy, self.rad)


class Bricks:
    """Creating bricks."""

    def __init__(self):
        """List of brick coordinates."""
        self.coordinates = []

    def brick_coordinates(self, amount):
        """Computing brick coordinates."""
        x = 120
        y = 35
        step_x = 0
        step_y = 0

        for j in range(amount):  # Amount of brick lines
            if step_y >= 275:  # Exception for bricks not being too close
                break
            for i in range(7):  # 7 columns of bricks
                self.coordinates.append(list([x + step_x, y + step_y]))
                step_x += 80
            step_y += 30
            step_x = 0
        return self.coordinates

    def draw_bricks(self, surf, s_color, length, thick):
        """Drawing bricks at the screen."""
        for i in self.coordinates:
            pygame.draw.rect(surf, s_color, (i[0], i[1], length, thick))


class Game:
    """Executing game."""

    def __init__(self):
        """Defining variables."""
        pygame.init()
        self.interface = GameInterface()  # GameInterface class object

        self.width = 800  # Display width
        self.height = 600  # Display height
        self.stick_length = 80  # Stick length
        self.surf = pygame.display.set_mode((self.width, self.height))  # set display

        self.colors = {"or": (255, 69, 0), "bl": (0, 0, 0), "wh": (255, 255, 255), "yel": (255, 255, 0),
                       "rd": (240, 0, 0), "lgr": (0, 150, 30), "blue": (0, 0, 150), "pink": (255, 20, 147)}
        # Dict of colours

        pygame.display.set_caption("Break a Brick")

        self.x_b = int(self.width / 2)  # Ball coordinate x
        self.y_b = self.height - 30  # Ball coordinate y
        self.x = int(self.width / 2 - self.stick_length / 2)  # Stick coordinate x
        self.y = self.height - 20  # Stick coordinate y

        self.ball = Ball()  # Ball class object
        self.brick = Bricks()  # Bricks class object
        self.change_x_b = 0  # Ball movement in X direction
        self.change_y_b = 0  # Ball movement in Y direction
        self.ball_speed = 3  # Ball speed
        self.speed = 5  # Platform speed
        self.s_color = self.choose_color("or")
        self.f_color = self.choose_color("wh")
        self.change_x = 0  # Platform movement.
        self.exit = False
        self.start = False
        self.start_menu = True
        self.start_diff = True

        self.clock = pygame.time.Clock()  # For frame updating.

        self.length = 70  # Length of the bricks
        self.brick_thick = 10  # Thickness of the bricks
        self.borders = 50  # Game borders
        self.lives = 3  # Amount of lives in game

    def choose_color(self, s_color):
        """Choosing colors."""
        return self.colors[s_color]

    def draw_borders(self, s_color, width, height):
        """Drawing borders on the right and left."""
        pygame.draw.rect(self.surf, s_color, (0, 0, self.borders, height))  # Left border
        pygame.draw.rect(self.surf, s_color, (width - self.borders, 0, self.borders, height))  # Right border

    def game_controls(self):
        """Defining game controls."""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                self.exit = True

            elif event.type == KEYDOWN:  # Depending on a key pressed subtract or add points to x or y
                if event.key == K_LEFT:
                    self.change_x = -self.speed

                elif event.key == K_RIGHT:
                    self.change_x = self.speed

                elif event.key == K_q:
                    raise SystemExit

                if not self.start:  # Initial state (beginning)
                    if event.key == K_SPACE:
                        self.change_y_b = -self.ball_speed
                        self.change_x_b = random.choice(range(-self.ball_speed, self.ball_speed))
                        self.start = True

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    self.change_x = 0  # Stop platform moving.

    def platform_borders(self):
        """Defining platform borders."""
        if self.x <= self.borders:  # Platform at the left border.
            self.change_x = 0
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.change_x = self.speed
                if not self.start:  # Start the game while platform is at the left border.
                    if event.key == K_SPACE:
                        self.change_y_b = -self.ball_speed
                        self.change_x_b = random.choice(range(-self.ball_speed, self.ball_speed))
                        self.start = True

        elif self.x >= self.width - (self.borders + self.stick_length):  # Platform at the right border.
            self.change_x = 0
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.change_x = -self.speed
                if not self.start:  # Start the game while platform is at the right border.
                    if event.key == K_SPACE:
                        self.change_y_b = -self.ball_speed
                        self.change_x_b = random.choice(range(-self.ball_speed, self.ball_speed))
                        self.start = True
        else:
            self.game_controls()

    def ball_borders(self):
        """Defining ball borders and ball directions."""
        if not self.start:  # Set the ball on the middle of the platform.
            self.x_b = self.x + int(self.stick_length / 2)
            self.y_b = self.y - self.ball.rad

        if self.x_b >= self.width - (self.borders + self.ball.rad):  # Ball touches right border.
            self.change_x_b = -self.ball_speed
        elif self.x_b <= self.borders + self.ball.rad:  # Ball touches left border.
            self.change_x_b = self.ball_speed
        elif self.y_b <= self.ball.rad:  # Ball touches top border.
            self.change_y_b = self.ball_speed

    def ball_movement(self):
        """Setting ball movement schematics. Ball bouncing from the platform."""
        if self.start:
            if self.x_b in range(self.x + 10, self.x + 40) and self.y_b in range(self.y - self.ball.rad, self.y):
                self.change_y_b = -self.ball_speed
                self.change_x_b = int(- self.ball_speed / 2)

            elif self.x_b in range(self.x - 20, self.x + 10) and self.y_b in range(self.y - self.ball.rad, self.y):
                self.change_y_b = -self.ball_speed
                self.change_x_b = -self.ball_speed

            elif self.x_b in range(self.x + 40, self.x + 70) and self.y_b in range(self.y - self.ball.rad, self.y):
                self.change_y_b = -self.ball_speed
                self.change_x_b = int(self.ball_speed / 2)

            elif self.x_b in range(self.x + 70, self.x + 100) and self.y_b in range(self.y - self.ball.rad, self.y):
                self.change_y_b = -self.ball_speed
                self.change_x_b = self.ball_speed

            elif self.y_b >= self.height:  # Ball falls behind platform
                self.x_b = self.x + int(self.stick_length / 2) + self.change_x
                self.y_b = self.y - self.ball.rad  # Set ball on the middle of the platform.
                self.change_x_b = self.change_x
                self.change_y_b = 0
                self.lives -= 1  # Lose 1 life.
                self.start = False

    def brick_remove(self):
        """Removing the brick from the screen in case of collision."""
        for i in self.brick.coordinates:  # For all bricks.
            rect = pygame.Rect(i[0], i[1], self.length, self.brick_thick)
            if rect.collidepoint(self.x_b + self.ball.rad, self.y_b) or \
                    rect.collidepoint(self.x_b - self.ball.rad, self.y_b) or \
                    rect.collidepoint(self.x_b, self.y_b + self.ball.rad) or \
                    rect.collidepoint(self.x_b, self.y_b - self.ball.rad) or \
                    rect.collidepoint(self.x_b + self.ball.rad, self.y_b + self.ball.rad) or \
                    rect.collidepoint(self.x_b - self.ball.rad, self.y_b - self.ball.rad):
                    # If point is in the rect, remove brick.
                self.brick.coordinates.remove(i)
                if self.change_y_b == self.ball_speed:  # If ball hits the brick from the upside.
                    self.change_y_b = -self.ball_speed
                else:
                    self.change_y_b = self.ball_speed  # If ball hits the brick from the downside.

    def start_colour_choice(self):
        """Activating user menu for choosing colours."""
        while self.start_menu:
            self.interface.start_menu_colors(self.surf, self.s_color, self.f_color)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_g:
                        self.s_color = self.choose_color("lgr")
                        self.f_color = self.choose_color("or")
                    elif event.key == K_r:
                        self.s_color = self.choose_color("rd")
                        self.f_color = self.choose_color("wh")
                    elif event.key == K_l:
                        self.s_color = self.choose_color("blue")
                        self.f_color = self.choose_color("wh")
                    elif event.key == K_b:
                        self.s_color = self.choose_color("pink")
                        self.f_color = self.choose_color("yel")
                    elif event.key == K_q:
                        raise SystemExit
                    else:
                        continue
                    self.start_menu = False

    def difficulties(self):
        """Activating user menu for choosing difficulties."""
        while self.start_diff:
            self.interface.difficulty_choice(self.surf, self.s_color, self.f_color)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_e:
                        self.ball_speed = 2
                        self.speed = 5
                    elif event.key == K_m:
                        self.ball_speed = 3
                        self.speed = 5
                    elif event.key == K_i:
                        self.ball_speed = 5
                        self.speed = 6
                    elif event.key == K_x:
                        self.ball_speed = 9
                        self.speed = 7
                        self.lives = 5
                    elif event.key == K_q:
                        raise SystemExit
                    else:
                        continue
                    self.start_diff = False

    def game_instructions(self):
        """Show user info about game controls before game starts."""
        if not self.start:
            self.interface.game_info(self.surf, self.f_color)

    def game_over(self):
        """Activating game end user menu."""
        if not self.brick.coordinates or self.lives == 0:
            self.interface.end_choice(self.surf, self.s_color, self.f_color)

    def game_run(self):
        """Main game loop."""
        amount = 10  # Amount of brick lines
        self.brick.brick_coordinates(amount)  # Computing all brick coordinates

        while True:
            self.start_colour_choice()  # Colour choose
            self.difficulties()  # Difficulty choose
            self.platform_borders()  # Setting platform borders.
            self.ball_borders()  # Setting ball movement borders.
            self.ball_movement()  # Define ball bouncing.

            self.x += self.change_x  # Platform move

            self.x_b += self.change_x_b  # Ball move x
            self.y_b += self.change_y_b  # Ball move y

            self.surf.fill(self.colors["bl"])  # Re-filling the background, so rectangle stays as one piece
            self.game_instructions()  # Show user game info

            self.ball.draw_a_ball(self.surf, [self.x_b, self.y_b], self.choose_color("rd"))  # Draw a ball

            pygame.draw.rect(self.surf, self.s_color, (self.x, self.y, self.stick_length, 10))  # Draw a stick

            self.draw_borders(self.s_color, self.width, self.height)  # Border pillars at the corners

            self.brick.draw_bricks(self.surf, self.s_color, self.length, self.brick_thick)  # Draw bricks

            self.interface.lives_left(self.surf, self.f_color, self.lives)  # Show how many lives left

            self.brick_remove()  # Remove brick when contacting with the ball

            self.game_over()  # Check if game is not over

            pygame.display.update()  # Update display

            self.clock.tick(100)  # Frames per second

game = Game()
game.game_run()
