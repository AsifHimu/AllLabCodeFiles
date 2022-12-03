import matplotlib.pyplot as plt
import cv2
import numpy as np
import random


def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    eqimg = cv2.equalizeHist(grayscale)
    
    grayhist = cv2.calcHist([grayscale],[0],None,[256],[0,256])
    eqhist = cv2.calcHist([eqimg],[0],None,[256],[0,256])
    
    plt.subplot(1,2,1)
    plt.title('Grayhist')
    plt.plot(grayhist)
    
    plt.subplot(1,2,2)
    plt.title('EqualizeHist')
    plt.plot(eqhist)
    
    plt.show()
if __name__ == '__main__':
    main()