#!/usr/bin/python3
import matplotlib.pyplot as plt

def take_input():
    rx = int(input("Enter the value of rx: "))
    ry = int(input("Enter the value of ty: "))

    x, y = map(int, input("Enter the center x,y: ").split())
    return rx, ry, x, y

def calculation():
    rx, ry, x, y = take_input()

    a = 0
    b = ry
    points_on_x = [a]
    points_on_y = [b]

    #first decision parameter
    p = (ry**2) - ((rx**2)*ry) + ((rx**2)/4)

    #condition to go to the next region
    while 2 * (ry ** 2) * a < 2 * (rx ** 2) * b:
         a += 1
         if p < 0:
            p += (2 * (ry ** 2) * a) + (ry ** 2)
         else:
            b -= 1
            p += (2 * (ry ** 2) * a) - (2 * (rx ** 2) * b) + (ry ** 2)
         points_on_x.extend((a + x, -a + x, -a + x, a + x))
         points_on_y.extend((b + y, b + y, -b + y, -b + y))

    #initial parameter for second region
    p = (ry ** 2) * ((a + 0.5) ** 2) + ((rx ** 2) * ((b - 1) ** 2)) - ((rx**2) * (ry ** 2))
    while b != 0:
        b -= 1
        if p > 0:
            p += (- 2 * (rx ** 2) * b) + (rx ** 2)

        else:
            a += 1
            p += 2 * (ry ** 2) * a - (2 * (rx ** 2) * b) + (rx ** 2)

        points_on_x.extend((a + x, -a + x, -a + x, a + x))
        points_on_y.extend((b + y, b + y, -b + y, -b + y))

    print(points_on_x)
    print(points_on_y)
    plt.plot(points_on_x, points_on_y, 'ro')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    calculation()