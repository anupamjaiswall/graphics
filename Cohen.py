#import matplotlib.pyplot as plt

def draw(x1, x2, y1, y2):




#input for the line to be displayed
x1, y1 = map(int, input("Enter the first point of the line : x1 y1 :").split())
x2, y2 = map(int, input("Enter the second point of the line: x2 y2 :").split())

#input to select the screen
x_lower_left, y_lower_left = map(int, input("Enter the lower left corner: xll yll :").split())
x_upper_right, y_upper_right = map(int, input("Enter the upper right corner: xur yur: ").split())

#remaining two cordinates:
x_upper_left = x_lower_left
y_upper_left = y_upper_right
x_lower_right = x_upper_right
y_lower_right = x_lower_left

#bits:
bit1 = [0, 0, 0, 0]
bit2 = [0, 0, 0, 0]

#for first endpoint bits:
bit1[3] = 1 if x1 < x_lower_left else 0
bit1[2] = 1 if x1 > x_lower_right else 0
bit1[1] = 1 if y1 < y_lower_left else 0
bit1[0] = 1 if y1 > y_upper_right else 0

#for second endpoint bits:
bit2[3] = 1 if x2 < x_lower_left else 0
bit2[2] = 1 if x2 > x_lower_right else 0
bit2[1] = 1 if y2 < y_lower_left else 0
bit2[0] = 1 if y2 > y_upper_right else 0

#visibility
counter = 0
not_visible_flag = 0
totally_visible_flag = 1
while counter < 4:
    if bit1[counter] and bit2[counter]:
        not_visible_flag = 1
        print("This line is not visible :/")
        exit(0)
    counter += 1

if 1 in bit1 or 1 in bit2:
    totally_visible_flag = 0

if totally_visible_flag:
    print("This line is totally visible")
    draw(x1, x2, y1, y2)
    exit(0)
else:
    #since counter = 4
    while counter > 0:
        if bit1[counter] == 1:
            x
        counter -= 1
    slope = (y2 - y1)/(x2 - x1)


