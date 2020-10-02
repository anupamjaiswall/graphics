#!/usr/bin/python3

#import matplotlib.pyplot as plt

m = float(input("Enter the slope: "))
x0,y0= input("""Enter the starting point (a,b): """).split()
x0 = float(x0)
y0 = float(y0)
b = int(input("Enter the intersecting point: "))

points_on_x = [x0]
points_on_y = [y0]
for x1 in range(1,6):
    y1 = ( m * x1 ) + b
    y1 = round(y1)
    points_on_x.append(x1)
    points_on_y.append(y1)
    x0 = x1
    y0 = y1


print(points_on_x)
print(points_on_y)

plt.plot(points_on_x,points_on_y, marker = 'o')
plt.grid()
plt.show()



#drawing for 5 points


