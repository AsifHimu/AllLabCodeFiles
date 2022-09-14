import matplotlib.pyplot as plt
import cv2
import numpy as np
import random


def main():
    img_path = 'village1.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    print(gray.shape)
    
    eqimg = cv2.equalizeHist(gray)
    
    grayhist = cv2.calcHist([gray],[0],None,[256],[0,256])
    eqhist = cv2.calcHist([eqimg],[0],None,[256],[0,256])
    
    plt.subplot(2,2,1)
    plt.title('Garscale')
    plt.imshow(gray,cmap='gray')
    plt.subplot(2, 2, 2)
    plt.title('GarscaleHIST')
    plt.plot(grayhist)
    plt.subplot(2, 2, 3)
    plt.title('Equalized')
    plt.imshow(eqimg, cmap='gray')
    plt.subplot(2, 2, 4)
    plt.title('EqualizedHIST')
    plt.plot(eqhist)
    
    plt.show()
    
    
    
if __name__ == '__main__':
    main()
    