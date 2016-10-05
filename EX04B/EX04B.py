"""Draw stair construction with door."""
from graphics import *


a = 20
nr = 7


def total_width(a, nr):
    """Count picture total width.

    :param a: size.
    :param nr: number of steps.
    :return: Return picture width.
    """
    return 2 * a * nr + 10 * a


def total_height(a, nr):
    """Count picture total height.

    :param a: size.
    :param nr: number of steps.
    :return: Return picture height.
    """
    return a * nr + 6 * a


def draw_line(x1, y1, x2, y2, th, win):
    """Draw line.

    :param x1: X starting point for line.
    :param y1: Y starting point for line.
    :param x2: X finishing point for line.
    :param y2: Y finishing point for line.
    :param th: line width.
    :param win: link for window.
    :return: Return line.
    """
    basic_line = Line(Point(x1, y1), Point(x2, y2))
    basic_line.setWidth(th)
    basic_line.draw(win)


def draw_strair_constr(a, x, y, nr, th, win):
    """Draw stair construction.

    :param a: size.
    :param x: X starting point for construction.
    :param y: Y starting point for construction.
    :param nr: number of steps.
    :param th: line width.
    :param win: link for window.
    :return: Return picture of stair construction.
    """
    draw_line(x, y, x, y - a / 3, th, win)
    draw_line(x, y - a / 3, x + 6 * a, y - a / 3, th, win)
    for i in range(nr):
        draw_line(x + 6 * a + 2 * a * i, y - a / 3 - a * i,
                  x + 6 * a + 2 * a * i, y - 4 * a / 3 - a * i, th, win)
        draw_line(x + 6 * a + 2 * a * i, y - 4 * a / 3 - a * i,
                  x + 8 * a + 2 * a * i, y - a / 3 - a - a * i, th, win)
    draw_line(x + 6 * a + 2 * a * nr, y - nr * a - a / 3,
              x + 10 * a + 2 * a * nr, y - nr * a - a / 3, th, win)
    draw_line(x + 10 * a + 2 * a * nr, y - nr * a - a / 3,
              x + 10 * a + 2 * a * nr, y - nr * a, th, win)
    draw_line(x + 10 * a + 2 * a * nr, y - nr * a,
              x + 6 * a + 2 * a * nr, y - nr * a, th, win)
    draw_line(x + 6 * a + 2 * a * nr, y - nr * a, x + 6 * a, y, th, win)
    draw_line(x + 6 * a, y, x, y, th, win)


def draw_reiling(x1, y1, x2, y2, d, th, win):
    """Draw reiling.

    :param x1: X first starting point for reiling.
    :param y1: Y first starting point for reiling.
    :param x2: X second starting point for reiling.
    :param y2: Y second starting point for reiling.
    :param d: reiling width.
    :param th: line width.
    :param win: link for window.
    :return: Return picture of reiling.
    """
    draw_line(x1, y1, x1, y1 - d, th, win)
    draw_line(x1, y1, x1 + 2 * a * (nr - 1), y1 - a * (nr - 1), th, win)
    draw_line(x2, y2, x2, y2 - d, th, win)
    draw_line(x2, y2 - d, x2 - 2 * a * (nr - 1),
              y2 + a * (nr - 1) - d, th, win)


def draw_door(x, y, b, h, th, win):
    """Draw door.

    :param x: X starting point for door.
    :param y: Y starting point for door.
    :param b: step width.
    :param h: door height.
    :param th: line width.
    :param win: link for window.
    :return: Return picture of the door.
    """
    draw_line(x, y, x, y - h, th, win)
    draw_line(x, y - h, x + b, y - h, th, win)
    draw_line(x + b, y - h, x + b, y, th, win)
    draw_line(x + 3 * b / 4, y - h / 2, x + 3 * b / 4 + 2 * a / 3,
              y - h / 2, th, win)


def main():
    """Draw all functions together.

    :return: Return picture of stair construction and door.
    """
    th = 1
    y = total_height(a, nr)
    x = 0
    d = a / 3
    b = 4 * a - a / 3
    h = 6 * a - a / 3
    win = GraphWin("My ", total_width(a, nr) + 1, total_height(a, nr) + 1)
    draw_strair_constr(a, x, y, nr, th, win)
    draw_reiling(6 * a, y - 4 * a - a / 3, 6 * a + 2 * a * (nr - 1),
                 y - (4 * a + a * (nr - 1) + a / 3), d, th, win)
    draw_door(6 * a + 2 * a * nr, y - nr * a - a / 3, b, h, th, win)
    win.getMouse()
    win.close()
main()
