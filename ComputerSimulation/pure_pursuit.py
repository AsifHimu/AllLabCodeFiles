import math
import numpy as np
import matplotlib.pyplot as plt
import pygame

vf = 20  # fighter velocity
# caught_thresh = 10
# escaped_thresh = 10

xf = 0
yf = 0

bomber_x = []
bomber_y = []

fighter_x = []
fighter_y = []

fighter_x.append(xf)
fighter_y.append(yf)

for line in open('./bc.txt'):
    xb, yb = line.strip().split(',')
    xb, yb = int(xb), int(yb)
    bomber_x.append(xb)
    bomber_y.append(yb)

# print(bomber_x,end=' ')
# print(bomber_y,end=' ')
T = len(bomber_x)
for t in range(T):
    dist = np.sqrt((bomber_y[t] - fighter_y[t]) ** 2 + (bomber_x[t] - fighter_x[t]) ** 2)
    print("distance ={}".format(dist))
    if dist <= 7:
        val = t
        print('Target caught', end=' ')
        print("at Step = {}".format(t))
        break
    elif t >= T - 1:
        val = t
        print('Escaped', end=' ')
        print("at Step = {}".format(t))
        break
    else:
        sin = (bomber_y[t] - fighter_y[t]) / dist
        cos = (bomber_x[t] - fighter_x[t]) / dist

        xf = fighter_x[t] + vf * cos
        yf = fighter_y[t] + vf * sin

        fighter_x.append(xf)
        fighter_y.append(yf)

print(fighter_x, end=' ')
print()
print(fighter_y, end=' ')
# by using matplotlib
plt.plot(fighter_x, fighter_y, 'red')
plt.plot(bomber_x, bomber_y, 'blue')
plt.show()

