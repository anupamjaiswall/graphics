#!/usr/bin/python3

#programmer name: ANUPAM JAISWAL
#DATE: 01/09/2020

import matplotlib.pyplot as plt

x1,y1 = input("Enter the first point (x1,y1): ").split()
x2,y2 = input("Enter the second point (x2,y2): ").split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

dx = x2 - x1
dy = y2 - y1

points_on_x = [x1]
points_on_y = [y1]

steps = abs(dx) if abs(dx) >= abs(dy) else dy

steps = int(steps)

xIncr = dx/steps
yIncr = dy/steps

print(yIncr)
for x in range( 0, steps  ):
    x1 += xIncr
    y1 += yIncr
    points_on_x.append( round( x1 ) )
    points_on_y.append( round( y1 ) )

print( points_on_x )
print( points_on_y )


plt.plot( points_on_x, points_on_y, marker = 'o' )
plt.grid()
plt.show()
