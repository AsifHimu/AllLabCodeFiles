import random
import matplotlib.pyplot as plt
import numpy as np

vf = 20
t = 0
flag = True
xf = random.randint(0, 1000)
yf = random.randint(0, 1000)

fighter_x = []
fighter_y = []
bomber_x = []
bomber_y = []
fighter_x.append(xf)
fighter_y.append(yf)

while flag:
    xb = random.randint(0, 1000)
    yb = random.randint(0, 1000)
    bomber_x.append(xb)
    bomber_y.append(yb)

    dist = np.sqrt((yb - yf) ** 2 + (xb - xf) ** 2)
    print("Distance = {}".format(dist))
    if dist < 100:
        flag = 0
        print("Target caught",end=' ')
        print("at Step = {}".format(t))
    elif dist > 900:
        flag = 0
        print("Target Escaped",end=' ')
        print("at Step = {}".format(t))
    else:
        sin = (yb - yf)/dist
        cos = (xb - xf)/dist
        t = t+1
        xf = xf + vf * cos
        yf = yf + vf * sin

        fighter_x.append(xf)
        fighter_y.append(yf)

plt.plot(fighter_x,fighter_y,"red")
plt.plot(bomber_x,bomber_y,"Green")
plt.show()