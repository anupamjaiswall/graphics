#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
import matplotlib.patches as mpatches

def draw(old_pts, pts):
    p = Polygon(old_pts, closed=False, color='blue')
    p1 = Polygon(pts, closed=False, color='red')
    old_patch = mpatches.Patch(color='blue', label='Before Transformation')
    new_patch = mpatches.Patch(color='red', label='After transformation')
    ax = plt.gca()
    plt.legend(handles = [old_patch,new_patch])
    ax.add_patch(p)
    ax.add_patch(p1)

    #    plt.plot(p,p1)
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 5)
    ax.set_xlabel('Red: After transformation\n'
                  'Blue: Before transformation')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    x1,y1 = map(int, input("Enter the first point of triangle x1, y1 : ").split())
    x2,y2 = map(int, input("Enter the second point of triangle x2, y2 : ").split())
    x3,y3 = map(int, input("Enter the third point of the triangle x3, y3 : ").split())

    theta = int(input("Enter the rotation angle: "))

    old_pts = np.array([[x1,y1],[x2,y2],[x3,y3]])

    #from transformation formula

    M1 = np.array([[round(math.cos(math.radians(theta)),2), round(math.sin(math.radians(theta)),2)],
                   [-round(math.sin(math.radians(theta)),2), round(math.cos(math.radians(theta)),2)]])

    M2 = np.array([[x1, y1],
                   [x2, y2],
                   [x3, y3]])
    T = [[0,-1],[-1,0]]

    Mul = np.matmul(M2, M1)
    Mul = np.matmul(Mul,T)

    #    print(Mul)
    pts = Mul
    draw(old_pts, pts)
