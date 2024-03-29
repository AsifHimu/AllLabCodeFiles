import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    
    d = dict()
    for i in range(256):
        d[i] = 0
    for x in grayscale:
        for y in x:
            d[y] = d[y] + 1
    
    #print(d)
    x = d.keys()
    y = d.values()
    
    val = cv2.calcHist([grayscale],[0],None,[256],[0,256])
    
    plt.subplot(1,2,1)
    plt.title('Hist without function')
    plt.plot(x,y)
    
    plt.subplot(1,2,2)
    plt.title('Hist with function')
    plt.plot(val)
    
    plt.show()
if __name__ == '__main__':
    main()