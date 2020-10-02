#!/usr/bin/python3
import matplotlib.pyplot as plt

r = int(input("Enter the radius of the circle: "))
a,b = input("Enter the center of the circle: ").split()
a = int(a)
b = int(b)

points_on_x = [0]
points_on_y = [r]

x = int(0)
y = r

p = 1 - r

while x < y:
    if p < 0:
#        p = p + 2*(x + 1) + 1
         p += 2*x + 3
    else:
#        p = p + 2*(x + 1) + 1 - 2*(y - 1)
        p += 2 * (x - y) + 5
        y -= 1

    x += 1
    points_on_x.extend((a+x,a+x,a-x,a-x,a+y,a+y,a-y,a-y))
    points_on_y.extend((b+y,b-y,b+y,b-y,b+x,b-x,b+x,b-x))

counter = int(0)

print(points_on_x)
print(points_on_y)

plt.plot(points_on_x,points_on_y,'ro')
plt.grid()
plt.show()
