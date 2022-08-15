import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    
    d = dict()
    #print(d)
    #val = np.array([[1,2,3],[4,1,2],[1,3,9]])
    for i in range(256):
        d[i] = 0
    #print(d)
    
    for x in gray:
        for y in x:
            d[y] = d[y] + 1
    #print(d)
    x = d.keys()
    y = d.values()
    plt.subplot(2,1,1)
    plt.title('withoutfunc')
    plt.plot(x,y)
    plt.subplot(2,1,2)
    plt.title('withfunc')
    val = cv2.calcHist([gray], [0], None, [256], [0, 256])
    plt.plot(val)
    plt.show()
    
if __name__ == '__main__':
    main()
        