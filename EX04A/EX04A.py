"""
Peafunktsioon „main()“ kutsub välja/käivitab järgmised alamfunktsioonid:

                  fence_width(a, nr) leiab aia laiuse;

                  tree_height(a) leiab puu kõrguse;

                  draw_tree(x, y, a, win) joonistab puu;

                  draw_fence(x, y, a, nr, b,  win) joonistab aia.

Funktsioonide parameetrid:

a – ühikmõõt/lipi laius

nr – lippide arv

x, y – aia ja puu alguskoordinaadid

b – aia laius ehk rõhtpuu pikkus

win – viit graafikaaknale

"""
from graphics import *

def fence_width(a, nr):
    return a * (nr * 2 + 1)
def tree_height(a):
    return 18 * a

def draw_tree(x, y, a, win):
    tree = Rectangle(Point(x, y), Point(x + a, y - 9*a ))
    tree.setFill("brown")
    tree.draw(win)
    tree_leaves = Circle(Point(x + 0.5 * a, y - 13.5 * a), 4.5 * a)
    tree_leaves.setFill("green")
    tree_leaves.draw(win)

def draw_fence(x, y, a, nr, b, win):
    horizonal_fence_1 = Rectangle(Point(x, y - a), Point(x + b, y - 2 * a ))
    horizonal_fence_2 = Rectangle(Point(x, y - 8 * a), Point(x + b, y - 9 * a))
    horizonal_fence_1.setFill("yellow")
    horizonal_fence_2.setFill("yellow")
    horizonal_fence_1.draw(win)
    horizonal_fence_2.draw(win)
    for i in range (nr):
        vertical_fence = Rectangle(Point(a + i * 2 * a, y), Point(2 * a + i * 2 * a, y - 10 * a))
        vertical_fence.setFill("yellow")
        vertical_fence.draw(win)

def main():
    a = 25
    nr = 21
    win = GraphWin("My Garden", fence_width(a, nr) + 1, 20 * a + 1)
    number_of_trees = 3
    dist = (fence_width(a, nr) - number_of_trees * 9 * a) / 6
    for i in range (3):
        draw_tree((dist + 4 * a) + (9 * a + 2 * dist) * i, tree_height(a), a, win)
    draw_fence(0, 20 * a, a, nr, fence_width(a, nr), win)




    win.getMouse() # pause for click in window
    win.close()
main()
