import matplotlib.pyplot as plt
import math
import numpy as np

vf = 20
xf = 0
yf = 0
fighter_x = []
fighter_y = []
bomber_x = []
bomber_y = []

fighter_x.append(xf)
fighter_y.append(yf)
for line in open("./bc.txt"):
    xb, yb = line.strip().split(',')
    xb, yb = int(xb), int(yb)
    bomber_x.append(xb)
    bomber_y.append(yb)

T = len(bomber_x)
for t in range(T):
    dist = np.sqrt((bomber_y[t] - fighter_y[t]) ** 2 + (bomber_x[t] - fighter_x[t]) ** 2)
    print("Distance ={}".format(dist))
    if dist <= 7:
        print("Target caught", end=' ')
        print("at step={}".format(t))
        break
    elif t >= T-1:
        print("Target Escaped", end=' ')
        print("at step={}".format(t))
        break
    else:
        sin = (bomber_y[t] - fighter_y[t])/dist
        cos = (bomber_x[t] - fighter_x[t])/dist

        xf = fighter_x[t] + vf * cos
        yf = fighter_y[t] + vf * sin

        fighter_x.append(xf)
        fighter_y.append(yf)

print(fighter_x,end=' ')
print()
print(fighter_y,end=' ')

plt.plot(fighter_x,fighter_y,"r*")
plt.plot(bomber_x,bomber_y,"b*")
plt.show()