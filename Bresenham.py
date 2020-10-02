#!/usr/bin/python3
import matplotlib.pyplot as plt

x1,y1 = input("Enter the starting point (x1,y1): ").split()
x2,y2 = input("Enter the end point (x2,y2): ").split()


x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

x = x1
y = y1

dx = x2-x1
dy = y2-y1

p = 2 * dy - dx

points_on_x = []
points_on_y = []

while x <= x2:
    points_on_y.append(y)
    points_on_x.append(x)

    x += 1

    if p < 0:
        p = p + 2 * dy

    else:
        p = p + 2 * dy - 2 * dx
        y += 1

print(points_on_x)
print(points_on_y)


plt.plot(points_on_x, points_on_y, marker = 'o')
plt.grid()
plt.show()
