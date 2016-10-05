"""Drawing garden"""
from graphics import *

def fence_width(a, nr):
    """Count fence width.

    :param a: one fence stick width.
    :param nr: number of fence sticks.
    :return: Return fence width.
    """
    return a * (nr * 2 + 1)


def tree_height(a):
    """Count tree height.

    :param a: one fence stick width.
    :return: Return tree height.
    """
    return 18 * a


def draw_tree(x, y, a, win):
    """Draw tree.

    :param x: X starting point for tree.
    :param y: Y starting point for tree.
    :param a: one fence stick width.
    :param win: link for window
    :return: Draw tree with brown trunk and green leaves.
    """
    tree = Rectangle(Point(x, y), Point(x + a, y - 9 * a))
    tree_leaves = Circle(Point(x + 0.5 * a, y - 13.5 * a), 4.5 * a)
    tree.setFill("brown")
    tree_leaves.setFill("green")
    tree.draw(win)
    tree_leaves.draw(win)


def draw_fence(x, y, a, nr, b, win):
    """Draw fence.

    :param x: X starting point for fence.
    :param y: Y starting point for fence.
    :param a: one fence stick width.
    :param nr: number of fence sticks.
    :param b: garden width or image width.
    :param win: link for window
    :return: Draw yellow fence.
    """
    horizonal_fence_1 = Rectangle(Point(x, y - a), Point(x + b, y - 2 * a))
    horizonal_fence_2 = Rectangle(Point(x, y - 8 * a), Point(x + b, y - 9 * a))
    horizonal_fence_1.setFill("yellow")
    horizonal_fence_2.setFill("yellow")
    horizonal_fence_1.draw(win)
    horizonal_fence_2.draw(win)
    for i in range(nr):
        vertical_fence = Rectangle(Point(a + i * 2 * a, y), Point(2 * a + i * 2 * a, y - 10 * a))
        vertical_fence.setFill("yellow")
        vertical_fence.draw(win)


def main():
    """Draw garden.

    :return: Draw garden with 3 trees and fence.
    """
    a = 5
    nr = 100
    win = GraphWin("My Garden", fence_width(a, nr) + 1, 20 * a + 1)
    number_of_trees = 3
    dist = (fence_width(a, nr) - number_of_trees * 9 * a) / 6
    for i in range(3):
        draw_tree((dist + 4 * a) + (9 * a + 2 * dist) * i, tree_height(a), a, win)
    draw_fence(0, 20 * a, a, nr, fence_width(a, nr), win)
    win.getMouse()# pause for click in window
    win.close()
main()
