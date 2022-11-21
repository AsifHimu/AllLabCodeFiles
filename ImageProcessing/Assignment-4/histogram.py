import matplotlib.pyplot as plt
import cv2
import numpy as np
from pip import main

def main():
    img_path = 'image_RGB.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(grayscale.shape)
    d = dict()
    for x in range(256):
        d[x] = 0
    
    #print(d)
    for x in grayscale:
        for y in x:
            d[y] += 1
   
    #print(d)
   
    x = d.keys()
    y = d.values()
    
    plt.subplot(1,2,1)
    plt.title('Histogram calcHist')
    val = cv2.calcHist([grayscale], [0], None, [256], [0, 256])
    plt.plot(val)
    plt.subplot(1,2,2)
    plt.title('Histogram manually')
    plt.plot(x,y)
    plt.savefig('hist')
    plt.show()  
    

if __name__ == '__main__':
    main()
    