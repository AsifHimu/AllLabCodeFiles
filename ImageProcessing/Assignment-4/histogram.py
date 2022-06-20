import matplotlib.pyplot as plt
import cv2
import numpy as np
from pip import main

def main():
    img_path = 'nature.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(grayscale.shape)
    d = dict()
    for x in range(256):
        d[x] = 0
    
    print(d)
    for x in grayscale:
        for y in x:
            d[y] += 1
   
    print(d)
   
    x = d.keys()
    y = d.values()
    
    plt.subplot(2,1,1)
    plt.title('GrayscaleUsingFunction')
    val = cv2.calcHist([grayscale], [0], None, [256], [0, 256])
    plt.plot(val)
    plt.subplot(2,1,2)
    plt.title('GrayscaleUsingImplementation')
    plt.plot(x,y)
    plt.savefig('hist')
    plt.show()  
    

if __name__ == '__main__':
    main()
    