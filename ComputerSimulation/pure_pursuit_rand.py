import numpy as np
import matplotlib.pyplot as plt
import random
flag = 1
t = 0
vf = 20
xf = random.randint(0, 1000)
yf = random.randint(0, 1000);
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

    dist = np.sqrt((yb - yf)**2 + (xb - xf)**2)
    if dist < 100:
        flag = 0
        print('target caught')
    elif dist > 900:
        flag = 0
        print('Escaped')
    else:
        sin = (yb - yf)/dist
        cos = (xb - xf)/dist
        t = t+1
        xf = xf + vf*cos
        yf = yf + vf*sin

        fighter_x.append(xf)
        fighter_y.append(yf)

plt.plot(fighter_x, fighter_y, "red")
plt.plot(bomber_x, bomber_y, "green")
plt.show()
