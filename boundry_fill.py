#boundry fill algorithm:
#this program starts from a pixel which exists anywhere in the screen, and we start coloring it and call its neighbor
##pixels and color it until we reach boundry of the screen

import matplotlib.pyplot as plt

def take_input():
    x, y = map(int, input("Enter the origin: x y : ").split())
    r = int(input("Enter the radius for the circle"))
    fill_color = (input("Enter the color name or hex code")).lower()
    return x, y, r, fill_color

def fill(x, y, fill_color, border_color):
    if

if __name__ == '__main__':
    x, y, r, fill_color = take_input()
    xb = x
    yb = y
    border_color = 'b'
    circle = plt.Circle((x, y), color=border_color, fill=False)
    ax = plt.gca()
    ax.add_artist(circle)
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))
    plt.grid()
    fill(x, y, fill_color, border_color)
    #plt.show()

