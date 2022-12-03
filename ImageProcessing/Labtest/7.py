import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

def main():
    img_path = 'village.jpg'
    rgb = plt.imread(img_path)
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    row = grayscale.shape[0]
    col = grayscale.shape[1]
    
    left = grayscale.copy()
    right = grayscale.copy()
    band = grayscale.copy()
    
    left = left - 68
    right = right + 30
    for i in range(row):
        for j in range(col):
            if band[i][j] <= 50:
                band[i][j] = 50
            elif band[i][j] >= 175:
                band[i][j] = 175
    
    gh = cv2.calcHist([grayscale],[0],None,[256],[0,256])
    lh = cv2.calcHist([left], [0], None, [256], [0, 256])
    rh = cv2.calcHist([right], [0], None, [256], [0, 256])
    bh = cv2.calcHist([band], [0], None, [256], [0, 256])
    
    plt.subplot(2,2,1)
    plt.title('Grayhist')
    plt.plot(gh)
    
    plt.subplot(2, 2, 2)
    plt.title('Lefthist')
    plt.plot(lh)
    
    plt.subplot(2, 2, 3)
    plt.title('Righthist')
    plt.plot(rh)
    
    plt.subplot(2, 2, 4)
    plt.title('bandhist')
    plt.plot(bh)
    
    plt.show()
    
if __name__ == '__main__':
    main()